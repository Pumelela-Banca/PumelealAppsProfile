from django.db import models
from .power_2 import PowerBall

# Create your models here.


class PowerBallP1(models.Model, PowerBall):
    """
    This model will store the information about the Power Ball 2 game.
    """

    def __str__(self):
        return f"Power Ball Plus - 
        {self.date}-{self.number_1}-{self.number_2}-{self.number_3}-{self.number_4}-
        {self.number_5}-{self.number_6}--{self.bonus_number}"
