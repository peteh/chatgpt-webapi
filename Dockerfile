FROM python:3.9-slim-bullseye

RUN apt-get update && \
    apt-get install -y chromium xvfb chromium-driver 

COPY . /app
WORKDIR /app
# CMD ["python", "main.py"]
#CMD ["bash"]
RUN apt-get update; apt-get dist-upgrade; apt-get install -y build-essential python3 swig libpulse-dev 
WORKDIR /app
COPY app/ .
RUN pip3 install -U -r requirements.txt
RUN pip3 install -e pyChatGPT/
RUN ffdl install -y
CMD ["python3", "run.py"]

ENV SERVER_PORT 8000
EXPOSE 8000/tcp
