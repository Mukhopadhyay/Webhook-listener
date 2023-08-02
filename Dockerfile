FROM python:3.10-slim

COPY /requirements.txt /requirements.txt
COPY /requirements.doc.txt /requirements.doc.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install -r requirements.doc.txt

# Documentation
COPY ./mkdocs.yml .
COPY ./docs .

# Build documentation
RUN python3 -m mkdocs build

WORKDIR $WORKDIR

COPY ./app .

COPY ./scripts/entrypoint.sh ..
RUN chmod +x  ../entrypoint.sh

ENTRYPOINT .././entrypoint.sh $0 $@
CMD [ "fastapi" ]
