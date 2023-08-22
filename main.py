from funcoes import *
from time import sleep



def main():
  display_menu = True
  while display_menu:
    print(f'\n:::Gerenciador de Medicação:::')
    print(f'\n---MENU PRINCIPAL---')
    print(f'''
1 - Salvar Arquivo
2 - Cadastrar receita
          ''')
    op = input(f'\nEscolha dos números da opções acima ou insira qualquer tecla para finalizar o programa: ')
    if op not in '12':
      print(f'\nSALVAMENTO AUTOMÁTICO DE SAÍDA...')
      salvar_arquivo()
      sleep(3)
      print(f'\nPROGRAMA FINALIZAD0!')
      display_menu = False
    else:
      if op == '1':
        salvar_arquivo()
        pass
      elif op == '2':
        cadastrar_receita()

  
  #todo: estrutura de menu




main()
