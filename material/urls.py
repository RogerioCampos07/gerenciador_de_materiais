from django.urls import path
from material import views


app_name = 'material'

urlpatterns = [
    path('',views.index,name='index'),
    
]
