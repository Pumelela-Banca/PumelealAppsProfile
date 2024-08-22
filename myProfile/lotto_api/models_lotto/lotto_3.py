from django.db import models
from .lotto_1 import LottoP1

# Create your models here.


class LottoP12(models.Model, LottoP1):
    """
    This model will store the information about the Lotto Plus 2 game.
    """

    def __str__(self):
        return f"Lotto Plus 2 - 
        {self.draw_date}-{self.number_1}-{self.number_2}-{self.number_3}-
        {self.number_4}-{self.number_5}-{self.number_6}--{self.bonus_number}"
