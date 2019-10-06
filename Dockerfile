FROM ubuntu:18.10

LABEL maintainer="Shreya Daing <daing.shreya@gmail.com>"

RUN apt-get update
RUN apt-get install -y python3 python3-dev python3-pip
RUN pip3 install uwsgi

COPY ./ ./app
WORKDIR ./app

RUN pip3 install -r requirements.txt

ENTRYPOINT [ "python3" ]

CMD [ "polestar_api.py" ]
