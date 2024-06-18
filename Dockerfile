FROM python:slim

WORKDIR /app

ADD ./app /app
ADD ./requirements.txt /

RUN pip install --trusted-host pypi.python.org -r /requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]
