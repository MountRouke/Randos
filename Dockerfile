FROM python:3.8-slim-buster

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY derk_randos.py ./

EXPOSE 8789

CMD [ "python", "./derk_randos.py", "--server"]