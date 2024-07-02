from _init_ import *
import os
import sys
from time import sleep

#Começo do loop MENU
while True:
    print("\n" * os.get_terminal_size().lines)
    cabeçalho('\033[1;36m        SMARTGYM APP\033[m') #Cabeçalho
    print('\033[36mMENU PRINCIPAL\033[m') #Titulo do menu
    resposta = menu(['Aluno','Professor','Treino','Mensalidade','Matriculas','Presenças','Sair'])

 #Menu Aluno   
    if resposta == 1:
        print("\n" * os.get_terminal_size().lines)
        cabeçalho('\033[1;36m        SMARTGYM APP\033[m') 
        print('\033[36mMENU ALUNO\033[m')
        resposta2 = menu(['Cadastrar Aluno','Atualizar Informações Aluno','Consultar Alunos','Acompanhamento Aluno','Plano(os) relacionado(os) ao Aluno','Treino','Sair'])

#Cadastro de aluno
        if resposta2 == 1:
            print("\n" * os.get_terminal_size().lines)
            cabeçalho('\033[1;36m        SMARTGYM APP\033[m') 
            cabeçalho('\033[36m         Cadastro Aluno\033[m')
            criar_aluno()
            

#Menu atualizar aluno
        elif resposta2 == 2:
            print("\n" * os.get_terminal_size().lines)
            cabeçalho('\033[1;36m        SMARTGYM APP\033[m') 
            cabeçalho('\033[36m         Atualizar Aluno\033[m')
            rsptatualiza = menu(['Atualizar por CPF','Atualizar por Codigo Aluno'])
            if rsptatualiza == 1:
#Começo atualiza por CPF
                print("\n" * os.get_terminal_size().lines)
                cabeçalho('\033[1;36m        SMARTGYM APP\033[m') 
                cabeçalho('\033[36m         Atualizar Aluno\033[m')
                print('\n Valores disponiveis:\n')
                respostaatualiza = menu(['Contato','CEP','Endereco','Numero Endereco'])
                if respostaatualiza == 1:                   
                    novovalor_aluno = "contato_aluno"
                    atualiza_aluno_cpf(novovalor_aluno)

                elif respostaatualiza == 2: 
                    novovalor_aluno = "cep_aluno"
                    atualiza_aluno_cpf(novovalor_aluno)

                elif respostaatualiza == 3: 
                    novovalor_aluno = "endereco_aluno"
                    atualiza_aluno_cpf(novovalor_aluno)
                    
                elif respostaatualiza == 4: 
                    novovalor_aluno = "endereco_nmr_aluno"
                    atualiza_aluno_cpf(novovalor_aluno)
                    
                else:
                    cabeçalho
                    print('\n')
                    cabeçalho('Opcao invalida')

#Começo atualiza por cod                        
            elif rsptatualiza == 2:
                print("\n" * os.get_terminal_size().lines)
                cabeçalho('\033[1;36m        SMARTGYM APP\033[m') 
                cabeçalho('\033[36m         Atualizar Aluno\033[m')
                print('\n Valores disponiveis:\n')
                respostaatualiza = menu(['Contato','CEP','Endereco','Numero Endereco'])
                if respostaatualiza == 1:                   
                    novovalor_aluno = "contato_aluno"
                    atualiza_aluno(novovalor_aluno)

                elif respostaatualiza == 2: 
                    novovalor_aluno = "cep_aluno"
                    atualiza_aluno(novovalor_aluno)

                elif respostaatualiza == 3: 
                    novovalor_aluno = "endereco_aluno"
                    atualiza_aluno(novovalor_aluno)
                    
                elif respostaatualiza == 4: 
                    novovalor_aluno = "endereco_nmr_aluno"
                    atualiza_aluno(novovalor_aluno)
                    
                else:
                    cabeçalho
                    print('\n')
                    cabeçalho('Opcao invalida')
            
            else:
                print('\n')
                cabeçalho('Opcao invalida')
            sleep(3)
            
#Começo Menu consultar aluno        
        elif resposta2 == 3:
            print("\n" * os.get_terminal_size().lines)
            cabeçalho('\033[1;36m        SMARTGYM APP\033[m') 
            cabeçalho('\033[36m         Consultar Alunos\033[m')
            print('\033[36mOpcoes disponiveis:\n\033[m')
            opcconsulta_aluno = menu(['Consulta todos o alunos','Consulta por CPF','Consulta por codigo','Sair'])
            if opcconsulta_aluno == 1:
                exibe_aluno()

            elif opcconsulta_aluno == 2:
                exibe_aluno_cpf()
            
            elif opcconsulta_aluno == 3:
                exibe_aluno_cod()

            sleep(3)

        
