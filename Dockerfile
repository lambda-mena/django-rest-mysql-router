FROM python:3.11

# Setting fallback variables
ENV SECRET_KEY=insecure-u4%24F#7_4AWw$/WAR/1b+89#24%!8l4
ENV DEBUG=0
ENV HOSTNAME=*

WORKDIR /

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN python manage.py migrate

EXPOSE 8000

CMD ["gunicorn", "-b", "0.0.0.0:8000", "core.wsgi"]