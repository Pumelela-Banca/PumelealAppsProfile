from django.urls import path
from lotto_api.views import (Lotto1Lister, Lotto2Lister, Lotto3Lister,
                             PowerBallLister, PowerBallPlusLister,
                             DailyLottoLister, Lotto1Detail, Lotto2Detail,
                             Lotto3Detail, PowerBallDetail, PowerBallPlusDetail,
                             Lotto1Date, Lotto2Date, Lotto3Date, PowerBallDate,
                             PowerBallPlusDate, DailyLottoDate)
from django.conf.urls import handler404


handler404 = render_404