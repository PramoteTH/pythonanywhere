from django.urls import path
from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name='index'),
    path('',views.Register, name="Register"),
    path('',views.Login, name="Login"),
    path('',views.Travel, name='Travel'),
    path('',views.Contact, name='Contact'),
    path('',views.Indexforuser, name='Indexforuser'),
    path('',views.Contactforuser, name='Contactforuser'),
    path('',views.Travelforuser, name='Travelforuser'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
