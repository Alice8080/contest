from django.shortcuts import render
from viewflow.urls import ModelViewset

from data.models import CustomUser

# Create your views here.

class CustomUserViewset(ModelViewset):
    model = CustomUser
    # list_columns = '__all__'
    # list_search_fields = '__all__'
    # list_order_columns = '__all__'
