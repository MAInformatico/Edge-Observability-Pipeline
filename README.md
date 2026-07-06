# Edge Observability Pipeline

Lightweight distributed observability and alerting system designed for edge and constrained environments (e.g. Raspberry Pi clusters, home labs, or remote infrastructure nodes).

It provides centralized log aggregation, event filtering, and real-time security alerting through a Telegram-based notification pipeline.

The system is inspired by production-grade observability architectures but optimized for simplicity, transparency, and low-resource environments.

---

## 🧠 Problem Statement

Modern systems require visibility into distributed nodes, but full-scale observability stacks (ELK, Datadog, Grafana stacks) are often too heavy for:

- Edge devices (Raspberry Pi, IoT nodes)
- Home lab environments
- Lightweight private infrastructure
- Educational or experimental setups

This project explores how to build a minimal but effective observability pipeline using standard Linux tooling.

---

## 🏗️ Architecture

```text
Client Nodes (Raspberry Pi / Linux Hosts)
        │
        ▼
   rsyslog ingestion layer
        │
        ▼
 /var/log/remote/<hostname>.log
        │
        ▼
 Event filtering layer (security rules)
        │
        ▼
 Telegram alerting daemon (systemd service)
        │
        ▼
   Real-time notifications
```

## ⚙️ Features

- Centralized log aggregation using rsyslog
- Multi-host log separation by hostname
- SSH brute-force detection (Failed password events)
- Lightweight event filtering pipeline
- Real-time alerting via Telegram Bot API
- systemd-managed daemon for reliability
- Designed for low-resource edge devices
- Fully reproducible configuration via Python bootstrapper

## 🚀 Quick Start
### 1. Clone repository
```bash
git clone https://github.com/your-user/edge-observability-pipeline.git
cd edge-observability-pipeline
```
### 2. Configure system
```bash
cp config.example.yml config.yml
```

Edit:

```yaml
telegram:
  token: "YOUR_BOT_TOKEN"
  chat_id: "YOUR_CHAT_ID"

rsyslog:
  remote_port: 514

alerts:
  ssh_failed: true
  log_file: "/var/log/telegram-alerts.log"
```

### 3. Deploy system
```bash
sudo python3 main.py --config config.yml
```

### 4. Test pipeline

From any client node:
```bash
logger "TEST ALERT: system verification"
```

## 📲 Example Alert
```text
🚨 ALERT: Failed password for invalid user admin from 192.168.1.50
```

## 🧱 Design Decisions
### Why rsyslog?

Chosen for its simplicity, low overhead, and native Linux integration. It avoids introducing heavy dependencies.

### Why Telegram?

Provides a zero-infrastructure alerting channel without requiring additional messaging infrastructure.

### Why file-based pipeline?

A deliberate design choice to maintain transparency and debuggability of the system.

## ⚠️ Limitations
- No deduplication or rate limiting of alerts
- No structured log schema (JSON not enforced)
- No persistent queue or backpressure handling
- Not suitable for high-throughput production environments

## 🔭 Future Work
- Add structured logging (JSON + schema validation)
- Introduce alert aggregation (anti-spam / batching)
- Replace file pipeline with event queue (Redis / NATS)
- Add FastAPI control plane for remote configuration
- Export metrics to Prometheus / Grafana
- Multi-node orchestration layer

## 🧠 Key Learnings

This project explores:

- Event-driven system design on constrained hardware
- Trade-offs between simplicity and scalability
- Building observability without heavy external stacks
- Linux-native infrastructure tooling (systemd, rsyslog)
- Distributed log pipeline design principles

## 📦 Tech Stack
- Python 3
- rsyslog
- systemd
- Telegram Bot API
- Linux (Raspberry Pi OS / Debian-based systems)

## 📌 Disclaimer

This project is intended for educational and infrastructure experimentation purposes in controlled environments.

## ⭐ Why this project matters

It demonstrates practical understanding of:

- Distributed systems fundamentals
- Observability pipelines
- Event-driven architecture
- Linux systems engineering
- Lightweight infrastructure design
