FROM debian:stable

RUN apt-get update && apt-get install -y \
    python3 python3-pip curl unzip libgconf-2-4 \
    xvfb chromium

RUN pip3 install http://files.mountrouke.com/gym-derk/gym_derk-0.1.21.tar.gz

COPY main.py main.py
COPY start.sh start.sh
RUN chmod +x start.sh

ENTRYPOINT ["/start.sh"]