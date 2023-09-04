import csv
from datetime import datetime, timedelta

lista_pacientes = list()

def salvar_arquivo():
    if len(lista_pacientes) == 0:
        print(f'\nSem lista sem cadastros! Nada a salvar!')
    else:
        headerLista = ['cpf','hora_cad','paciente_nome','endereco','telefone','receitas_paciente']
        arquivoCSV = input(f'Insira no nome do arquivo CSV: ')
        arquivoCSV = arquivoCSV+'.csv'
        with open(arquivoCSV, 'w', newline='') as arquivo:
            header_tabela = csv.DictWriter(arquivo, delimiter='|', fieldnames=headerLista)

            header_tabela.writeheader()

            conteudo_linha  = csv.writer(arquivo, delimiter='|')

            for paciente in lista_pacientes:
                conteudo_linha.writerow(paciente.values())

def menu(): 
    print(f'1 - Cadastrar paciente')
    print(f'2 - Cadastrar receita')
    print(f'3 - Mostrar todas as entidades') 
    print(f'4 - Editar dados do paciente')
    print(f'5 - Excluir')
    print(f'6 - Listagem dos cpfs e nomes dos pacientes')
    print(f'7 - Informativo de dia e hora do término de tratamento')
    print(f'8 - Ler descrição do tratamento do paciente')
    print(f'Digite qualquer outra tecla Salvar arquivo e sair')

def verificar_existencia(cpf):
    for dicio_paciente in lista_pacientes:
        if dicio_paciente['cpf'] == cpf:
            return True
        else:
            return False
    
def cadastro_paciente():
    cpf = input('Digite o cpf: ')
    if verificar_existencia(cpf):
        print(f'Paciente já existe!')
    else:
        print('Cadastrando novo paciente:')
        dicioPaciente = dados_paciente(cpf)
        lista_pacientes.append(dicioPaciente)
        
def dados_paciente(cpf):
        paciente = dict()
        paciente['cpf'] = cpf
        paciente['hora_cad'] = datetime.now()
        paciente['paciente_nome']= input(f'Nome do paciente: ').lower()
        paciente['endereco'] = input(f'Endereço do paciente: ').lower()
        paciente['telefone'] = input(f'Telefone do paciente: ')
        paciente['receitas_paciente'] = list()
        return paciente

def cadastro_receita():
    cpf_receita = input(f'Digite po CPF do paciente para cadastrar receita:')
    if not verificar_existencia(cpf_receita):
        print(f'CPF não cadastrado! FAÇA O CADASTRO ANTES')
    else:
        dicioReceita = dados_receita()
        for paciente in lista_pacientes:
            if paciente['cpf'] == cpf_receita:
                paciente['receitas_paciente'].append(dicioReceita)

def dados_receita():
    cad_remedio = dict()
    cad_remedio['nome_remedio'] = input(f'Nome do medicamento: ').lower()
    cad_remedio['hora_cad'] = datetime.now() 
    cad_remedio['fabricante'] = input('Fabricante: ').lower()
    cad_remedio['dose'] = input(f'Insira a dose do medicamento: ').lower()
    cad_remedio['data_inicio']  = input('Digite a data de início do tratamento (AAAA-MM-DD): ')
    cad_remedio['hora_inicio'] = input('Digite a hora de início do tratamento (HH:MM): ')
    cad_remedio['tratamento_dias'] = input(f'Tempo do tratamento em dias - número: ')
    cad_remedio['descricao_tratamento'] = input(f'Descrição do tratamento: ').lower()
    return cad_remedio

def mostra_entidades():
    contador = 0
    print(f'Todas as entidades cadastradas: ')
    for linha in lista_pacientes: 
        print(linha.items())
        print()
        contador +=1
    print(f'Número de cadastros: {contador}')