#Fim Consulta Aluno

        elif resposta2 == 4:
            print("\n" * os.get_terminal_size().lines)
            cabeçalho('\033[1;36m        SMARTGYM APP\033[m')
            cabeçalho('\033[36m         Acompanhamento Aluno\033[m')
            respostaacomp = menu(['Registrar ','Consultar','Atualizar','Sair'])
            if respostaacomp == 1:
                cabeçalho('\033[1;36m        SMARTGYM APP\033[m')
                cabeçalho('\033[36m         Registrar Acompanhamento Aluno\033[m')
#Começo registra Acompanhamento Aluno
                gera_acompanhamento()
            elif respostaacomp == 2:
                print("\n" * os.get_terminal_size().lines)
                cabeçalho('\033[1;36m        SMARTGYM APP\033[m')
                cabeçalho('\033[36m         Consultar Acompanhamentos Alunos\033[m')
#Começo Consulta Acompanhamento Aluno
                respostaacompaluno = menu(['Consultar todos acompanhamentos','Consultar acompanhamentos por aluno','Consultar acompanhamento por professor','Sair'])
                if respostaacompaluno == 1:
                    exibe_acompanhamento()
                    
                elif respostaacompaluno == 2:
                    exibe_acompanhamento_aluno()

                elif respostaacompaluno == 3:
                    exibe_acompanhamento_prof()

                elif respostaacompaluno == 4:
                    False
                else:
                    cabeçalho('Opcao invalida')
                    sleep(3)
                continuar = int(input('\nDigite [1] se deseja continuar no sistema ou [2] para sair: '))
                if continuar == 1:
                     False 
                else:
                     quit()

            elif respostaacomp == 3:
                print("\n" * os.get_terminal_size().lines)
                cabeçalho('\033[1;36m        SMARTGYM APP\033[m')
                cabeçalho('\033[36m         Atualizar Acompanhamentos Alunos\033[m')
#Começo atualiza Acompanhamento Aluno
                print('\n Valores disponiveis *inserir apenas numeros:\n')
                respostaatualiza = menu(['Peso','Altura','Massa Magra','Percentual gordura','Braco','Antebraco','Peito','Quadris','Cintura','Panturrilha','Sair'])
                if respostaatualiza == 1:                    
                    novovalor_acomp = "peso"
                    atualiza_acomp(novovalor_acomp)

                elif respostaatualiza == 2: 
                    novovalor_acomp = "altura"
                    atualiza_acomp(novovalor_acomp)
                    

                elif respostaatualiza == 3: 
                    novovalor_acomp = "massamagra"
                    atualiza_acomp(novovalor_acomp)
                    
                elif respostaatualiza == 4: 
                    novovalor_acomp = "perc_gordura"
                    atualiza_acomp(novovalor_acomp)
                    
                elif respostaatualiza == 5: 
                    novovalor_acomp = "med_braco"
                    atualiza_acomp(novovalor_acomp)
                    
                elif respostaatualiza == 6: 
                    novovalor_acomp = "med_ante"
                    atualiza_acomp(novovalor_acomp)

                elif respostaatualiza == 7: 
                    novovalor_acomp = "med_peito"
                    atualiza_acomp(novovalor_acomp)

                elif respostaatualiza == 8: 
                    novovalor_acomp = "med_quadris"
                    atualiza_acomp(novovalor_acomp)

                elif respostaatualiza == 9: 
                    novovalor_acomp = "med_cintura"
                    atualiza_acomp(novovalor_acomp)

                elif respostaatualiza == 10: 
                    novovalor_acomp = "med_panturrilha"
                    atualiza_acomp(novovalor_acomp)
            else:
                cabeçalho('Opcao invalida')
            sleep(2)

        elif resposta2 == 5:
            print("\n" * os.get_terminal_size().lines)
            cabeçalho('\033[1;36m        SMARTGYM APP\033[m')
            cabeçalho('\033[36m         Plano(os) relacionado(os) ao Aluno\033[m')
            exibe_plano_aluno()
        #Menu Treino

    elif resposta == 3:
        print("\n" * os.get_terminal_size().lines)
        cabeçalho('\033[36mMENU TREINO\033[m')
        resposta4 = menu(['Cadastrar Treino','Atualizar Treino','Consultar Treinos','Sair'])
        if resposta4 == 1:
            print("\n" * os.get_terminal_size().lines)
            cabeçalho('\033[1;36m        SMARTGYM APP\033[m') 
            cabeçalho('\033[36m         Cadastro Treino\033[m')
            criar_treino()

        elif resposta4 == 2:
                print("\n" * os.get_terminal_size().lines)
                cabeçalho('\033[1;36m        SMARTGYM APP\033[m') 
                cabeçalho('\033[36m         Atualizar Treino \033[m')
