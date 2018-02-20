"""ethercheck URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from website import views

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^transactions$', views.transactions, name="transactions"),
    url(r'^alias$', views.alias, name="alias"),
    url(r'^graph$', views.graph, name="graph"),
    url(r'^visgraph2$', views.visgraph2, name="visgraph2"),
    url(r'^visgraph3$', views.visgraph3, name="visgraph3"),
    url(r'^visgraph$', views.visgraph, name="visgraph"),
    url(r'^graphData$', views.graphData, name="graphData"),
    url(r'^tauxChange$', views.tauxChange, name="tauxChange"),
    url(r'^blocks$', views.blocks, name="blocks")
]
