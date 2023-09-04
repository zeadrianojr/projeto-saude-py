from funcoes import *

def main():
  display_menu = True
  while display_menu:
    print(f'\n:::Receituário:::')
    print(f'\n---MENU INICIAL---')
    menu()
    op = input(f'\nEscolha: ')
    if op not in '12345678':
      print(f'\nPROGRAMA FINALIZAD0!') 
      salvar_arquivo()
      display_menu = False   
    else:
      if op == '1':
        cadastro_paciente()
      if op == '2':
        cadastro_receita() 
      if op == '3':
        mostra_entidades()
      if op == '4':
        tipo_edicao = escolha_op()
        if tipo_edicao == 'paciente':
          editar_paciente()
        else:
          editar_receita()
      if op == '5':
        tipo_edicao = escolha_op()
        if tipo_edicao == 'paciente':
          print(f'ATENÇÃO ESSA OPÇÃO APAGA TODOS OS DADOS DO PACIENTE')
          excluir_paciente()
        else:
          print(f'ATENÇÃO ESSA OPÇÃO APAGA APENAS A RECEITA DESEJADA')
          excluir_receita()
      if op == '6':
        relatorio_cpf_nome()
      if op == '7':
        informativo_termino()
      if op == '8':
        relatorio_anotacoes_medicamento()

main()
