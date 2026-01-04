FROM ubuntu:latest

ARG STATEMENT="v1"

RUN apt update

RUN apt install -y git

RUN apt install -y python3

RUN git clone https://github.com/michaelolawoye/testingKubernetesApp.git 

WORKDIR /testingKubernetesApp

RUN echo "This is the read file in container ${STATEMENT}" > read.txt

CMD ["python3", "testpy.py"]