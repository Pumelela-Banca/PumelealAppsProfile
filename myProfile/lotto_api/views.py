"""
Views for the lotto_api app.
"""
from django.shortcuts import render
from datetime import datetime
from rest_framework import generics
from .models import *
from .serializers import *
from django.shortcuts import get_object_or_404


# Create your views here.

# about API

def render_about_api(request):
    """
    Api usage information.
    """
    return render(request, 'about_api.html')


class Lotto2Lister(generics.ListCreateAPIView):
    """
    This class will return all the lotto 3 numbers.
    """
    queryset = LottoP2.objects.all()
    serializer_class = LottoSerializer2


class Lotto1Lister(generics.ListCreateAPIView):
    """
    This class will return all the lotto numbers.
    """
    queryset = LottoP1.objects.all()
    serializer_class = LottoSerializer


class Lotto3Lister(generics.ListCreateAPIView):
    """
    This class will return all the lotto 3 numbers.
    """
    queryset = LottoP3.objects.all()
    serializer_class = LottoSerializer3

class PowerBallLister(generics.ListCreateAPIView):
    """
    This class will return all the powerball numbers.
    """
    queryset = PowerBall.objects.all()
    serializer_class = PowerBallSerializer


class PowerBallPlusLister(generics.ListCreateAPIView):
    """
    This class will return all the powerball plus numbers.
    """
    queryset = PowerBallP1.objects.all()
    serializer_class = PowerBallPlusSerializer


class DailyLottoLister(generics.ListCreateAPIView):
    """
    This class will return all the daily lotto numbers.
    """
    queryset = Daily.objects.all()
    serializer_class = DailyLottoSerializer


# Get latest lotto number

class Lotto2Detail(generics.RetrieveUpdateDestroyAPIView):
    """
    This class will return a single lotto number.
    """
    serializer_class = LottoSerializer2

    def get_queryset(self):
        queryset = LottoP2.objects.all()
        if queryset.exists():
            return queryset.last()
        return LottoP2.objects.none()


class Lotto1Detail(generics.RetrieveUpdateDestroyAPIView):
    """
    This class will return a single lotto number.
    """
    serializer_class = LottoSerializer

    def get_queryset(self):
        queryset = LottoP1.objects.all()
        if queryset.exists():
            return queryset.last()
        return LottoP1.objects.none()


class Lotto3Detail(generics.RetrieveUpdateDestroyAPIView):
    """
    This class will return a single lotto number.
    """
    serializer_class = LottoSerializer3

    def get_queryset(self):
        queryset = LottoP3.objects.all()
        if queryset.exists():
            return queryset.last()
        return LottoP3.objects.none()


class PowerBallDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    This class will return a single powerball number.
    """
    
    serializer_class = PowerBallSerializer

    def get_queryset(self):
        queryset = PowerBall.objects.all()
        if queryset.exists():
            return queryset.last()
        return PowerBall.objects.none()
    

class PowerBallPlusDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    This class will return a single powerball plus number.
    """
    serializer_class = PowerBallPlusSerializer

    def get_queryset(self):
        queryset = PowerBallP1.objects.all()
        if queryset.exists():
            return queryset.last()
        return PowerBallP1.objects.none()


class DailyLottoDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    This class will return a single daily lotto number.
    """
    serializer_class = DailyLottoSerializer

    def get_queryset(self):
        queryset = Daily.objects.all()
        if queryset.exists():
            return queryset.last()
        return Daily.objects.none()


# Get numbers for specific date

class Lotto1Date(generics.RetrieveUpdateDestroyAPIView):
    """
    This class will return a single lotto number. For a specific date.
    """
    serializer_class = LottoSerializer

    def get_queryset(self):
        return LottoP1.objects.all()

    def get_object(self):
        """
        This view should return a list of all the lotto numbers
        for the date as determined by the URL.
        """
        queryset = self.get_queryset()
        year = self.kwargs['year']
        month = self.kwargs['month']
        day = self.kwargs['day']
        date = datetime(year, month, day)
        obj = get_object_or_404(queryset, date=date)
        return obj


class Lotto2Date(generics.RetrieveUpdateDestroyAPIView):
    """
    This class will return a single lotto number. For a specific date.
    """
    serializer_class = LottoSerializer2

    def get_queryset(self):
        return LottoP2.objects.all()

    def get_object(self):
        """
        This view should return a list of all the lotto numbers
        for the date as determined by the URL.
        """
        queryset = self.get_queryset()
        year = self.kwargs['year']
        month = self.kwargs['month']
        day = self.kwargs['day']
        date = datetime(year, month, day)
        obj = get_object_or_404(queryset, date=date)
        return obj


class Lotto3Date(generics.RetrieveUpdateDestroyAPIView):
    """
    This class will return a single lotto number. For a specific date.
    """
    serializer_class = LottoSerializer3

    def get_queryset(self):
        return LottoP3.objects.all()

    def get_object(self):
        """
        This view should return a list of all the lotto numbers
        for the date as determined by the URL.
        """
        queryset = self.get_queryset()
        year = self.kwargs['year']
        month = self.kwargs['month']
        day = self.kwargs['day']
        date = datetime(year, month, day)
        obj = get_object_or_404(queryset, date=date)
        return obj


class PowerBallDate(generics.RetrieveUpdateDestroyAPIView):
    """
    This class will return a single powerball number. For a specific date.
    """
    serializer_class = PowerBallSerializer

    def get_queryset(self):
        return PowerBall.objects.all()

    def get_object(self):
        """
        This view should return a list of all the powerball numbers
        for the date as determined by the URL.
        """
        queryset = self.get_queryset()
        year = self.kwargs['year']
        month = self.kwargs['month']
        day = self.kwargs['day']
        date = datetime(year, month, day)
        obj = get_object_or_404(queryset, date=date)
        return obj


class PowerBallPlusDate(generics.RetrieveUpdateDestroyAPIView):
    """
    This class will return a single powerball plus number. For a specific date.
    """
    serializer_class = PowerBallPlusSerializer

    def get_queryset(self):
        return PowerBallP1.objects.all()

    def get_object(self):
        """
        This view should return a list of all the powerball plus numbers
        for the date as determined by the URL.
        """
        queryset = self.get_queryset()
        year = self.kwargs['year']
        month = self.kwargs['month']
        day = self.kwargs['day']
        date = datetime(year, month, day)
        obj = get_object_or_404(queryset, date=date)
        return obj


class DailyLottoDate(generics.RetrieveUpdateDestroyAPIView):
    """
    This class will return a single daily lotto number. For a specific date.
    """
    serializer_class = DailyLottoSerializer

    def get_queryset(self):
        return Daily.objects.all()

    def get_object(self):
        """
        This view should return a list of all the daily lotto numbers
        for the date as determined by the URL.
        """
        queryset = self.get_queryset()
        year = self.kwargs['year']
        month = self.kwargs['month']
        day = self.kwargs['day']
        date = datetime(year, month, day)
        obj = get_object_or_404(queryset, date=date)
        return obj
