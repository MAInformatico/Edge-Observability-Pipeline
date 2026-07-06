from pathlib import Path
import subprocess

CONF_PATH = "/etc/rsyslog.d/30-remote.conf"


def run(cmd):
    print(f"[RUN] {cmd}")
    subprocess.run(cmd, shell=True, check=True)


def setup_rsyslog(config, dry_run=False):
    print("[+] Setting up rsyslog")

    content = f"""
module(load="imudp")
input(type="imudp" port="{config['rsyslog']['remote_port']}")

module(load="imtcp")
input(type="imtcp" port="{config['rsyslog']['remote_port']}")

$template RemoteLogs,"/var/log/remote/%HOSTNAME%.log"

*.* ?RemoteLogs
"""

    if dry_run:
        print(content)
        return

    Path(CONF_PATH).write_text(content)

    run("apt update && apt install -y rsyslog")
    run("mkdir -p /var/log/remote")
    run("chown syslog:adm /var/log/remote")
    run("systemctl restart rsyslog")
