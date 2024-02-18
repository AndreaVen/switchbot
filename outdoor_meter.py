
from datetime import datetime
class Outdoor_meter:

    def __init__(self,temperature=None,humidity=None,timestamp=None):
        self.temperature=temperature
        self.humidity=humidity
        self.timestamp=timestamp

    def validate_input(self):
        if type(self.temperature)!=float:
            Exception
        if type(self.humidity)!=int:
            Exception

        try:
            date = datetime.fromtimestamp(self.timestamp)
            date=2
        except  Exception:
            Exception






