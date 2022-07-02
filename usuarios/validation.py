from datetime import datetime
from validate_docbr import CPF


def senhas_diferentes(senha, senha2, lista_de_erros):
    """Verifica se a senha e confirmação de senha sao diferentes"""
    if senha != senha2:
        lista_de_erros['senha2'] = 'As Senhas estão diferentes'


def data_valida(data_nascimento, lista_de_erros):
    """Verifica se a data é válida"""
    data_atual = datetime.today().date()
    if data_nascimento > data_atual:
        lista_de_erros['data_nascimento'] = 'A data de nascimento não pode ser maior que a data de hoje'


def cpf_valido(cpf_recebido, lista_de_erros):
    cpf_base = CPF()
    if not cpf_base.validate(cpf_recebido):
        lista_de_erros['cpf'] = 'CPF inválido'
