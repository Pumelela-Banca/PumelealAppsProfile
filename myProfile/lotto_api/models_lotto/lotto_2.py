from django.db import models
from .lotto_1 import LottoP1

# Create your models here.


class LottoP2(LottoP1):
    """
    This model will store the information about the Lotto Plus 1 game.
    """

    def __str__(self):
        return (f"Lotto Plus 1 - "
                f"{self.draw_date}-{self.number_1}-{self.number_2}-{self.number_3}-{self.number_4}-"
                f"{self.number_5}-{self.number_6}--{self.bonus_number}")
