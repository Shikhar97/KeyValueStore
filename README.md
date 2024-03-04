# Project Overview

This project implements a scalable key-value store using Kubernetes (k8s), FastAPI, and Huey as a REDIS queue. 
The key-value store is designed to be highly scalable, robust, and efficient, capable of handling a large number of concurrent requests while maintaining high availability and fault tolerance.

## Key Features

1. **Kubernetes Deployment**: Utilizes Kubernetes for managing deployment, auto-scaling, and management of containerized applications.
2. **FastAPI**: Modern, fast web framework for building APIs with Python 3.7+ based on standard Python type hints.
3. **Huey as a REDIS Queue**: Lightweight task queue built on top of Redis, allows offloading time-consuming tasks to the background.
4. **Scalability**: Designed to scale horizontally by adding more pods/deployments based on the metrics.

<div style="text-align:center">
  <img alt="Demo" src="https://github.com/Shikhar97/KeyValueStore/blob/main/HLA.png" />
</div>

## Project Structure

- `app/`: Contains the main application code
  - `models/`: Data model for our server
  - `Dockerfile`: Dockerfile to create an image for the server
  - `huey_consumer.py`: To run the Huey consumer for the tasks
  - `redis_huey.py`: It contains the functions to Add/Get/Delete key to/from database
  - `requirements.txt`: Dependencies required for this project
  - `main.py`: FastAPI application entry point
- `deployments/`: Kubernetes deployment files
  - `redis/`: To deploy redis on k8 cluster
  - `kvserver/`: To deploy FastApi Server and consumer
- `tests/`: Test cases
- `README.md`: Project documentation


## Prerequisites

Make sure you have the following tools installed on your system:
- Python 3.x
- FastAPI
- Huey
- Redis
- Docker
- Kubernetes (minikube for local development)
- kubectl


## Usage
### Local Setup

**1. Clone the repository and Install dependencies**
```bash
git clone https://github.com/Shikhar97/KeyValueStore.git
cd KeyValueStore/app; pip install -r requirements.txt
```

**2. Run the redis server**
```bash
redis-server
```

**3. Run the FASTApi server**
```bash
python3 uvicorn main:app --host 0.0.0.0 --port 8000
```

**4. Run Huey consumer** 
```bash
python3 huey_consumer.py redis_huey.huey
```


Access FastAPI server at [http://localhost:8000/api/v1/](http://localhost:8000/api/v1) using Postman or any other tool. 


### Kubernetes Setup(Minikube)

**1. Clone the repository**
```bash
git clone https://github.com/Shikhar97/KeyValueStore.git

```

**2. Start minikube(_if not already running_) and Deploy the redis stateful-set**
```bash
minikube start
cd KeyValueStore/deployment/redis
kubectl -n kvstore apply -f redis-statefulSet.yml
```

**3. Deploy the FASTApi server**
```bash
cd KeyValueStore/deployment/kvserver
kubectl -n kvstore apply -f kvserver-deployment.yml
```

**4. Enable port-forwarding** 
```bash
kubectl -n kvstore port-forward svc/fastapi-service 8000:8000
```

**5. Cleanup**
```bash
cd KeyValueStore/deployment/redis
kubectl -n kvstore delete -f redis-statefulSet.yml

cd KeyValueStore/deployment/kvserver
kubectl -n kvstore delete -f kvserver-deployment.yml
minikube stop
minikube delete
```

Access FastAPI server at [http://localhost:8000/api/v1/](http://localhost:8000/api/v1) using Postman or any other tool.


**_Docker images are built on arm64 architechture. Not supported on amd64._**

## API Documentation
Check the available APIs at [http://localhost:8000/docs](http://localhost:8000/docs) 

## Testing
### To run the test cases

1. **Navigate to the root directory of your project:**

    ```bash
    cd KeyValueStore/app
    ```

2. **Install pytest:**

    ```bash
    pip install pytest
    ```

3. **Run the test cases using pytest:**

    ```bash
    pytest tests.py
    ```

The test results will be displayed in the terminal, indicating whether each test passed or failed.


## Acknowledgments

- [Kubernetes](https://kubernetes.io/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Huey](https://huey.readthedocs.io/en/latest/)
- [Postman](https://www.postman.com/)
- [Redis](https://redis.io/docs/about/)


