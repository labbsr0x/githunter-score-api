FROM rafaelmm/conductor-client-py:2.31.1

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install -r requirements.txt --ignore-installed

COPY . /app
COPY . /app/usr/lib/python3.8/site-packages/

RUN ls -l /app/usr/lib/python3.8/site-packages/

ENTRYPOINT [ "python3", "-m"]

CMD [ "githunter.app" ]