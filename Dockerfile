FROM ubuntu:latest

ARG STATEMENT="version1"

ENV IMAGE_VERSION=$STATEMENT

RUN apt update

RUN apt install -y git

RUN apt install -y python3

RUN git clone https://github.com/michaelolawoye/testingKubernetesApp.git 

WORKDIR /testingKubernetesApp

RUN echo "This is the read file in container ${STATEMENT}" > read.txt

CMD ["python3", "testpy.py"]