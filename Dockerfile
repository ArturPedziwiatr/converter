FROM debian:latest

ENV CGO_LDFLAGS="-g -O2 -lm"
ENV PATH="/root/miniconda/bin:${PATH}"

COPY ./script/install.sh /opt/app/install.sh

RUN chmod +x /opt/app/install.sh

RUN /opt/app/install.sh

# SHELL ["conda", "run", "-n", "app_env", "/bin/bash", "-c"]

ENTRYPOINT uvicorn main:app --reload