#Começo do Atualiza Treino
                respostaatualiza = menu(['Serie','Intervalo','Repeticao','Data Inicio','Data Fim','Status','Professor','Objetivo/Descricao','Tempo estimado'])
                if respostaatualiza == 1:                    
                    novovalor_treino = "serie_treino"
                    atualiza_treino(novovalor_treino)  

                elif respostaatualiza == 2: 
                    novovalor_treino = "intervalo_treino"
                    atualiza_treino(novovalor_treino)

                elif respostaatualiza == 3: 
                    novovalor_treino = "repeticao_treino"
                    atualiza_treino(novovalor_treino)
                    
                elif respostaatualiza == 4: 
                    novovalor_treino = "repeticao_treino"
                    atualiza_treino(novovalor_treino)
                    
                elif respostaatualiza == 5: 
                    novovalor_treino = "dtinicio_treino"
                    atualiza_treino(novovalor_treino)

                elif respostaatualiza == 6: 
                    novovalor_treino = "dtfim_treino"
                    atualiza_treino(novovalor_treino)

                elif respostaatualiza == 7: 
                    novovalor_treino = "status_treino"
                    atualiza_treino(novovalor_treino)

                elif respostaatualiza == 8: 
                    novovalor_treino = "cod_prof"
                    atualiza_treino(novovalor_treino)
                    
                elif respostaatualiza == 9: 
                    novovalor_treino = "objetivo_treino"
                    atualiza_treino(novovalor_treino)

                elif respostaatualiza == 10: 
                    ovovalor_treino = "tempo_treino"
                    atualiza_treino(novovalor_treino)
                else:
                    print('\n')
                    cabeçalho('\033[31m Opcao invalida\033[m')
                    sleep(3)

        elif resposta4 == 3:
            print("\n" * os.get_terminal_size().lines)
            cabeçalho('\033[1;36m        SMARTGYM APP\033[m') 
            cabeçalho('\033[36m         Consultar Treinos\033[m')
            respostatreino = menu(['Consultar treinos por professor','Consultar por Aluno'])
            if respostatreino == 1:
                exibe_treino_prof()

            if respostatreino == 2:
                exibe_treino_aluno()
                
            elif resposta4 == 4:
                False
            else:
                cabeçalho('\033[33m     Opção inválida\033[m')
#Fim menu treino

            
#Menu Professor    
    elif resposta == 2:
        print("\n" * os.get_terminal_size().lines)
        cabeçalho('\033[36mMENU Professor\033[m')
        resposta3 = menu(['Cadastrar Professor','Atualizar Informações Professor','Consultar Professores','Sair'])

#Menu Cadastro Professor
        if resposta3 == 1:
            print("\n" * os.get_terminal_size().lines)
            cabeçalho('\033[1;36m        SMARTGYM APP\033[m') 
            cabeçalho('\033[36m         Cadastro Professor\033[m')
            criar_prof()

