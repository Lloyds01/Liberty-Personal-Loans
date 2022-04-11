from rest_framework import serializers
from .models import Loans


class loan_serializer(serializers.ModelSerializer):
    
    model = Loans
    fields = "__all__"