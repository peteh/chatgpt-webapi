# syntax=docker/dockerfile:1
FROM ultrafunk/undetected-chromedriver:latest
#FROM python:3.10-alpine
#FROM python:3.10-slim-bullseye
#FROM ubuntu:22.10
#alpine
#RUN apk update; apk add build-base swig pulseaudio-dev ffmpeg chromium chromium-chromedriver xvfb 
#debian
#RUN apt-get update; apt-get install -y build-essential python3 swig libpulse-dev ffmpeg chromium chromium-driver xvfb 
#ubuntu 2010
#RUN apt-get update; apt-get install -y build-essential python3 python3-pip swig libpulse-dev ffmpeg chromium-browser chromium-driver xvfb 
# undetected chromedriver
RUN apt-get update; apt-get dist-upgrade; apt-get install -y build-essential python3 swig libpulse-dev 
WORKDIR /app
COPY app/ .
RUN pip3 install -r requirements.txt
RUN ffdl install -y
CMD ["python3", "runIdle.py"]

ENV SERVER_PORT 8000
EXPOSE 8000/tcp