#Atualizar informações do professores
        elif resposta3 == 2:
            print("\n" * os.get_terminal_size().lines)
            cabeçalho('\033[1;36m        SMARTGYM APP\033[m') 
            cabeçalho('\033[36m         Atualizar Professor\033[m')
            atlzprof = menu(['Atualizacao por CPF','Por Codigo Professor'])
            if atlzprof == 1:
                print("\n" * os.get_terminal_size().lines)
                cabeçalho('\033[1;36m        SMARTGYM APP\033[m') 
                cabeçalho('\033[36m         Atualizar Professor\033[m')
                respostaatualiza = menu(['Contato','CEP','Endereco','Numero Endereco','Hora Saida','Hora Entrada','Especializacao'])
                if respostaatualiza == 1:                    
                    novovalor_prof = "contato_prof"
                    atualiza_prof_cpf(novovalor_prof)                    
                elif respostaatualiza == 2: 
                    novovalor_prof = "cep_prof"
                    atualiza_prof_cpf(novovalor_prof)

                elif respostaatualiza == 3: 
                    novovalor_prof = "endereco_prof"
                    atualiza_prof_cpf(novovalor_prof)
                    
                elif respostaatualiza == 4: 
                    novovalor_prof = "endereco_nmr_prof"
                    atualiza_prof_cpf(novovalor_prof)
                    
                elif respostaatualiza == 5: 
                    novovalor_prof = "hrsaida_prof"
                    atualiza_prof_cpf(novovalor_prof)
                    
                elif respostaatualiza == 6: 
                    novovalor_prof = "hora_entrada_prof"
                    atualiza_prof_cpf(novovalor_prof)
                    
                elif respostaatualiza == 7: 
                    novovalor_prof = "especializacao"
                    atualiza_prof_cpf(novovalor_prof)

            elif atlzprof == 2:
                print("\n" * os.get_terminal_size().lines)
                cabeçalho('\033[1;36m        SMARTGYM APP\033[m') 
                cabeçalho('\033[36m         Atualizar Professor\033[m')
                respostaatualiza = menu(['Contato','CEP','Endereco','Numero Endereco','Hora Saida','Hora Entrada','Especializacao'])
                if respostaatualiza == 1:                    
                    novovalor_prof = "contato_prof"
                    atualiza_prof(novovalor_prof)                    
                elif respostaatualiza == 2: 
                    novovalor_prof = "cep_prof"
                    atualiza_prof(novovalor_prof)

                elif respostaatualiza == 3: 
                    novovalor_prof = "endereco_prof"
                    atualiza_prof(novovalor_prof)
                    
                elif respostaatualiza == 4: 
                    novovalor_prof = "endereco_nmr_prof"
                    atualiza_prof(novovalor_prof)
                    
                elif respostaatualiza == 5: 
                    novovalor_prof = "hrsaida_prof"
                    atualiza_prof(novovalor_prof)
                    
                elif respostaatualiza == 6: 
                    novovalor_prof = "hora_entrada_prof"
                    atualiza_prof(novovalor_prof)
                    
                elif respostaatualiza == 7: 
                    novovalor_prof = "especializacao"
                    atualiza_prof(novovalor_prof)
            else:
                print('\n')
                cabeçalho('\033[33m Opcao invalida')
            sleep(3)


#Consulta Professores
        elif resposta3 == 3:
            print("\n" * os.get_terminal_size().lines)
            cabeçalho('\033[1;36m        SMARTGYM APP\033[m') #
            cabeçalho('\033[36m         Consultar Professores\033[m')
            print('Opcoes de consulta:')
            opcconsulta = menu(['Todos os professores','Buscar por CPF','Por Codigo do Professor'])
            if opcconsulta == 1:
                exibe_prof()

            elif opcconsulta == 2:
                exibe_prof_cpf()

            elif opcconsulta == 3:
                exibe_prof_cod()

            else:
                cabeçalho('Opção inválida')
                sleep(2)

        elif resposta3 == 4:
            False

        else:
            cabeçalho('Opção inválida')
        sleep(1)


    elif resposta == 4:
        print("\n" * os.get_terminal_size().lines)
        cabeçalho('\033[1;36m        SMARTGYM APP\033[m')
        cabeçalho('\033[36mMENU MENSALIDADE\033[m')
        resposta5 = menu(['Consultar Mensalidade','Atualizar Mensalidade','Gerar Mensalidade (Caso nao tenha gerado automatico com a matricula)','Sair'])
        if resposta5 == 1:
            print("\n" * os.get_terminal_size().lines)
            cabeçalho('\033[1;36m        SMARTGYM APP\033[m') 
            cabeçalho('\033[36m         Consultar Mensalidade\033[m')
            print('\nOpcoes disponiveis\n')
            opcconsulta = menu(['Consulta todas mensalidades','Consulta por Aluno','Por intervalo de Data Vencimento','Por intervalo de Data Pagamento','Sair'])
            if opcconsulta == 1:
                exibe_mensalidade()
            
            elif opcconsulta == 2:
                exibe_mensalidade_aluno()

            elif opcconsulta == 3:
                exibe_mensalidade_datavence()
                
            elif opcconsulta == 4:
                exibe_mensalidade_datapago()

            elif opcconsulta == 5:
                cabeçalho('\033[33m\n     Voltando para o menu principal\n\033[m')
                False
            else:
                print('\n')
                cabeçalho('Opcao invalida')          
        
        elif resposta5 == 2:
            print("\n" * os.get_terminal_size().lines)
            cabeçalho('\033[1;36m        SMARTGYM APP\033[m') 
            cabeçalho('\033[36m         Atualizar Mensalidade \033[m')
