import csv
import datetime

lista_de_cadastros = list()
#*todo: acessar tabela criada para editar?

#  def carregar arquivo para edição
'''with open('filename.csv') as csv_file:
    csv_read=csv.reader(csv_file, delimiter=',')

    
'''
#todo: concatenar dia + nome para criar arquivo csv


#criar nova tabela
def cadastrar_receita():
    cadastrando = True
    while cadastrando:
        cadastro = dict()
        cadastro['cpf'] = input(f'CPF do paciente: ')
        cadastro['nome'] = input(f'Nome do paciente: ')
        '''
        SIMPLIFICAR TESTE
        cadastro['nome_remedio'] = input(f'Nome do medicamento: ')
        cadastro['dose'] = input(f'Insira a dose do medicamento: ')
        cadastro['intervalo'] = input(f'Insira o intervalo de tempo para administração da medicação em horas: ')
        cadastro['data_inicio'] = input(f'Data de início do tratamento: ')
        cadastro['hora_inicio'] = input(f'Hora de início do tratamento: ')
        cadastro['tratamento_dias'] = input(f'Tempo do tratamento em dias')
        cadastro['descricao_tratamento'] = input(f'Descrição do tratamento: ')
        '''
        lista_de_cadastros.append(cadastro)
        salvar_arquivo()
        op = input(f'\nContinuar cadastrando? 1-SIM ou 0-NÃO: ')
        while op not in '01': 
            op = input(f'\nCódigo Inválido!Continuar cadastrando? 1-SIM ou 0-NÃO: ')
        if op == '1':
            cadastrando = True
        else:
            #* teste para ver se está cadastrando print(lista_de_cadastros)
            cadastrando = False

def salvar_arquivo():
    
    if len(lista_de_cadastros)==0:
        print(f'\nSem lista sem cadastros! Nada a salvar!')
    else:
        #todo: implementar csv
        headerLista = lista_de_cadastros[0].keys()
        with open('tabelaMedicamentos.csv', 'w', newline='') as arquivo:
            header_tabela = csv.DictWriter(arquivo, delimiter='|', fieldnames=headerLista)

            header_tabela.writeheader()

            line_content  = csv.writer(arquivo, delimiter='|')

            for receita in lista_de_cadastros:
                line_content.writerow(receita.values())


        
     

def mostrar_receita(lista_de_cadastros):
    #TODO:
    pass

def editar_receita(lista_de_cadastros, opcao):
    #TODO: perguntar qual receita quer atualizar, se quer editar algo a mais na mesma receita e volta para menu principal
    pass

def excluir_receita():
    #TODO:
    pass

def relatorio_progresso():
    #TODO: Barra de progresso em porcentagem e mostrar quantos dias faltam para terminar tratamento - manipular datas
    pass

def relatorio_historico_paciente():
    #TODO: Pelo identificador do paciente -  ver todas as datas - nome de medicamentos - doses - tratamento finalizado ou não
    pass

def relatorio_anotacoes_medicamento():
    #todo:
    pass

#todo: mais um relatório

# * testes

#lista_de_cadastros = list()

#lista_de_cadastros.append(cadastrar_receita())
#print(lista_de_cadastros)

#print(lista_de_cadastros[0]['cpf'])
