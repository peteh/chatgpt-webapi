FROM python:3.10-bullseye

COPY . /app
WORKDIR /app
# CMD ["python", "main.py"]
#CMD ["bash"]
#RUN apt-get update; apt-get dist-upgrade; apt-get install -y rustc
ENV PATH="${PATH}:/root/.cargo/bin"
RUN curl --proto '=https' --tlsv1.2 -o rust.sh -sSf https://sh.rustup.rs 
RUN chmod +x rust.sh;./rust.sh -y
WORKDIR /app
COPY app/ .
RUN pip3 install -U -r requirements.txt
CMD ["python3", "run.py"]

ENV SERVER_PORT 8000
EXPOSE 8000/tcp
