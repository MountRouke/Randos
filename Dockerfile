FROM debian:stable

RUN apt-get update && apt-get install -y \
    python3 python3-pip curl unzip libgconf-2-4 \
    xvfb chromium

RUN pip3 install gym-derk==0.3.7

COPY main.py main.py
COPY start.sh start.sh
RUN chmod +x start.sh

ENV DERK_CHROME_EXECUTABLE chromium

CMD ["/start.sh"]