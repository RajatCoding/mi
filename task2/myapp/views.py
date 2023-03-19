from django.shortcuts import render
import datetime
# Create your views here.


def calc(request):
    if request.method == "POST":
        hidden_val = request.POST["val"]
        period = request.POST["period"]
        rate = request.POST["rate"]
        interest_amount = request.POST["interest_amount"]
        investment_amount = request.POST["investment_amount"]
        maturity_amount = request.POST["maturity_amount"]
        due_date = request.POST["due_date"]
        investment_date = request.POST["investment_date"]
        date_format = "%Y-%m-%d"
        

        if investment_date and due_date and not period:
            due_date = datetime.datetime.strptime(due_date, date_format)
            investment_date = datetime.datetime.strptime(investment_date, date_format)
            period = abs((due_date-investment_date).days)
            
        
        elif investment_date and period and not due_date: 
            investment_date = datetime.datetime.strptime(investment_date, date_format)
            period = datetime.timedelta(days=int(period))       
            due_date = investment_date + period
            period = period.days
            
        elif due_date and period and not investment_date:
            due_date = datetime.datetime.strptime(due_date, date_format)
            period = datetime.timedelta(days=int(period))       
            investment_date = due_date - period
            period = period.days
            
        elif investment_date and due_date and period:
            investment_date = datetime.datetime.strptime(investment_date, date_format)
            period = datetime.timedelta(days=int(period))       
            due_date = investment_date + period
            period = period.days

        if hidden_val =="1":
            # interest_amount = (float(investment_amount)*float(rate)*float(period))/36500
            # maturity_amount = float(investment_amount)+float(interest_amount)
            try:
                if rate == "" :
                    
                    t = (float(investment_amount))*int(period)
                    rate = (float(interest_amount)*36500)/t
                else:
                    interest_amount1 = (float(investment_amount)*float(rate)*float(period))/36500
                    maturity_amount1 = float(investment_amount)+float(interest_amount1)
                    interest_amount = (float(maturity_amount1)*float(rate)*float(period))/36500
                    maturity_amount =  float(investment_amount) + float(interest_amount)
            except Exception as msg:
                print("error", msg)
            

        if hidden_val == "2":
            # investment_amount = (float(maturity_amount)*36500)/(float(rate)*float(period)+36500)
            # interest_amount = (float(investment_amount)*float(rate)*float(period))/36500
            try:
                    a = float(rate)**2*float(period)**2+36500*float(rate)*float(period)+36500**2
                    investment_amount = (float(maturity_amount)*36500*36500)/a
                    interest_amount = float(maturity_amount)-float(investment_amount)
            except Exception as msg:
                print(msg)
 
        context = {"investment_amount":investment_amount, "maturity_amount":maturity_amount, "interest_amount":interest_amount, "period":period, "rate":rate, "due_date":due_date, "investment_date":investment_date}

    elif request.method== "GET":
        maturity_amount = 0.0
        interest_amount = 0.0
        rate = 0.0
        period = 0.0

        context = {"maturity_amount":maturity_amount, "interest_amount":interest_amount}
    return render(request, 'base.html', context)

def calc1(request):
    if request.method == "POST":
        period = request.POST["period"]
        rate = request.POST["rate"]
        investment_amount = request.POST["investment_amount"]
        interest_amount1 = (float(investment_amount)*float(rate)*float(period))/36500
        maturity_amount1 = float(investment_amount)+float(interest_amount1)
        interest_amount = (float(maturity_amount1)*float(rate)*float(period))/36500
        maturity_amount =  float(investment_amount) + float(interest_amount) 
        context = {"investment_amount1":investment_amount, "maturity_amount1":maturity_amount, "interest_amount1":interest_amount, "period1":period, "rate1":rate}
    else:
        context = {}
    return render(request,'base.html', context )