from xml.dom.domreg import registered
from django.db import models


class Loan_disbursed(models.Model):

    loan_product_name =         models.CharField(max_length=20, default="")
    loan_amount =               models.FloatField(default=0.0)
    interest =                  models.FloatField(default=0.0)
    amount_disbursed =          models.FloatField(default=0.0)
    amount_due =                models.FloatField(default=0.0) 
    princpal_due =              models.FloatField(default=0.0)
    interest_due =              models.FloatField(default=0.0)
    penalty =                   models.FloatField(default=0.0)
    tenor   =                   models.CharField(max_length=20)
    interest_rate =             models.CharField(max_length=30)
    date_disbursed =            models.DateField(auto_now_add=True)
    status =                    models.CharField(max_length=20, default="settled")
    first_payment_due =         models.DateField(auto_now=True)
    last_payment_due =          models.DateField(auto_now=True)
    loan_classification =       models.CharField(max_length=30, default="closed")
    principal_paid =            models.FloatField(default=0.0)
    insterest_paid =            models.FloatField(default=0.0)
    penalty_paid =              models.FloatField(default=0.0)


class extra_informations(models.Model):

    state=                 models.CharField(max_length=50, default="")
    lga=                   models.CharField(max_length=150, default="")
    Nearest_landmark=      models.CharField(max_length=100, default="")
    street=                models.CharField(max_length=50, default="")
    gender=                models.CharField(max_length=10, default="male")
    marital_status=        models.CharField(max_length=100, default="Married")
    education=             models.CharField(max_length=100, default="")
    employment_status=     models.BooleanField(default="False")
    sector=                models.CharField(max_length=100, default="")
    monthly_income=        models.FloatField(default=0.0)
    registered_company=    models.BooleanField(default="False")
    cac =                  models.CharField(max_length=50)   


class Loan_repayments(models.Model):
    pass


class user_cached_loans(models.Model):
    
    # user            =         models.ForeignKey()
    blacklist_score =         models.CharField(max_length=10)
    credolab_score  =         models.CharField(max_length=10)
    pengme_response =         models.CharField(max_length=20)
    hadada_response =         models.CharField(max_length=20)
    loan_offer      =         models.FloatField(default=0.0)
    is_disbursed    =         models.BooleanField(default=False)


class Returning_good_borrowers(models.Model):
    pass 


class loan_performance(models.Model):
    pass 


class Disbursment_transaction(models.Model):
    pass 