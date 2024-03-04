# Project Overview

This project implements a scalable key-value store using Kubernetes (k8s), FastAPI, and Huey as a REDIS queue. 
The key-value store is designed to be highly scalable, robust, and efficient, capable of handling a large number of concurrent requests while maintaining high availability and fault tolerance.

## Key Features

1. **Kubernetes Deployment**: Utilizes Kubernetes for managing deployment, auto-scaling, and management of containerized applications.
2. **FastAPI**: Modern, fast web framework for building APIs with Python 3.7+ based on standard Python type hints.
3. **Huey as a REDIS Queue**: Lightweight task queue built on top of Redis, allows offloading time-consuming tasks to the background.
4. **Scalability**: Designed to scale horizontally by adding more pods/deployments based on the metrics.


## Project Structure

- `app/`: Contains the main application code.
  - `models/`: Data models.
  - `Dockerfile`: 
  - `huey_consumer.py`:
  - `redis_huey.py`:
  - `requirements.txt`:
  - `main.py`: FastAPI application entry point.
- `deployments/`: Kubernetes deployment files
  - `redis/`: To deploy redis on k8 cluster.
  - `kvserver/`: To deploy FastApi Server and consumer
- `tests/`: Test cases.
- `README.md`: Project documentation.


## Prerequisites

Make sure you have the following tools installed on your system:
- Python 3.x
- FastAPI
- Huey
- Redis
- Docker
- Kubernetes (minikube for local development)
- kubectl


## Usage(Local)

1. Clone the repository: `git clone https://github.com/Shikhar97/KeyValueStore.git`
2. Install dependencies: `cd KeyValueStore/app; pip install -r requirements.txt`
3. Run the FASTApi server: `python3 uvicorn main:app --host 0.0.0.0 --port 8000`
4. Run Huey consumer: `python3 huey_consumer.py redis_huey.huey`

Access FastAPI server at [http://localhost:8000](http://localhost:8000). 



## Acknowledgments

- [Kubernetes](https://kubernetes.io/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Huey](https://huey.readthedocs.io/en/latest/)