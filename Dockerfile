FROM ubuntu:16.04
MAINTAINER Caner Dagli
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential git
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "run.py"]

# docker build -t bayesic-be .
# 
# For Development Container
# docker run -dt --name=bayesic-be -v $PWD:/app -p 5000:5000 -e 'WORK_ENV=DEV' bayesic-be
# 
# For Production Container
# docker run -dt --restart=always --name=bayesic-be -p 5000:5000 -e 'WORK_ENV=PROD' bayesic-be
# 
# Remove the container
# docker rm -f bayesic-be

# docker logs --follow bayesic-be
# docker exec -it bayesic-be bash
