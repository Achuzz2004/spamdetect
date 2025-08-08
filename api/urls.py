from django.urls import path
from .views import home, predict_spam

urlpatterns = [
    path('', home,),
    path('predict_spam/', predict_spam),
]