import os
import random

def criar_e_validar_digito(cpf, multiplicador, seg_multiplicador=0):
    if len(cpf) == 9 or len(cpf) == 10:
        total = 0
        for num in cpf:
            total += int(num) * multiplicador
            multiplicador -= 1

        digito = (total * 10) % 11
        if digito <= 9:
            cpf += str(digito)
        else:
            cpf += '0'
        return cpf
    
    else:
        total = 0
        for num in cpf[:9]:
            total += int(num) * multiplicador
            multiplicador -= 1

        digito = (total * 10) % 11
        if digito >= 10:
            digito = 0

        if str(digito) == cpf[9]:
            total = 0
            for num in cpf[:10]:
                total += int(num) * seg_multiplicador
                seg_multiplicador -= 1
            
            digito_2 = (total * 10) % 11

            if digito_2 >= 10:
                digito_2 = 0

            if str(digito_2) == cpf[10]:
                return f'O CPF: "{cpf}" é válido!\n'
            
            else:
                return f'O CPF: "{cpf}" é inválido\n'
        
        else:
                return f'O CPF: "{cpf}" é inválido\n'

os.system('cls')

while True:

    print('***Gerador e Validador de CPF***')
    print('[G] - Gerar um CPF\n[V] - Verificar se um CPF é válido\n[S] - Sair')
    opcao = input('O que você deseja fazer? ').lower()
    
    if opcao == 'g':

        cpf = [str(random.randint(0,9)) for i in range(9)]
        cpf_unido = ''.join(cpf)
        
        cpf_com_primeiro_digito = criar_e_validar_digito(cpf_unido, 10)

        cpf_pronto = criar_e_validar_digito(cpf_com_primeiro_digito, 11)

        print(f'O CPF é: {cpf_pronto[:3]}.{cpf_pronto[3:6]}.{cpf_pronto[6:9]}-{cpf_pronto[9:]}')
        
        if cpf_pronto[8] == '8':
            print('Esse CPF é de SP!\n')
        
        while True:
            print('[S] - Sim\n[N] - Não')
            resposta = input("Você deseja validar o seu cpf gerado? ").lower()

            if resposta == 's':
                cpf_validado_2 = criar_e_validar_digito(cpf_pronto, 10, 11)
                break

            elif resposta == 'n':
                print('Ok!\n\n')
                break

            else:
                print('Digite uma resposta válida!\n')

    elif opcao == 'v':

        cpf_enviado = input('Digite seu CPF: ')
        cpf_corrigido = cpf_enviado.replace('.','').replace('-','')

        if len(cpf_corrigido) == 11:
            if cpf_corrigido.isdigit():
                cpf_com_numeros_iguais = ''
                for i in cpf_corrigido:
                    cpf_com_numeros_iguais += cpf_corrigido[0]

                if cpf_com_numeros_iguais != cpf_corrigido:

                    cpf_validado = criar_e_validar_digito(cpf_corrigido, 10, 11)
                    print(cpf_validado)
                    
                    if 'inválido' not in cpf_validado:
                        if cpf_corrigido[8] == '8':
                            print('E esse CPF é de SP!\n')

                else:
                    print("Você digitou um CPF inválido.\n")
                                 
            else:
                print('Você não digitou apenas números.\n')
        
        else:
            print("Digite um CPF válido.\n")
        
    if opcao == 's':
        os.system('cls')
        print('Você saiu!')
        break