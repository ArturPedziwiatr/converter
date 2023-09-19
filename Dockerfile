FROM archlinux:latest

ENV CGO_LDFLAGS="-g -O2 -lm"
COPY . /opt/app
EXPOSE 80

RUN chmod +x /opt/app/script/install.sh
RUN chmod +x /opt/app/script/start.sh
RUN /opt/app/script/install.sh

ENTRYPOINT ["bash", "/opt/app/script/start.sh"]
