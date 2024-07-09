from base.basic_receiver import BasicReceiver
from settings import TOPIC, getRabbitMqConfig

def _receiver():
    receiver = BasicReceiver(getRabbitMqConfig())
    receiver.receive_message(TOPIC)
    
if __name__ == "__main__":
    _receiver()