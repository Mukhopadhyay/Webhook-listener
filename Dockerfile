FROM python:3.10-slim

COPY /requirements.txt /requirements.txt
COPY /requirements.doc.txt /requirements.doc.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install -r requirements.doc.txt

WORKDIR /app

COPY ./app .

COPY ./scripts/start.sh ..
RUN chmod +x  ../start.sh

CMD ["sh", ".././start.sh"]