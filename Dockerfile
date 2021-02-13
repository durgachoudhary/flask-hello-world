FROM python:3-alpine

ADD requirements.txt /tmp/requirements.txt

RUN pip install -r /tmp/requirements.txt

ADD main.py /var/server/main.py

CMD python /var/server/main.py