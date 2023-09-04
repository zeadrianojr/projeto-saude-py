# Relatório do Sistema de Gerenciamento de Pacientes e Receitas

Este script em Python é um simples Sistema de Gerenciamento de Pacientes e Receitas que permite aos usuários gerenciar registros de pacientes e as suas prescrições médicas. Ele fornece várias funções para adicionar pacientes, adicionar prescrições, editar detalhes de pacientes e etc.

## Sumário

- [Visão Geral](#visão-geral)
- [Primeiros Passos](#primeiros-passos)
- [Principais Funções](#principais-funções)
- [Exemplos de Uso](#exemplos-de-uso)
- [Salvando Dados](#salvando-dados)
- [Licença](#licença)

## Visão Geral

Esta é uma aplicação de linha de comando para gerenciar registros de pacientes. Ele oferece as seguintes funcionalidades principais:

- Adicionar e gerenciar informações de pacientes.
- Adicionar e gerenciar detalhes de prescrições para pacientes.
- Editar informações de pacientes e prescrições.
- Excluir registros de pacientes e prescrições.
- Exibir uma lista de pacientes com seus nomes e CPFs.
- Calcular a data e hora de término de um tratamento com prescrição.
- Ler a descrição do tratamento de um paciente.

## Primeiros Passos

1. **Instalação**: Não é necessária nenhuma instalação. Você pode executar o script usando qualquer interpretador Python que suporte Python 3.x.

2. **Executando o Script**: Para executar o script, basta executar o arquivo Python em seu ambiente de desenvolvimento preferido ou na linha de comando.

## Principais Funções

### 1. Cadastrar Paciente (`cadastro_paciente`)

Esta função permite adicionar um novo paciente ao sistema. Ela coleta os seguintes detalhes do paciente:
- CPF;
- Nome;
- Endereço;
- Número de telefone;

### 2. Cadastrar Receita (`cadastro_receita`)

Esta função permite adicionar uma prescrição para um paciente. Ela coleta os seguintes detalhes da prescrição:
- Nome do medicamento;
- Fabricante;
- Dose;
- Data e hora de início;
- Duração do tratamento (em dias);
- Descrição do tratamento;

### 3. Mostrar Todas as Entidades (`mostra_entidades`)

Exibe todos os registros de pacientes juntamente com os detalhes das prescrições.

### 4. Editar Dados do Paciente (`editar_paciente`)

Permite editar os detalhes de um paciente existente, fornecendo o CPF do paciente.

### 5. Excluir (`excluir_paciente`, `excluir_receita`)

Permite a remoção de registros de pacientes e detalhes de prescrições, fornecendo o CPF do paciente e o nome da prescrição.

### 6. Listagem dos CPFs e Nomes dos Pacientes (`relatorio_cpf_nome`)

Exibe uma lista de CPFs e nomes de pacientes.

### 7. Informativo de Data e Hora do Término de Tratamento (`informativo_termino`)

Calcula e exibe a data e hora de término de um tratamento com prescrição com base na data de início e na duração do tratamento.

### 8. Ler Descrição do Tratamento do Paciente (`relatorio_anotacoes_medicamento`)

Lê e exibe a descrição do tratamento de um paciente para um medicamento específico.

## Exemplos de Uso

Aqui estão alguns exemplos de uso do Sistema de Gerenciamento de Pacientes:

- Adicionar um novo paciente e sua prescrição.
- Editar detalhes de pacientes.
- Excluir registros de pacientes e prescrições.
- Gerar um relatório com nomes e CPFs de pacientes.
- Calcular a data e hora de término de um tratamento com prescrição.
- Ler a descrição do tratamento de um paciente.

## Salvando Dados

O script oferece a opção de salvar os dados dos pacientes em um arquivo CSV. Ele solicita ao usuário um nome de arquivo, os registros dos pacientes são salvos e o programa é finalizadp.

## Licença

Este script é fornecido sob a [Licença MIT](LICENSE.md). Você tem liberdade para usá-lo e modificá-lo para seus fins, mas consulte o arquivo de licença para obter mais detalhes sobre o uso e a distribuição.

---

