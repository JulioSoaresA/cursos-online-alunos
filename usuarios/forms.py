from django import forms
from usuarios.validation import *


class Autocadastro(forms.Form):
    choices = {
        (1, 'Não'),
        (2, 'Sim')
    }

    nome_completo = forms.CharField(label='Nome completo', max_length=200, required=True,
                                    widget=forms.TextInput(attrs={
                                        'class': 'form-control',
                                        'placeholder': 'Seu nome'
                                    }))
    cpf = forms.CharField(label='CPF (Insira apenas números)', max_length=11, required=True,
                          widget=forms.TextInput(attrs={
                                        'class': 'form-control',
                                        'placeholder': 'xxxxxxxxxxx'
                                    }))
    data_nascimento = forms.DateField(label='Data de nascimento', required=True,
                                      widget=forms.DateInput(attrs={
                                          'class': 'form-control',
                                          'type': 'date'
                                      }))
    senha = forms.CharField(label='Senha', max_length=100, required=True,
                            widget=forms.TextInput(attrs={
                                'class': 'form-control',
                                'type': 'password'
                            }))
    senha2 = forms.CharField(label='Confirmar senha', max_length=100, required=True,
                             widget=forms.TextInput(attrs={
                                'class': 'form-control',
                                'type': 'password'
                             }))

    indica_privacidade = forms.ChoiceField(label='Indicador de privacidade', choices=choices)

    def clean(self):
        cpf = self.cleaned_data.get('cpf')
        data_nascimento = self.cleaned_data.get('data_nascimento')
        senha = self.cleaned_data.get('senha')
        senha2 = self.cleaned_data.get('senha2')
        lista_de_erros = {}
        cpf_valido(cpf, lista_de_erros)
        data_valida(data_nascimento, lista_de_erros)
        senhas_diferentes(senha, senha2, lista_de_erros)

        if lista_de_erros is not None:
            for erro in lista_de_erros:
                mensagem_erro = lista_de_erros[erro]
                self.add_error(erro, mensagem_erro)
        return self.cleaned_data
