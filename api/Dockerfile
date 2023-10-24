FROM python:3.11.0-alpine AS base

RUN apk update && apk add build-base

WORKDIR /api
ADD ./api /api
RUN pip install -r requirements.txt

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]