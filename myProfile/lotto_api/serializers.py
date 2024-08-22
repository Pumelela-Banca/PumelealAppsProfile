from rest_framework import serializers
from .models import *


class LottoSerializer(serializers.ModelSerializer):
    class Meta:
        model = LottoP1
        fields = '__all__'


class LottoSerializer2(serializers.ModelSerializer):
    class Meta:
        model = LottoP2
        fields = '__all__'


class LottoSerializer3(serializers.ModelSerializer):
    class Meta:
        model = LottoP3
        fields = '__all__'


class PowerBallSerializer(serializers.ModelSerializer):
    class Meta:
        model = PowerBall
        fields = '__all__'


class PowerBallPlusSerializer(serializers.ModelSerializer):
    class Meta:
        model = PowerBallP1
        fields = '__all__'


class DailyLottoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Daily
        fields = '__all__'
