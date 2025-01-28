| --------------------- | ----------- |
|docker ps | lists all running Docker containers. |
|docker ps -a | lists all Docker containers, including running, stopped, and exited containers.|
|docker image ls | lists all Docker images stored locally on your system. Shows repository name, image ID, size etc. |
| --------------------- | ----------- |
|docker start <> | Starts a stopped container with the specified container ID or name. |
|docker stop <> | Stops a running container gracefully using the specified container ID or name.|
|docker compose up | builds, creates, starts, and attaches containers defined in the docker-compose.yml. |
|docker compose down | stops and removes everything created by docker-compose up. Cleans up everything defined in the docker-compose.yml file. |
| --------------------- | ----------- |
|docker image prune | removes unused Docker images to free up space (Images not associated with any tag). **To remove all** unused images "docker image prune -a". |
|docker container prune | removes stopped containers that are not running. |
| --------------------- | ----------- |
| docker build -t name_of_docker .| Builds a Docker image from the Dockerfile in the current directory and tags it with the specified name (name_of_docker).|
|docker run name_of_docker | Runs a container from the specified image (name_of_docker).|
|docker run --name new_name image_name | Runs a container from image_name and assigns it a custom name (new_name).|
|docker exec -it my_container /bin/bash | Executes a command inside a running container. The command to run inside the container (e.g., /bin/bash).|


| --------------------- | ----------- |
|docker run -it --rm --name 05_demo_container 05_demo_image /bin/bash |
| --------------------- | ----------- |
| -d | **detached mode**: meaning they run in the background without attaching to the terminal.|
|-it | Runs the container in interactive mode, allowing you to interact with it via the terminal.|
|--rm | Automatically removes the container when it stops, keeping your system clean.|
|--name | Assigns a custom name to the container for easier reference.|
|/bin/bash | Starts the container with a Bash shell, allowing you to execute commands inside it.|
|uname | shows operationssystem, te.x. LINUX. |
|cat filename | displays the contents of the file named filename in the terminal. It’s commonly used to quickly view or print the content of a file.|


### **START**
- 1. docker ps/docker image ls - view info
- 2. docker build -t my_image_name - Run the docker build command to create the image from the Dockerfile
- 3. docker run -it --name my_container_name my_image_name - gives image a custom name & create and start a container from it

**If you want to interact with the container through a Bash shell, you can specify /bin/bash explicitly.**
- 4. docker run -it --name my_container_name my_image_name /bin/bash
- 5. docker rm my_container_name - removes containers 
- 6. pip freeze - view your container installments


#after new update ls data - to view - python main.py
#df.head().to_csv(data_path / "prog_book_head.csv")-- porg_book_head adderad 