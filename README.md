Just Your Bayesic Dropouts

Other modules used are listed below; 
- sqlalchemy
- marshmallow
- sqlalchemy marshmallow
- flask sqlalchemy

###To run locally:

```
git clone
cd bayesic-be
virtualenv venv
source venv/bin/activate
cd src
pip install -r requirements.txt
python -m run 
```

Run tests:
```
nose2 -v
```

###Using Docker
Build with docker: 
```
cd bayesic-be
docker build -t bayesic-be .
```

Run in development mode: 
```
docker run -dt --name=bayesic-be -v $PWD:/app -p 5000:5000 -e 'WORK_ENV=DEV' bayesic-be
```

Run in production mode:
```
docker run -dt --restart=always --name=bayesic-be -p 5000:5000 -e 'WORK_ENV=PROD' bayesic-be
```

Remove the container:
```
docker rm -f bayesic-be
```

To see logs and connect the container:
```
docker logs --follow bayesic-be
docker exec -it bayesic-be bash

```