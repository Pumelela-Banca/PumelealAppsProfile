from django.db import models

# Create your models here.


class Daily(models.Model):
    """
    This model will store the information about the daily Lotto game.
    """
    draw_date = models.DateField()
    number_1 = models.IntegerField()
    number_2 = models.IntegerField()
    number_3 = models.IntegerField()
    number_4 = models.IntegerField()
    number_5 = models.IntegerField()
    
    # Divsions winners
    div_winners_1 = models.IntegerField()
    div_winners_2 = models.IntegerField()
    div_winners_3 = models.IntegerField()
    div_winners_4 = models.IntegerField()

    # Divsions prises
    div_prise_1 = models.FloatField()
    div_prise_2 = models.FloatField()
    div_prise_3 = models.FloatField()
    div_prise_4 = models.FloatField()

    def __str__(self):
        return (f"Daily Lotto - " 
                f"{self.draw_date}-{self.number_1}-{self.number_2}-{self.number_3}-" 
                f"{self.number_4}-{self.number_5}")
