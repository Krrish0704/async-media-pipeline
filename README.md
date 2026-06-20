# The Hidden Eye - Core Engine

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.138-009688?logo=fastapi&logoColor=white)
![Celery](https://img.shields.io/badge/Celery-5.6-37814A?logo=celery&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-8.0-DC382D?logo=redis&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?logo=docker&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)

The backend engine for **The Hidden Eye**. This is a containerized pipeline that uses FastAPI and Celery to run heavy AI media checks in the background without slowing down the main API.

---

## Architecture

Instead of running everything in a single script, this project splits the workload:

1. FastAPI: Handles incoming media uploads and serves the REST API.
2. Celery: The background worker that picks up heavy AI inference tasks so the API doesn't freeze.
3. Redis: The message broker that passes tasks between FastAPI and Celery.
4. Docker: Containerizes the whole setup so it runs reliably on any machine.

---

## Quickstart

To run this locally, you just need [Git](https://git-scm.com/) and [Docker Desktop](https://www.docker.com/products/docker-desktop/).

### 1. Clone & Setup
Clone the repo and set up your environment variables:
```bash
git clone [https://github.com/Krrish0704/async-media-pipeline.git](https://github.com/Krrish0704/async-media-pipeline.git)
cd async-media-pipeline
cp .env.example .env
```