def editar_paciente():
    cpf = input(f'Digite nº do CPF do paciente para editar:')
    for paciente in lista_pacientes:
        if paciente['cpf'] == cpf:
            paciente['cpf'] = input(f'CPF do paciente: ')
            paciente['hora_cad'] = datetime.now()
            paciente['paciente_nome']= input(f'Nome do paciente: ').lower()
            paciente['endereco'] = input(f'Endereço do paciente: ').lower()
            paciente['telefone'] = input(f'Telefone do paciente: ')
        else:
            print(f'CPF não encontrado!')

def editar_receita():            
    cpf = input(f'Digite nº do CPF do paciente para editar: ')
    nomeRed = input(f'Insira o nome do medicação que quer alterar: ').lower()
    for paciente in lista_pacientes:
        if paciente['cpf'] == cpf:
            for item in paciente['receitas_paciente']:
                if item['nome_remedio'] == nomeRed:
                    item['nome_remedio'] = input(f'Nome do medicamento: ').lower()
                    item['hora_cad'] = datetime.now() 
                    item['fabricante'] = input('Fabricante: ').lower()
                    item['dose'] = input(f'Insira a dose do medicamento: ').lower()
                    item['data_inicio']  = input('Digite a data de início do tratamento (AAAA-MM-DD): ')
                    item['hora_inicio'] = input('Digite a hora de início do tratamento (HH:MM): ')
                    item['tratamento_dias'] = input(f'Tempo do tratamento em dias - número: ')
                    item['descricao_tratamento'] = input(f'Descrição do tratamento: ').lower()
                else:
                    print(f'Medicamento não encontrado!')
        else:
            print(f'CPF não encontrado!')

def escolha_op():
    display_menu = True
    while display_menu:
        print(f'1 - Paciente')
        print(f'2 - Receita')
        op = input(f'Escolha: ')
        if op not in '12':
            display_menu = True
        else:
            if op == '1':
                return 'paciente'
            if op == '2':
                return 'receita'

def excluir_paciente():
    cpf = input(f'Digite nº do CPF do paciente para excluir:')
    for paciente in lista_pacientes:
        if paciente['cpf'] == cpf:
            lista_pacientes.remove(paciente)

def excluir_receita():
    cpf = input(f'Digite nº do CPF do paciente para excluir: ')
    nomeMed = input(f'Insira o nome do medicamento da receita: ')
    for paciente in lista_pacientes:
        if paciente['cpf'] == cpf:
            for item in paciente['receitas_paciente']:
                if item['nome_remedio'] == nomeMed:
                    paciente['receitas_paciente'].remove(item)

def relatorio_cpf_nome():
    if len(lista_pacientes)==0:
        print(f'AINDA VAZIO! NADA A LISTAR!')
    else:
        print(f'CPF - NOME')
        for i in range(len(lista_pacientes)):
            print(f"{lista_pacientes[i]['cpf']} - {lista_pacientes[i]['paciente_nome']}")

def informativo_termino():
    cpf = input(f'Digite nº do CPF do paciente: ')
    nomeMed = input(f'Insira o nome do medicamento da receita: ')
    for paciente in lista_pacientes:
        if paciente['cpf'] == cpf:
            for item in paciente['receitas_paciente']:
                if item['nome_remedio'] == nomeMed:
                    data_inicial = item['data_inicio']
                    data_inicial=datetime.strptime(data_inicial, "%Y-%m-%d")
                    duracao = item['tratamento_dias']
                    duracao = int(duracao)
                    data_final = data_inicial + timedelta(days=duracao - 1)
                    print(f'Data final do tratamento: {data_final}')

def relatorio_anotacoes_medicamento():
    cpf = input(f'Digite nº do CPF do paciente: ')
    nomeMed = input(f'Insira o nome do medicamento da receita: ')
    for paciente in lista_pacientes:
        if paciente['cpf'] == cpf:
            for item in paciente['receitas_paciente']:
                if item['nome_remedio'] == nomeMed:
                    print(f"{item['nome_remedio']} - {item['descricao_tratamento']}")