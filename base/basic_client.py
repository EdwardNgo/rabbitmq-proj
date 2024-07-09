import ssl
import pika


class BasicPikaClient:

    def __init__(self, host, port, rabbitmq_username, rabbitmq_password):

        # SSL Context for TLS configuration of Amazon MQ for RabbitMQ
        # ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
        # ssl_context.set_ciphers('ECDHE+AESGCM:!ECDSA')

        connection_params = pika.ConnectionParameters(
            host,  # Replace with your RabbitMQ server URL
            port,  # Replace with your RabbitMQ server port if different
            '/',
            pika.PlainCredentials(rabbitmq_username, rabbitmq_password)  # Replace with your credentials - should move with other creds
        )
        # connection_params.ssl_options = pika.SSLOptions(context=ssl_context)

        self.connection = pika.BlockingConnection(connection_params)
        self.channel = self.connection.channel()