#Começo atualiza Mensalidade
            campoatualiza = menu(['Valor','Status','Data Vencimento','Data pagamento (realizado)','Sair'])
            #campoatualiza = input('Digite a coluna que deseja alterar [valor,status,datavence,datavence,datapago]: ')
            if campoatualiza == 1:                    
                novovalor_mensalidade = "valor_mensalidade"
                atualiza_mensalidade(novovalor_mensalidade)  

            elif campoatualiza == 2: 
                print('\033[32m\n*digite 1 para mensalidade (PAGA) ou 0 para mensalidade (AGUARDANDO PAGAMENTO)')
                novovalor_mensalidade = "status_mensalidade"
                atualiza_mensalidade(novovalor_mensalidade)

            elif campoatualiza == 3: 
                novovalor_mensalidade = "data_vence"
                atualiza_mensalidade(novovalor_mensalidade)
            
            elif campoatualiza == 4: 
                novovalor_mensalidade = "data_paga"
                atualiza_mensalidade(novovalor_mensalidade)
            elif campoatualiza ==5:
                True
            else:
                print('\n')
                cabeçalho('\033[31m Opcao invalida\033[m')
                sleep(3)
            
        elif resposta5 == 3:
            print("\n" * os.get_terminal_size().lines)
            cabeçalho('\033[1;36m        SMARTGYM APP\033[m') 
            cabeçalho('\033[36m         Gerar Mensalidade\033[m')
            gera_mensalidade()

        elif resposta5 == 4:
            False

        else:
            cabeçalho('Opção inválida')
            sleep(3)

#Menu Matricula
    elif resposta == 5:
        print("\n" * os.get_terminal_size().lines)
        cabeçalho('\033[36mMENU Matricula\033[m')
        resposta6 = menu(['Gerar Matricula','Atualizar Matricula','Consultar Matriculas','Gerenciar Planos','Atualizar Plano Matricula','Sair'])
        if resposta6 == 1:
            print("\n" * os.get_terminal_size().lines)
            cabeçalho('\033[1;36m        SMARTGYM APP\033[m') 
            cabeçalho('\033[36m         Gerar Matricula\033[m')
            criar_matricula( )

        elif resposta6 == 2:
            print("\n" * os.get_terminal_size().lines)
            cabeçalho('\033[1;36m        SMARTGYM APP\033[m') 
            cabeçalho('\033[36m         Atualizar Status Matricula \033[m')
#Valida CODIGO ALUNO
            if valida_cod_aluno() == True:
#Começo do atualiza Aluno
                    atualiza_matricula_status(
                    input('Confirme o numero do CODIGO do Aluno que deseja alterar informações: '),
                    input('Digite [1] para MATRICULA ATIVA ou [0] para MATRICULA TRANCADA OU ENCERRADA: ')
                    )
                    confirma = input('Deseja confirmar a atualizacao do campo Status Matricula [s ou n]')
                    if confirma == 'S' or confirma == 's':
                        conn.commit()
                        cabeçalho('O Status da Matricula atualizada com sucesso')
                        False
                    else:
                        conn.rollback()
                        cabeçalho('Status Matricula não atualizada')
                        True
            else:
                cabeçalho('CODIGO Invalido, nao cadastrado no sistema')
            continuar = int(input('Digite [1] se deseja continuar no sistemaa ou [2] para sair: '))
            if continuar == 1:
                False 
            else:
                quit()

        elif resposta6 == 3:
            print("\n" * os.get_terminal_size().lines)
            cabeçalho('\033[1;36m        SMARTGYM APP\033[m') 
            cabeçalho('\033[36m         Consultar Matricula\033[m')
#Começo consulta matriculas
            opcconsulta = menu(['Consultar Todas as Matriculas','Consultar por codigo do aluno','Sair'])
            if opcconsulta == 1:
                exibe_matricula()
            elif opcconsulta == 2:
                exibe_matricula_aluno()
            elif opcconsulta == 3:
                print('\n')
                cabeçalho('\033[33m\n     Voltando para o menu principal\n\033[m')
                False
                sleep(1)
            else:
                print('\n')
                cabeçalho('\033[33m\n     Opcao Invalida\n\033[m')

