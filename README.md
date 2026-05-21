# DataTopics • Data Engineering

Modern, open source and project-based data engineering learning platform focused on real-world engineering practices.

---

## Philosophy

This project was designed to teach modern data engineering through a progressive and practical approach.

Instead of isolated tutorials, students build and evolve a complete local data platform using modern open source tools and real-world datasets.

The course structure combines:

* Project-Based Learning (PBL)
* Incremental engineering practices
* Experiential learning
* Gamified progression systems

Core principles:

* Engineering-first mindset
* Local-first architecture
* Open source technologies
* Real-world workflows
* Incremental platform evolution
* Autonomous problem solving

---

## Learning Platform

The repository includes an interactive learning platform built with Streamlit.

Current platform features:

* Learner dashboard
* Repository analysis
* Progress tracking
* Automatic module validation
* Multilingual documentation support
* Incremental course progression

---

## What You Will Build

Throughout the course, students progressively build a modern local data platform capable of:

* Batch data ingestion
* API integrations
* Distributed processing
* Streaming pipelines
* Data modeling
* Orchestration
* Lakehouse architectures
* Analytical transformations
* Operational monitoring

---

## Tech Stack

### Languages

* Python
* SQL

### Infrastructure

* Docker
* Docker Compose

### Databases & Storage

* PostgreSQL
* DuckDB
* Apache Iceberg

### Processing & Transformation

* PySpark
* dbt

### Orchestration & Streaming

* Apache Airflow
* Apache Kafka

### Platform & Visualization

* Streamlit

---

## Prerequisites

Before starting, make sure you have installed:

* Git
* Docker Desktop
* VSCode

Recommended:

* WSL2 (Windows users)

---

## Getting Started

### 1. Fork this repository

Click the `Fork` button at the top-right corner of this repository.

---

### 2. Clone your fork

```bash
git clone <your-fork-url>
cd datatopics-data-engineering
```

---

### 3. Start the platform

```bash
docker compose up
```

---

### 4. Open the learning platform

Open your browser at:

```text
http://localhost:8501
```

---

## Repository Structure

```text
course/       # Course modules and learner progress
docs/         # Multilingual documentation
platform/     # Streamlit learning platform
tooling/      # Validators and automation tooling
```

---

## Development Workflow

This project uses:

* uv for dependency management
* Ruff for linting and formatting
* pre-commit for local validation

Run validations locally:

```bash
uv run ruff check .
uv run ruff format .
uv run pre-commit run --all-files
```

---

## Course Structure

The repository evolves progressively throughout the course.

New services, tools and architectural components are introduced module by module as students build the platform step by step.

---

## Status

🚧 Work in progress

---

## License

Apache License 2.0
