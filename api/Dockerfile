FROM python:3.11.0-alpine AS base

RUN apk update && apk add build-base

WORKDIR /api
ADD ./api /api
RUN pip install -r requirements.txt
RUN python -m spacy download en_core_web_sm

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]