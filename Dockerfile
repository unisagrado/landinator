FROM python:3.9-slim-buster

ARG A_SECRET_KEY=super-secret-key-of-the-app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PORT 8000
ENV SECRET_KEY=${A_SECRET_KEY}}

# install mysqlclient
RUN apt-get update \ 
    && apt-get install -y python3-dev libmysqlclient-dev build-essential

RUN pip install --upgrade pip

RUN mkdir landinator

WORKDIR landinator

COPY requirements.txt requirements-prod.txt manage.py ./

RUN pip install -r requirements-prod.txt

COPY ./landinator ./landinator
COPY ./.docker/entrypoint.sh /bin/entrypoint.sh

RUN python manage.py test

EXPOSE $PORT

ENTRYPOINT ["/bin/entrypoint.sh"]