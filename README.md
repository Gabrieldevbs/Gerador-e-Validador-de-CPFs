Este repositório apresenta um Gerador e Validador de CPF em Python. O programa permite ao usuário gerar um CPF válido aleatoriamente ou validar um CPF fornecido manualmente.

✅ Funcionalidades Gerar um CPF válido aleatoriamente Validar um CPF informado pelo usuário Verificar se um CPF gerado pertence ao estado de SP Interface interativa no terminal

📁 Estrutura do Código O programa está dividido nas seguintes partes:

Importação de Bibliotecas
import random import os

random: Usado para gerar números aleatórios na criação do CPF. os: Utilizado para limpar o terminal durante a execução.

Função criar_e_validar_digito
def criar_e_validar_digito(cpf, multiplicador, seg_multiplicador=0):

Esta função é responsável por calcular e validar os dígitos verificadores do CPF.

🔄 Cálculo dos Dígitos Verificadores

Para o primeiro dígito, multiplica-se os 9 primeiros números por pesos de 10 a 2, soma-se os valores e obtém-se o resto da divisão por 11. Se o resultado for maior que 9, o dígito é 0. Para o segundo dígito, repete-se o processo, mas agora usando os 10 primeiros números e pesos de 11 a 2. Se os dígitos calculados forem diferentes dos informados, o CPF é inválido.

Geração de CPF Aleatório
cpf = [str(random.randint(0, 9)) for i in range(9)] cpf_unido = "".join(cpf)

Cria uma lista de 9 dígitos aleatórios. Junta os dígitos em uma string. Calcula os dois dígitos verificadores com a função criar_e_validar_digito. O CPF gerado é formatado e validado.

Validação de CPF Informado pelo Usuário
cpf_enviado = input("Digite seu CPF: ") cpf_corrigido = cpf_enviado.replace(".", "").replace("-", "")

O usuário digita um CPF. Remove pontos e traços para garantir que esteja no formato correto. Verifica se é um CPF válido utilizando a função criar_e_validar_digito. Se for válido, o programa exibe "CPF válido!", senão, solicita um novo CPF.

Identificação do Estado de Origem
if cpf_pronto[8] == '8': print("Esse CPF é de SP!")

O nono dígito do CPF indica o estado de origem. Se for 8, o CPF pertence a São Paulo.

🔧 Como Usar

Execução do Programa

Clone o repositório: git clone https://github.com/seuusuario/gerador-validador-cpf.git Acesse a pasta do projeto: cd gerador-validador-cpf Execute o script: python cpf.py Escolha uma Opção

1 - Gerar um CPF válido

2 - Validar um CPF fornecido

0 - Sair do programa

📈 Exemplo de Saída

Geração de CPF:

CPF gerado: 123.456.789-09 Esse CPF é de SP!

Validação de CPF:

Digite seu CPF: 123.456.789-09 CPF válido!
