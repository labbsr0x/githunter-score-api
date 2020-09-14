FROM alpine:latest

ENV LC_ALL C.UTF-8

ENV LANG C.UTF-8

RUN apk update && apk add --update-cache python3 python3-dev py3-pip

RUN pip3 install --upgrade pip

RUN apk add make automake gcc g++ subversion python3-dev

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install -r requirements.txt --ignore-installed

COPY . /app

ENTRYPOINT [ "python3", "-m"]

CMD [ "githunter.app" ]