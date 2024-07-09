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

Start producer

```
python producer.py
```

Start consumer in other terminal

```
python consumer.py
```
