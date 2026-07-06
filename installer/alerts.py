from pathlib import Path
import subprocess

ALERT_CONF = "/etc/rsyslog.d/50-alerts.conf"


def run(cmd):
    print(f"[RUN] {cmd}")
    subprocess.run(cmd, shell=True, check=True)


def setup_alerts(config, dry_run=False):
    print("[+] Setting up alerts pipeline")

    log_file = config["alerts"]["log_file"]

    content = f"""
if ($msg contains "Failed password") then {{
    action(type="omfile" file="{log_file}")
}}
"""

    if dry_run:
        print(content)
        return

    Path(log_file).touch(exist_ok=True)

    Path(ALERT_CONF).write_text(content)

    run(f"chmod 666 {log_file}")
    run("systemctl restart rsyslog")
