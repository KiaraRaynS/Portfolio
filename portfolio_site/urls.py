from django.conf.urls import url
from django.contrib import admin
from appportfolio.views import IndexView, PortfolioView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', IndexView.as_view(), name='indexview'),
    url(r'^portfolio/$', PortfolioView.as_view(), name='portfolioview'),
]
