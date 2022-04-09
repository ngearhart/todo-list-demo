FROM python:3.10

RUN mkdir /todo && pip install flask flask_bootstrap

COPY . /todo
WORKDIR /todo

CMD ["python", "-m", "flask", "--host", "0.0.0.0"]
