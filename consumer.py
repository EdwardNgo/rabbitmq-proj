from base.basic_receiver import BasicReceiver
from settings import TOPIC

def _receiver():
    receiver = BasicReceiver()
    receiver.receive_message(TOPIC)
    
if __name__ == "__main__":
    _receiver()