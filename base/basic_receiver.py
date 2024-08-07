from base.basic_client import BasicPikaClient
import logging

logger = logging.getLogger()
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.INFO)

def callback(ch, method, properties, body):
    logger.info(f" [x] Received {body}")

class BasicReceiver(BasicPikaClient):

    def __init__(self, configs: dict = None):
        super().__init__(**configs)


    def receive_message(self, queue):
        channel = self.connection.channel()

        channel.queue_declare(queue=queue)

        channel.basic_consume(queue=queue, on_message_callback=callback, auto_ack=True)

        channel.start_consuming()
        
    def close(self):
        self.channel.close()
        self.connection.close()
