FROM python:3
WORKDIR  /usr/app

RUN pip install mysql-connector-python

COPY . .


CMD ["python", "src/app.py"]