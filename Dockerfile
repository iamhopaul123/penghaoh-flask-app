FROM ubuntu:16.04
MAINTAINER Penghao He "hopaul@umich.edu"
RUN apt-get update -y && \
    apt-get install -y python-pip python-dev
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]