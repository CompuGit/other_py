ARG PYTHON_VERSION=3.6
FROM assignments:0.1
ARG PYTHON_VERSION
ENV PYTHON_VERSION=$PYTHON_VERSION

ENV DockerHOME=/opt/sagar/assignments/python 

# set work directory  
RUN mkdir -p $DockerHOME  

# where your code lives  
WORKDIR $DockerHOME 
COPY requirements.txt $DockerHOME 
RUN pip3 install -r requirements.txt  
ENTRYPOINT ["/bin/sh", "-c", "python3 /collector/main.py"]