from rest_framework import serializers
from .models import *


class loan_serializer(serializers.ModelSerializer):
    
    model = Loan_data
    fields = "__all__"