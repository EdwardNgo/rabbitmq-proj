from dotenv import load_dotenv
import os
load_dotenv()

PRODUCE_TIME_INTERVAL_IN_SECOND = 5 
TOPIC = 'test'

def getRabbitMqConfig():
    return {
        'host': os.getenv('RABBITMQ_HOST'),
        'port': os.getenv('RABBITMQ_PORT'),
        'rabbitmq_username':os.getenv('RABBITMQ_USERNAME'),
        'rabbitmq_password':os.getenv('RABBITMQ_PASSWORD')
    }