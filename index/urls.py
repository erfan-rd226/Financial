from django.urls import path
from . import views


urlpatterns = [
    path('  ',views.Submit_Expense, name='Submit_Expense')
]
