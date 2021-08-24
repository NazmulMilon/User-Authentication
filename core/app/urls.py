
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('log', views.userlog, name='log'),
    path('show',views.show,name="show"),
    path('edit/<id>',views.edit, name="edit"),
    path('edit/update/<id>',views.update, name="update"),

    path('delete/<id>',views.delete, name="del"),
    path('ss', views.search, name="ss")


]

