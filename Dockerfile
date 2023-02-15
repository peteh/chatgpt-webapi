FROM python:3.10-bullseye

COPY . /app
WORKDIR /app
# CMD ["python", "main.py"]
#CMD ["bash"]
#RUN apt-get update; apt-get dist-upgrade; apt-get install -y python3
WORKDIR /app
COPY app/ .
RUN pip3 install -U -r requirements.txt
CMD ["python3", "run.py"]

ENV SERVER_PORT 8000
EXPOSE 8000/tcp
