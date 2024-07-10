# from django.shortcuts import render

# # Create your views here.
# def index(request):
#     template = 'index.html'
#     return render(request,template)

#new

# myapp/views.py
import requests
from django.shortcuts import render
from .forms import CurrencyConverterForm

def convert_currency(amount, from_currency, to_currency):
    api_url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
    response = requests.get(api_url)
    data = response.json()
    rate = data['rates'][to_currency]
    return amount * rate

def currency_converter_view(request):
    converted_amount = None
    if request.method == 'POST':
        form = CurrencyConverterForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            from_currency = form.cleaned_data['from_currency']
            to_currency = form.cleaned_data['to_currency']
            converted_amount = convert_currency(amount, from_currency, to_currency)
    else:
        form = CurrencyConverterForm()

    return render(request, 'myapp/currency_converter.html', {
        'form': form,
        'converted_amount': converted_amount,
    })

