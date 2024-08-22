from rest_framework import serializers


class LottoSerializer(serializers.Serializer):
    

    class Meta:
        fields = '__all__'
        model = LottoP1
        