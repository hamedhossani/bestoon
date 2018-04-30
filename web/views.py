from  json import JSONEncoder
from django.shortcuts import render
from  django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt

from web.models import User,Token,Expense,Income
from datetime import datetime
# Create your views here.
@csrf_exempt
def submit_expense(request):
    """ user submit an expense """
#    return HttpResponse ('we are hear')
    #print("i am in submit")
    #print(request.POST)

    this_token = request.POST['token']
    this_user = User.objects.filter(token__token = this_token).get()
    date_now =  datetime.now()
    this_text = request.POST['text']
    Expense.objects.create(
            user = this_user,
            amount=request.POST['amount'],
            date = date_now,
            text = this_text
            )

    return JsonResponse(
                        {
                            'status':'ok',
                        },encoder=JSONEncoder)
@csrf_exempt
def submit_income(request):
    """ user submit an expense """

    this_token = request.POST['token']
    this_user = User.objects.filter( token__token = this_token ).get()
    date_now =   datetime.now()
    this_text = request.POST['text']
    Income.objects.create(
            user = this_user,
            amount=request.POST['amount'],
            date = date_now,
            text = this_text
            )

    return JsonResponse(
                        {
                            'status':'ok',
                        },encoder=JSONEncoder)
