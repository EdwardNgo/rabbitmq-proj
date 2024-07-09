from base.basic_sender import BasicSender
import time
from datetime import datetime
import uuid
import json
from settings import TOPIC, PRODUCE_TIME_INTERVAL_IN_SECOND, getRabbitMqConfig

def _producer():
    sender = BasicSender(getRabbitMqConfig())
    try:
        while True:
            # Publish a message
            message = {"message_id": str(uuid.uuid4()), "created_on": datetime.now().timestamp()}
            sender.send_message(exchange='', routing_key=TOPIC, body=json.dumps(message))
            # Wait for 5 seconds before sending the next message
            time.sleep(PRODUCE_TIME_INTERVAL_IN_SECOND)
    except KeyboardInterrupt:
        print("Interrupted")
    finally:
        # Close the connection
        sender.close()
        
if __name__ == "__main__":
    _producer()