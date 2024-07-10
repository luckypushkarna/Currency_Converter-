# myapp/forms.py
from django import forms

class CurrencyConverterForm(forms.Form):
    amount = forms.FloatField(label='Amount')
    from_currency = forms.ChoiceField(choices=[('USD', 'USD'), ('EUR', 'EUR'), ('GBP', 'GBP'), ('JPY', 'JPY')], label='From')
    to_currency = forms.ChoiceField(choices=[('USD', 'USD'), ('EUR', 'EUR'), ('GBP', 'GBP'), ('JPY', 'JPY')], label='To')
