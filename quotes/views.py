from django.shortcuts import render, redirect, get_object_or_404
from .forms import StockForm
from .models import *
from django.contrib import messages



def home(request):
    import requests
    import json

    if request.method == 'POST':
        ticker = request.POST['ticker']
        # print(request.POST['ticker'])
        api_request = requests.get(
            "https://sandbox.iexapis.com/stable/stock/" + ticker + "/quote?token=Tpk_536d927f9fb04ab49f80ca8e845caedb")
        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error..."
        return render(request, 'home.html', {'api': api})
    else:
        return render(request, 'home.html', {'ticker': "Enter a ticker symbol above..."})


def about(request):
    context = {}
    return render(request, 'about.html', context)


def add_stock(request):
    import requests
    import json
    if request.method == "POST":
        form = StockForm(request.POST or None)

        if form.is_valid():
            form.save()
            messages.success(request, f" Stock has been Added")
            return redirect("add_stock")
    else:
        ticker = Stock.objects.all()
        output = []
        for ticker_item in ticker:
            api_request = requests.get(
                "https://sandbox.iexapis.com/stable/stock/" + str(ticker_item) + "/quote?token=Tpk_536d927f9fb04ab49f80ca8e845caedb")
            try:
                api = json.loads(api_request.content)
                output.append(api)
            except Exception as e:
                api = "Error..."
        return render(request, 'add_stock.html', {'ticker': ticker, 'output': output})


def delete(request, stock_id):
    item = Stock.objects.get(pk=stock_id)
    item.delete()
    messages.success(request, f"Stock {item} has been Deleted")
    return redirect(add_stock)


def delete_stock(request):
    import requests
    import json
    if request.method == "POST":
        form = StockForm(request.POST or None)

        if form.is_valid():
            form.save()
            messages.success(request, f" Stock has been Added")
            return redirect("add_stock")
    else:
        ticker = Stock.objects.all()
        output = []
        for ticker_item in ticker:
            api_request = requests.get(
                "https://sandbox.iexapis.com/stable/stock/" + str(
                    ticker_item) + "/quote?token=Tpk_536d927f9fb04ab49f80ca8e845caedb")
            try:
                api = json.loads(api_request.content)
                output.append(api)
            except Exception as e:
                api = "Error..."
        return render(request, 'delete_stock.html', {'ticker': ticker, 'output': output})