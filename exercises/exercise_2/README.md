## 2. Theory questions - docker

### a) What is the purpose of a dockerfile?

**Explanation:**
A Dockerfile is a script that contains a series of instructions used to automate the process of building a Docker image. It defines the environment, dependencies, and configurations needed for an application to run inside a container.

**Answer:**
- The purpose of a Dockerfile is to provide a repeatable, consistent way to build Docker images. It defines the base image, installs dependencies, copies files, and configures the container's environment.
  
  Example:
  ```dockerfile
  FROM python:3.9
  RUN pip install flask
  COPY . /app
  CMD ["python", "app.py"]```


### b) What is the purpose of dockerizing an app?

**Explanation:** Dockerizing an app refers to the process of packaging an application and its dependencies into a Docker container, which ensures that the app runs consistently across different environments.

**Answer:**
    The purpose of dockerizing an app is to ensure that it runs the same way in development, testing, and production environments. It isolates the app from underlying system differences and dependencies, making it easier to deploy and scale.

### c) What is the difference between dockerfile and docker compose?

**Answer:**
    A Dockerfile is a script that contains a series of instructions for creating a Docker image.
    Docker Compose is a tool for defining and running multi-container Docker applications, using a docker-compose.yml file to specify the services, networks, and volumes required.

### d) What is Docker, and how does it differ from traditional virtualization?

**Answer:**
    Docker allows applications to run in isolated containers that share the host system’s OS kernel. Containers are lightweight and fast compared to virtual machines, which require separate operating systems.
    Traditional virtualization uses hypervisors to run entire virtual machines with their own operating systems, which are more resource-intensive.

### e) What are the key components of Docker?

**Explanation:** Docker has several key components that work together to build, run, and manage containers.

**Answer:**
- Docker Engine: The runtime environment for building and running Docker containers.
- Docker Images: Read-only templates used to create containers.
- Docker Containers: A running instance of a Docker image.
- Docker Hub: A cloud-based registry service for storing Docker images.
- Docker Compose: A tool for defining and running multi-container Docker applications. 

### f) What is a Docker image, and how is it different from a container?
**Explanation:** A Docker image is a read-only template that contains the code, libraries, and dependencies needed to run an application. A container is a running instance of a Docker image.


### g) What is a Docker volume, and why is it used?