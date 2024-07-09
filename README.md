### Prerequisite

Make sure to have rabbitmq instance running in your machine

```
docker run -d --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:management
```

Install python package with virtual-env

```
python3 -m venv venv 
```

Or
```
virtualenv -p <your python version> venv
```

Install python package
```
source venv/bin/activate
pip install -r requirements.txt
```

### Main

Create .env file with this default value if you are using local rabbitmq or you can change it with yours

```
RABBITMQ_HOST=localhost
RABBITMQ_PORT=5672
RABBITMQ_USERNAME=guest
RABBITMQ_PASSWORD=guest
```


Start producer

```
python producer.py
```

Start consumer in other terminal

```
python consumer.py
```

### TODO

We want to store the .env in some kind of format so I will leave it with a local config -> I choose .env