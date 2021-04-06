FROM alpine:latest

ENV LC_ALL C.UTF-8

ENV LANG C.UTF-8

RUN apk update && apk add --update-cache python3 python3-dev py3-pip git

RUN pip3 install --upgrade pip

RUN apk add make automake gcc g++ subversion python3-dev

COPY . /app

RUN ln -sf python3 /usr/bin/python

RUN git clone https://github.com/Netflix/conductor.git --branch v2.31.1 --single-branch
RUN cd conductor/client/python && python3 setup.py install


COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install -r requirements.txt --ignore-installed

COPY . /app/usr/lib/python3.8/site-packages/

RUN ls -l

ENTRYPOINT [ "python3", "-m"]

CMD [ "githunter.app" ]