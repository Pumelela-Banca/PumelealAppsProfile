from django.db import models
from .power_1 import PowerBall

# Create your models here.


class PowerBallP1(PowerBall):
    """
    This model will store the information about the Power Ball 2 game.
    """

    def __str__(self):
        return (f"Power Ball Plus -"
                f"{self.date}-{self.number_1}-{self.number_2}-{self.number_3}-{self.number_4}-"
                f"{self.number_5}--{self.bonus_number}")
