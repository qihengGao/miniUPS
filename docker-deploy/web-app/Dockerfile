FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip3 install -r requirements.txt
RUN pip3 install protobuf
ADD . /code/
RUN chmod o+x runserver.sh
RUN chmod o+x initserver.sh
RUN chmod o+x runclient.sh
