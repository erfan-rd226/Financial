from django.urls import path
from . import views


urlpatterns = [
    path('  ',views.Submit_Expense, name='Submit_Expense'),
    path('  ',views.Submit_Inome, name='Submit_Income'),
]
