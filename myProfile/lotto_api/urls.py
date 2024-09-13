from django.urls import path
from lotto_api.views import (Lotto1Lister, Lotto2Lister, Lotto3Lister,
                             PowerBallLister, PowerBallPlusLister,
                             DailyLottoLister, Lotto1Detail, Lotto2Detail,
                             Lotto3Detail, PowerBallDetail, PowerBallPlusDetail,
                             Lotto1Date, Lotto2Date, Lotto3Date, PowerBallDate,
                             PowerBallPlusDate, DailyLottoDate, render_about_api,
                             DailyLottoDetail)


urlpatterns = [
    path("", render_about_api, name="about_api"),
    path("powerball/", PowerBallLister.as_view(), name="powerball"),
    path("powerball/recent", PowerBallDetail.as_view(), name="powerball_detail"),
    path("powerball/date/<int:year>/<int:month>/<int:day>", PowerBallDate.as_view(), name="powerball_date"),
    path("powerballplus/", PowerBallPlusLister.as_view(), name="powerballplus"),
    path("powerballplus/recent", PowerBallPlusDetail.as_view(), name="powerballplus_detail"),
    path("powerballplus/date/<int:year>/<int:month>/<int:day>", PowerBallPlusDate.as_view(), name="powerballplus_date"),
    path("dailylotto/", DailyLottoLister.as_view(), name="dailylotto"),
    path("dailylotto/recent", DailyLottoDetail.as_view(), name="dailylotto_detail"),
    path("dailylotto/date/<int:year>/<int:month>/<int:day>", DailyLottoDate.as_view(), name="dailylotto_date"),
    path("lotto1/", Lotto1Lister.as_view(), name="lotto1"),
    path("lotto1/recent", Lotto1Detail.as_view(), name="lotto1_detail"),
    path("lotto1/date/<int:year>/<int:month>/<int:day>", Lotto1Date.as_view(), name="lotto1_date"),
    path("lotto2/", Lotto2Lister.as_view(), name="lotto2"),
    path("lotto2/recent", Lotto2Detail.as_view(), name="lotto2_detail"),
    path("lotto2/date/<int:year>/<int:month>/<int:day>", Lotto2Date.as_view(), name="lotto2_date"),
    path("lotto3/", Lotto3Lister.as_view(), name="lotto3"),
    path("lotto3/recent", Lotto3Detail.as_view(), name="lotto3_detail"),
    path("lotto3/date/<int:year>/<int:month>/<int:day>", Lotto3Date.as_view(), name="lotto3_date"),
]


