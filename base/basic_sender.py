from base.basic_client import BasicPikaClient
import logging
logger = logging.getLogger()
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.INFO)

class BasicSender(BasicPikaClient):

    def __init__(self, configs: dict = None):
        """

        :param configs: Configurations for the pika client.
        """
        super().__init__(**configs)

    def declare_queue(self, queue_name):
        logger.info(f"Trying to declare queue({queue_name})...")
        self.channel.queue_declare(queue=queue_name)

    def send_message(self, exchange, routing_key, body):
        channel = self.connection.channel()
        logger.info(f'Message {body}')
        channel.basic_publish(exchange=exchange,
                              routing_key=routing_key,
                              body=body)
        logger.info(f"Sent message. Exchange: {exchange}, Routing Key: {routing_key}, Body: {body}")

    def close(self):
        self.channel.close()
        self.connection.close()

