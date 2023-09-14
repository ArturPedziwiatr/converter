FROM debian:latest

ENV CGO_LDFLAGS="-g -O2 -lm"
ENV PATH="/root/miniconda/bin:${PATH}"
ENV PATH="/usr/local/go/bin:${PATH}"

COPY . /opt/app

RUN chmod +x /opt/app/script/install.sh
RUN /opt/app/script/install.sh

SHELL ["conda", "run", "-n", "app_env", "/bin/bash", "-c"]
SHELL ["pip", "install", "-r", "./requirements.txt"]

ENTRYPOINT bash /opt/app/script/start.sh
