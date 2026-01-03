FROM ubuntu:latest as stage1

RUN apt install python3

RUN apt install python3-tk