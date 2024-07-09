FROM python:slim

WORKDIR /app

ADD ./requirements.txt /

RUN pip install --trusted-host pypi.python.org -r /requirements.txt

ADD ./app /app

EXPOSE 5000

CMD ["python", "app.py"]
