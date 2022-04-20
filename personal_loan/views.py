from urllib import response
from venv import create

from personal_loan.models import *
from .serializers import *
from rest_framework.views import APIView
from personal_loan.helpers.external_check import ExternalCheck


class loan_data(APIView):

    serializer_class = loan_serializer

    def post(self, request):

        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception=True)

        borrower = serializer.validated_data.get('borrower')
        email    = serializer.validated_data.get('email')
        phone    = serializer.validated_data.get('phone')
        bvn      = serializer.validated_data.get('bvn')
        loan_product_name =  serializer.validated_data.get('loan_product_name')
        loan_amount       =  serializer.validated_data.get ('loan_amount')
        interest          =  serializer.validated_data.get('interest')
        amount_disbursed  =  serializer.validated_data.get('amount_disbursed')
        amount_due        =  serializer.validated_data.get('amount_due')
        princpal_due      =  serializer.validated_data.get('princpal_due')
        interest_due      =  serializer.validated_data.get('interest_due')
        penalty           =  serializer.validated_data.get('penalty')
        tenor             =  serializer.validated_data.get('tenor')
        interest_rate     =  serializer.validated_data.get('interest_rate')
        date_disbursed    =  serializer.validated_data.get('date_disbursed')
        status            =  serializer.validated_data.get('status')
        first_payment_due =  serializer.validated_data.get('first_payment_due')
        last_payment_due  =  serializer.validated_data.get('last_payment_due')
        loan_classification = serializer.validated_date.get('loan_classification')
        principal_paid      = serializer.validated_data.get('principal_paid')
        insterest_paid      = serializer.validated_data.get('insterest_paid')
        penalty_paid        = serializer.validated_data.get('penalty_paid')


        blacklisted = ExternalCheck()
        blacklist = blacklisted.blacklist_status(bvn)

        if blacklist:

            create_loan = Loan_data.objects.create(
                borrower=borrower, 
                phone=phone, 
                email=email,
                bvn=bvn,
                loan_product_name=loan_product_name,
                loan_amount=loan_amount,
                interest=interest,
                amount_disbursed=amount_disbursed,
                amount_due=amount_due,
                princpal_due=princpal_due,
                interest_due=interest_due,
                penalty=penalty,
                tenor=tenor,
                interest_rate=interest_rate,
                date_disbursed=date_disbursed,
                status=status,
                first_payment_due=first_payment_due,
                last_payment_due=last_payment_due,
                loan_classification=loan_classification,
                principal_paid=principal_paid,
                insterest_paid=insterest_paid,
                penalty_paid=penalty_paid
                )















        # try:
        #     user = CustomUser.objects.get(email=request.user.email)
        # except:
        #     data = {
        #         "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
        #         "message": "please login before you can post repayment"


