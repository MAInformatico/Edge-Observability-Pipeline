from pathlib import Path
import subprocess

WATCHER = "/usr/local/bin/tg-watch.sh"
SERVICE = "/etc/systemd/system/tg-watch.service"


def run(cmd):
    print(f"[RUN] {cmd}")
    subprocess.run(cmd, shell=True, check=True)


def setup_telegram(config, dry_run=False):
    print("[+] Setting up Telegram watcher")

    token = config["telegram"]["token"]
    chat_id = config["telegram"]["chat_id"]
    log_file = config["alerts"]["log_file"]

    script = f"""#!/bin/bash

TOKEN="{token}"
CHAT_ID="{chat_id}"

tail -Fn0 {log_file} | while read line
do
    curl -s -X POST "https://api.telegram.org/bot$TOKEN/sendMessage" \\
    -d "chat_id=$CHAT_ID" \\
    -d "text=🚨 ALERTA: $line" > /dev/null
done
"""

    service = f"""
[Unit]
Description=Telegram Watcher
After=network.target

[Service]
ExecStart={WATCHER}
Restart=always
User=root

[Install]
WantedBy=multi-user.target
"""

    if dry_run:
        print(script)
        print(service)
        return

    Path(WATCHER).write_text(script)
    Path(WATCHER).chmod(0o755)

    Path(SERVICE).write_text(service)

    run("systemctl daemon-reload")
    run("systemctl enable tg-watch")
    run("systemctl restart tg-watch")
