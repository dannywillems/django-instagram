FROM python:3.6

COPY . /usr/src/app
RUN rm -f /usr/src/app/db.sqlite3
WORKDIR /usr/src/app
RUN mkdir -p .data

#ENV DATABASE_HOST django.db.backends.sqlite3
#ENV DATABASE_PORT
#ENV DATABASE_USER
#ENV DATABASE_PASSWORD
#ENV DATABASE_NAME db.sqlite3

RUN pip install pipenv
RUN pipenv install --deploy


EXPOSE 8000

CMD pipenv run python manage.py migrate && /usr/src/app/start.sh