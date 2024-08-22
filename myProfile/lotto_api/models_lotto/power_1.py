from django.db import models

# Create your models here.


class PowerBall(models.Model):
    """
    This model will store the power ball numbers.
    """
    date = models.DateField()
    number_1 = models.IntegerField()
    number_2 = models.IntegerField()
    number_3 = models.IntegerField()
    number_4 = models.IntegerField()
    number_5 = models.IntegerField()
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
    div_winners_9 = models.IntegerField()

    # Divsions prises
    div_prise_1 = models.FloatField()
    div_prise_2 = models.FloatField()
    div_prise_3 = models.FloatField()
    div_prise_4 = models.FloatField()
    div_prise_5 = models.FloatField()
    div_prise_6 = models.FloatField()
    div_prise_7 = models.FloatField()
    div_prise_8 = models.FloatField()
    div_prise_9 = models.FloatField()

    def __str__(self):
        return f"Power Ball - 
        {self.date}-{self.number_1}-{self.number_2}-{self.number_3}-{self.number_4}-
        {self.number_5}--{self.bonus_number}"