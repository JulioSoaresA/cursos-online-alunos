from django import forms
from usuarios.models import Usuarios
from usuarios.validation import *


class Autocadastro(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields = '__all__'
        exclude = ('username', 'email', 'is_admin', 'is_staff', 'is_active', 'is_superuser')
        labels = {'nome_completo': 'Nome completo',
                  'cpf': 'CPF (Insira apenas números)',
                  'data_nascimento': 'Data de nascimento',
                  'password': 'Senha',
                  'password2': 'Confirmar senha'}
        widgets = {
            'nome_completo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite o seu nome'}),
            'cpf': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'xxxxxxxxxxx'}),
            'data_nascimento': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'}),
            'password': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'password'}),
            'password2': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'password'
            })
        }

    field_order = ['nome_completo', 'cpf', 'data_nascimento', 'indica_privacidade', 'password', 'password2']

    def clean(self):
        cpf = self.cleaned_data.get('cpf')
        data_nascimento = self.cleaned_data.get('data_nascimento')
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        lista_de_erros = {}
        cpf_valido(cpf, lista_de_erros)
        cpf_existente(cpf, lista_de_erros)
        data_valida(data_nascimento, lista_de_erros)
        senhas_diferentes(password, password2, lista_de_erros)

        if lista_de_erros is not None:
            for erro in lista_de_erros:
                mensagem_erro = lista_de_erros[erro]
                self.add_error(erro, mensagem_erro)
        return self.cleaned_data