#Menu Plano
        elif resposta == 5:
            print("\n" * os.get_terminal_size().lines)
            cabeçalho('\033[1;36m        SMARTGYM APP\033[m')
            cabeçalho('\033[36mMENU PLANO\033[m')
            resposta7 = menu(['Cadastrar Plano','Atualizar Desconto Plano','Consultar Planos','Sair'])
            if resposta7 == 1:
                print("\n" * os.get_terminal_size().lines)
                cabeçalho('\033[1;36m        SMARTGYM APP\033[m') 
                cabeçalho('\033[36m         Cadastro Plano\033[m')
                criar_plano()

            elif resposta7 == 2:
                print("\n" * os.get_terminal_size().lines)
                cabeçalho('\033[1;36m        SMARTGYM APP\033[m') 
                cabeçalho('\033[36m         Atualizar Desconto do Plano \033[m')
                atualiza_plano_desconto()

            elif resposta7 == 3:
                print("\n" * os.get_terminal_size().lines)
                cabeçalho('\033[1;36m        SMARTGYM APP\033[m') 
                cabeçalho('\033[36m         Consultar Planos \033[m')
                exibe_plano()
            sleep(3)
        elif resposta == 6:
            print("\n" * os.get_terminal_size().lines)
            cabeçalho('\033[1;36m        SMARTGYM APP\033[m') 
            cabeçalho('\033[36m         Atualizar Status Plano \033[m')
#Valida CODIGO ALUNO
            if valida_cod_aluno() == True:
#Começo do atualiza Aluno
                    atualiza_matricula_status_plano(
                    input('Confirme o numero do CODIGO da Matricula que deseja alterar informações: '),
                    input('Digite [1] para Plano Ativo ou [0] para Plano Encerrado: ')
                    )
                    confirma = input('Deseja confirmar a atualizacao do campo Status Plano [s ou n]')
                    if confirma == 'S' or confirma == 's':
                        conn.commit()
                        cabeçalho('O Status Plano atualizado com sucesso')
                        False
                    else:
                        conn.rollback()
                        cabeçalho('Status Plano não atualizado')
                        True
            else:
                cabeçalho('CODIGO Invalido, nao cadastrado no sistema')
            continuar = int(input('Digite [1] se deseja continuar no sistemaa ou [2] para sair: '))
            if continuar == 1:
                False 
            else:
                quit()


#Menu presença
    elif resposta == 6:
        print("\n" * os.get_terminal_size().lines)
        cabeçalho('\033[36mMENU Presenças\033[m')
        resposta7 = menu(['Gerar Presenca Entrada','Gerar Saida','Atualizar Presença','Consultar Presenças','Sair'])
        if resposta7 == 1:
            print("\n" * os.get_terminal_size().lines)
            cabeçalho('\033[1;36m        SMARTGYM APP\033[m') 
            cabeçalho('\033[36m         Gerar Presenca Entrada\033[m')
            gera_presenca()

        if resposta7 == 2:
            print("\n" * os.get_terminal_size().lines)
            cabeçalho('\033[1;36m        SMARTGYM APP\033[m') 
            cabeçalho('\033[36m         Gerar Saida\033[m')
            gera_saida()

        elif resposta7 == 3:
            print("\n" * os.get_terminal_size().lines)
            cabeçalho('\033[1;36m        SMARTGYM APP\033[m') 
            cabeçalho('\033[36m         Gerar Presença Com Dados caso o Aluno tenha esquecido de dar presenca\033[m')
            gera_presenca_alt()

        elif resposta7 == 4:
            print("\n" * os.get_terminal_size().lines)
            cabeçalho('\033[1;36m        SMARTGYM APP\033[m') 
            cabeçalho('\033[36m         Consultar Presenças\033[m')
            opconsulta = menu(['Consulta por aluno','Consulta todas a presencas','Consulta presenca com intervalo entre datas'])
            if opconsulta == 1:
                exibe_presenca_aluno()

            elif opconsulta == 2:
                exibe_presenca()

            elif opconsulta == 3:
                exibe_presenca_data()
            else:
                cabeçalho('Opcao invalida')
        sleep(1)
            

    elif resposta == 7:
        cabeçalho('\033[31mSaindo do sistema... Até logo\033[m')
        break
        
#Fim do loop menu   
    else:
        cabeçalho('\033[31mERRO, Digite uma opção válida\033[m')
        
