from django import forms
from tempus_dominus.widgets import DatePicker


class Autocadastro(forms.Form):
    nome_completo = forms.CharField(label='Nome completo', max_length=200)
    cpf = forms.CharField(label='CPF', max_length=11)
    data_nascimento = forms.DateField(label='Data de nascimento', widget=DatePicker())
    senha = forms.CharField(label='Senha', max_length=100)
    senha2 = forms.CharField(label='Confirmar senha', max_length=100)
