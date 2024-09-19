from django.db import models

# Create your models here.


class LottoP3(models.Model):
    """
    This model will store the information about the Lotto Plus 2 game.
    """
    draw_date = models.CharField(max_length=50)
    number_1 = models.IntegerField()
    number_2 = models.IntegerField()
    number_3 = models.IntegerField()
    number_4 = models.IntegerField()
    number_5 = models.IntegerField()
    number_6 = models.IntegerField()
    bonus_number = models.IntegerField()
    
    # Divsions winners
    div_winners_1 = models.IntegerField()
    div_winners_2 = models.IntegerField()
    div_winners_3 = models.IntegerField()
    div_winners_4 = models.IntegerField()
    div_winners_5 = models.IntegerField()
    div_winners_6 = models.IntegerField()
    div_winners_7 = models.IntegerField()
    div_winners_7 = models.IntegerField()
    div_winners_8 = models.IntegerField()

    # Divsions prises
    div_prise_1 = models.FloatField()
    div_prise_2 = models.FloatField()
    div_prise_3 = models.FloatField()
    div_prise_4 = models.FloatField()
    div_prise_5 = models.FloatField()
    div_prise_6 = models.FloatField()
    div_prise_7 = models.FloatField()
    div_prise_8 = models.FloatField()


    def __str__(self):
        return (f"Lotto Plus 2 -"
                f"{self.draw_date}-{self.number_1}-{self.number_2}-{self.number_3}-{self.number_4}-"
                f"{self.number_5}-{self.number_6}--{self.bonus_number}")
