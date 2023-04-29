from lib.interface import *
from lib.arquivo import *
from time import sleep


arq = 'Projeto Final.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if resposta == 1:
        #Opção de listar o conteúdo de um arquivo
        lerArqvuivo(arq)
    elif resposta == 2:
        #Cadastrar uma nova pessoa
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçalho('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
    sleep(2)
