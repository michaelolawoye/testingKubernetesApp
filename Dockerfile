FROM ubuntu:latest

RUN apt update

RUN apt install -y git

RUN apt install -y python3

RUN apt install -y python3-venv

RUN git clone https://github.com/michaelolawoye/testingKubernetesApp.git 

WORKDIR /testingKubernetesApp

CMD ["python3", "testpy.py"]