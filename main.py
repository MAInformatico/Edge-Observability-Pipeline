#!/usr/bin/env python3
import argparse
import yaml
from installer.rsyslog import setup_rsyslog
from installer.alerts import setup_alerts
from installer.telegram import setup_telegram


def load_config(path):
    with open(path, "r") as f:
        return yaml.safe_load(f)


def main():
    parser = argparse.ArgumentParser(description="Edge Log Bootstrapper")
    parser.add_argument("--config", required=True, help="Path to YAML config")
    parser.add_argument("--dry-run", action="store_true")

    args = parser.parse_args()
    config = load_config(args.config)

    print("=== Edge Log Bootstrapper v2 ===")

    setup_rsyslog(config, dry_run=args.dry_run)
    setup_alerts(config, dry_run=args.dry_run)
    setup_telegram(config, dry_run=args.dry_run)

    print("\n✔ Setup completed successfully")


if __name__ == "__main__":
    main()
