FROM python:3.10-slim

COPY /requirements.txt /requirements.txt
COPY /requirements.doc.txt /requirements.doc.txt

# ENV MODE=development
# ENV WORKERS=1
# ENV LOG_LEVEL=INFO
# ENV WORKDIR="/app"

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install -r requirements.doc.txt

WORKDIR $WORKDIR

COPY ./app .

COPY ./scripts/entrypoint.sh ..
RUN chmod +x  ../entrypoint.sh

# CMD ["sh", ".././entrypoint.sh"]
ENTRYPOINT .././entrypoint.sh $0 $@
CMD [ "fastapi" ]
