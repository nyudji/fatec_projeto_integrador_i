import psycopg2
import os
import sys
from time import sleep




# Dados para conexão do banco de dados, 
host = "localhost"
dbname = "smartgym"
user = "postgres"
password = "admin"
sslmode = "disable"

# Construct connection string
conn_string = "host={0} user={1} dbname={2} password={3} sslmode={4}".format(host, user, dbname, password, sslmode)
conn = psycopg2.connect(conn_string)
print("Connection established")

cur = conn.cursor()

########################################## Outros ###################################################

########################################## Cadastros ###################################################

#Cadastro de alunos
def criar_aluno():
    cpf_aluno = input('Digite CPF [Apenas numeros]: '),
    nome_aluno = input('Digite nome do Aluno: '),
    sexo_aluno =input('Digite o sexo [M ou F]: '),
    dtnasc_aluno= input('Digite a data de nascimento do aluno [DD-MM-AAAA]: '),
    rg_aluno = input('Digite RG do Aluno[somente numeros]: '),
    contato_aluno = input('Digite telefone de contato do Aluno[apenas numero ex 1199999999]: '),
    cep_aluno = input('Digite CEP do Aluno: '),
    endereco_aluno = input('Digite Endereco do Aluno: '),
    endereco_nmr_aluno = input('Digite Numero da Casa do Aluno: ')
    cur.execute("insert into aluno (cpf_aluno, nome_aluno, sexo_aluno, dtnasc_aluno, rg_aluno, contato_aluno, cep_aluno, endereco_aluno, endereco_nmr_aluno, cod_aluno) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,default);",(cpf_aluno, nome_aluno, sexo_aluno, dtnasc_aluno, rg_aluno, contato_aluno, cep_aluno, endereco_aluno, endereco_nmr_aluno))
    confirma = input('\033[32m\nDeseja confirmar o cadastro? [s ou n]: \033[m')
    if confirma == 'S' or confirma == 's':
        conn.commit()
        print('\n')
        cabeçalho('\033[32m   Aluno registrado com sucesso\033[m')
        sleep(3)
    else:
        conn.rollback()
        print('\n')
        cabeçalho('\031[36m    Aluno nao registrado\033[m')
        sleep(3)
    confirma = input('\nDeseja realizar novo cadastro? [s ou n]:')
    if confirma == 'S' or confirma == 's':
        print("\n" * os.get_terminal_size().lines)
        cabeçalho('\033[1;36m        SMARTGYM APP\033[m') 
        cabeçalho('\033[36m         Cadastro Aluno\033[m')
        criar_aluno()
    else:
        print('\n')
        cabeçalho('\033[33m\n     Voltando para o menu principal\n\033[m')
        False
        sleep(1)

#Cadastro de Professor
def criar_prof():
    cpf_prof = input('Digite CPF [Apenas numeros]: '),
    nome_prof = input('Digite nome do Professor: '),
    rg_prof = input('Digite RG do professor[somente numeros]: '),
    especializacao =input('Digite a(s) especializacao(oes) do Professor: '),
    contato_prof = input('Digite telefone de contato do Professor[apenas numero ex 1199999999]: '),
    hr_entrada_prof = input('Digite a hora de entrada [08:00 ou 18:00]: '),
    hr_saida_prof = input('Digite a hora de saida [08:00 ou 18:00]: '),
    cep_prof = input('Digite CEP do Professor: '),
    endereco_prof = input('Digite Endereco do Professor: '),
    endereco_nmr_prof = input('Digite Numero da Casa do Professor: '),
    sexo_prof = input('Digite o sexo (M OU F): '),
    dtnasc_prof = input('Digite a data de nascimento DD-MM-AAAA: ')
    cur.execute("insert into professor (cpf_prof, nome_prof, rg_prof, especializacao, contato_prof, hr_entrada_prof, hr_saida_prof, cep_prof, endereco_prof, endereco_nmr_prof, sexo_prof, dtnasc_prof, cod_prof) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,default);",(cpf_prof, nome_prof, rg_prof, especializacao, contato_prof, hr_entrada_prof, hr_saida_prof, cep_prof, endereco_prof, endereco_nmr_prof, sexo_prof, dtnasc_prof))
    confirma = input('\033[32m\nDeseja confirmar o cadastro? [s ou n]: \033[m')
    if confirma == 'S' or confirma == 's':
        conn.commit()
        print('\n')
        cabeçalho('\033[32m      Professor registrado com sucesso\033[m')
        sleep(3)
    else:
        conn.rollback()
        print('\n')
        cabeçalho('\031[36m     Professor nao registrado\033[m')
        sleep(3)
    denovo = input('\nDeseja realizar novo cadastro? [s ou n]:')
    if denovo == 'S' or denovo == 's':
        print("\n" * os.get_terminal_size().lines)
        cabeçalho('\033[1;36m        SMARTGYM APP\033[m') 
        cabeçalho('\033[36m         Cadastro Professor\033[m')
        criar_prof()
    else:
        print('\n')
        cabeçalho('\033[33m\n     Voltando para o menu principal\n\033[m')
        False
        sleep(1)

#Criacao de Treino
def criar_treino():
    if valida_cod_prof() == True:
        if valida_cod_aluno() == True:
            atividade_treino = input('Digite a atividade a ser feita: '),
            serie_treino= input('Digite a serie da atividade (quantidade): '),
            intervalo_treino= input('Digite o intervalo (em segundos): '),
            repeticao_treino= input('Digite a quantidade de vezes que atividade sera repetida: '),
            dtinicio_treino= input('Digite a data do inicio do treino: '),
            dtfim_treino = input('Digite a data do fim (estimado) do treino: '),
            status_treino = input('Digite o status do treino [NAO COMECOU, EM ANDAMENTO OU FINALIZADO]: '),
            objetivo_treino = input('Digite objetivo ou descricacao do treino(opcional): '),
            tempo_treino = input('Tempo de finalizacao do treino(opcional) [ex: 30 minutos = 00:30]: ')
            cur.execute("insert into treino (cod_treino, atividade_treino, serie_treino, intervalo_treino, repeticao_treino, cod_aluno, dtinicio_treino, dtfim_treino, status_treino, cod_prof, objetivo_treino, tempo_treino) values (DEFAULT,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);",(atividade_treino, serie_treino, intervalo_treino, repeticao_treino, cod_aluno_valida, dtinicio_treino, dtfim_treino, status_treino, cod_prof_valida, objetivo_treino, tempo_treino))
            confirma = input('\033[32m\nDeseja confirmar o registro do treino? [s ou n]: \033[m')
            if confirma == 'S' or confirma == 's':
                conn.commit()
                print('\n')
                cabeçalho('\033[32m      Treino registrado com sucesso\033[m')
                sleep(3)
            else:
                conn.rollback()
                print('\n')
                cabeçalho('\031[36m     Treino nao registrado\033[m')
                sleep(3)
        
        else:
            print('\n')
            cabeçalho('\033[31mCodigo aluno invalido\033[m')        
    else:
        print('\n')
        cabeçalho('\033[31mCodigo Professor invalido\033[m')
    denovo = input('\nDeseja realizar novo cadastro? [s ou n]: ')
    if denovo == 'S' or denovo == 's':
        print("\n" * os.get_terminal_size().lines)
        cabeçalho('\033[1;36m        SMARTGYM APP\033[m') 
        cabeçalho('\033[36m         Cadastro Treino\033[m')
        criar_treino()
    else:
        print('\n')
        cabeçalho('\033[33m\n     Voltando para o menu principal\n\033[m')
        False
        sleep(1)

#Criacao de Plano
def criar_plano():
    desc_plano = input('Digite a descrição do plano, ex: TRIMESTRAL: '),
    qt_meses = input('Quantidade de meses: '),
    desconto_plano = input('Porcentagem do desconto do plano, ex: 0.07 para 7% , ou 0.10 para 10%]: '),
    cur.execute("insert into plano (cod_plano, desc_plano, qt_meses, desconto_plano) values (DEFAULT,%s,%s,%s);",(desc_plano, qt_meses, desconto_plano))
    confirma = input('\033[32m\nDeseja confirmar o registro de um novo plano? [s ou n]: \033[m')
    if confirma == 'S' or confirma == 's':
        conn.commit()
        print('\n')
        cabeçalho('\033[32m      Novo plano registrado com sucesso\033[m')
        sleep(3)
    else:
        conn.rollback()
        print('\n')
        cabeçalho('\031[36m     Novo plano nao registrado\033[m')
        sleep(3)
    denovo = input('\nDeseja realizar novo cadastro? [s ou n]: ')
    if denovo == 'S' or denovo == 's':
        print("\n" * os.get_terminal_size().lines)
        cabeçalho('\033[1;36m        SMARTGYM APP\033[m') 
        cabeçalho('\033[36m         Cadastro Plano\033[m')
        criar_plano()
    else:
        print('\n')
        cabeçalho('\033[33m\n     Voltando para o menu principal\n\033[m')
        False
        sleep(1)
        
def validamatricula():
    cur.execute("SELECT status_matricula FROM matricula WHERE cod_aluno=%s AND status_matricula=True;",(cod_aluno_valida, ))
    if cur.rowcount == 0:
        return True
    else:
        return False

#Realização de Matricula
global cod_plano
global cod_aluno
i=0
def criar_matricula():
    if valida_cod_aluno() == True:
        if validamatricula() == True:
            if valida_plano() == True:
                cur.execute("insert into matricula (cod_matricula, dt_matricula, status_matricula, cod_plano, cod_aluno, status_plano, fim_plano) values (DEFAULT,CURRENT_DATE,TRUE,%s,%s,TRUE,null);",(cod_plano_valida, cod_aluno_valida))
                confirma = input('\033[32m\nDeseja confirmar a realizacao da matricula? Digite [s ou n]: \033[m')
                if confirma == 'S' or confirma == 's':
                    cur.execute("SELECT qt_meses FROM plano WHERE cod_plano=%s ;",(cod_plano_valida))
                    quantidademeses={}
                    quantidademeses = cur.fetchone() #colocar resultados em um resultset
                    cur.execute("UPDATE matricula SET fim_plano = CURRENT_DATE + 30 * %s WHERE cod_aluno=%s and cod_plano=%s;",(quantidademeses, cod_aluno_valida, cod_plano_valida))
                    valor_mensalidade = int(input('\nDigite o valor da mensalidade (total, sem desconto): '))
                    valor_mensalidade_confirma = int(input('Confirme o valor da mensalidade (total, sem desconto): '))
                    if valor_mensalidade == valor_mensalidade_confirma:
                        cur.execute("SELECT qt_meses FROM plano WHERE cod_plano=%s;",(cod_plano_valida))
                #Calcula valor final da mensalidade 
                        quantidademeses = cur.fetchone() #colocar resultados em um resultset
                        intquantidademeses = int(quantidademeses[0])
                        cur.execute("SELECT desconto_plano FROM plano WHERE cod_plano=%s;",(cod_plano_valida))
                        descontoplano = cur.fetchone()
                        valorconta = float(valor_mensalidade) * float(descontoplano[0])
                        valorfinal = float(valor_mensalidade) - float(valorconta) 
                #Cria mensalidade
                        for i in range(1, int(quantidademeses[0])+1):
                            intloop = i+1
                            cur.execute("insert into mensalidade (cod_mensalidade, valor_mensalidade, dt_pago, dt_vence, status_mensalidade, cod_aluno) values (DEFAULT,%s,null,current_date + 30 * %s,False,%s);",(valorfinal, intloop, cod_aluno_valida))
                            i = i+1
                        conn.commit()
                        print('\n')
                        cabeçalho('\033[32m      Matricula realizada com sucesso\033[m')
                        sleep(3)
                    else:
                        print('\n')
                        cabeçalho('Valor nao confere')
                else:
                    conn.rollback()
                    print('\n')
                    cabeçalho('\033[36m     Matricula nao realizada\033[m')
                    sleep(3)
            else:
                print('\n')
                cabeçalho('\033[31mCodigo plano invalido\033[m')        
        else:
                print('\n')
                cabeçalho('\033[31mAluno ja possui uma matricula ativa\033[m')
    else:
        print('\n')
        cabeçalho('\033[31mCodigo aluno invalido\033[m')

    denovo = input('\nDeseja realizar nova matricula? [s ou n]: ')
    if denovo == 'S' or denovo == 's':
        print("\n" * os.get_terminal_size().lines)
        cabeçalho('\033[1;36m        SMARTGYM APP\033[m') 
        cabeçalho('\033[36m         Gerar Matricula\033[m')
        criar_matricula()
    else:
        print('\n')
        cabeçalho('\033[33m\n     Voltando para o menu principal\n\033[m')
        False
        sleep(1)    


#Gera mensalidade
def gera_mensalidade():
    print('\nDigite o cod do aluno para gerar mensalidade')
    if valida_cod_aluno() == True:
        valormensalide = input('Digite o novo valor da mensalidade [ex: 89.89]: ')
        dt_vence = input('Digite a data de vencimento: ')
        cur.execute("insert into mensalidade (cod_mensalidade, valor_mensalidade, dt_pago, dt_vence, status_mensalidade, cod_aluno) values (DEFAULT,%s,null,%s,False,%s);",(valormensalide, dt_vence, cod_aluno_valida))
    else:
        print('\n')
        cabeçalho('\033[31mCodigo aluno invalido\033[m')
    
    denovo = input('\nDeseja gerar nova mensalidade? [s ou n]: ')
    if denovo == 'S' or denovo == 's':
        print("\n" * os.get_terminal_size().lines)
        cabeçalho('\033[1;36m        SMARTGYM APP\033[m') 
        cabeçalho('\033[36m         Gerar Mensalidade\033[m')
        gera_mensalidade()
    else:
        print('\n')
        cabeçalho('\033[33m\n     Voltando para o menu principal\n\033[m')
        False
        sleep(1)  
    sleep(3)

#Valida se o aluno ja realizou presencca
def validapresenca():
    cur.execute("SELECT (dt_presenca, status_presenca) FROM aluno_presenca WHERE cod_aluno=%s AND dt_presenca=current_date AND status_presenca=false;",(cod_aluno_valida, ))
    if cur.rowcount == 0:
         return True
    else:
        return False

#Gera presença
def gera_presenca():
        if valida_cod_aluno() == True:
            if validapresenca() == True:
                cur.execute("insert into aluno_presenca (cod_aluno, dt_presenca, hr_presenca, hrsaida_presenca, status_presenca) values (%s,current_date,current_time,null,false);",(cod_aluno_valida))
                confirma = input('Deseja confirmar presenca do aluno? [s ou n]: ')
                if confirma == 'S' or confirma == 's':
                    conn.commit()
                    cabeçalho('Presenca registrada com sucesso')
                    False
                else:
                    conn.rollback()
                    cabeçalho('Presenca nao registrada')
                    
                    True
            else:
                cabeçalho('Aluno ja realizou presenca hoje')
        else:
            cabeçalho('Codigo aluno invalido')
        sleep(2)


#Gera saida
def gera_saida():
            
        if valida_cod_aluno() == True:     
            if validapresenca() == False:
                cur.execute("UPDATE aluno_presenca SET hrsaida_presenca=current_time, status_presenca=true WHERE cod_aluno=%s AND dt_presenca=current_date AND status_presenca=false;",(cod_aluno_valida))
                confirma = input('Deseja confirmar saida do aluno? [s ou n]: ')
                if confirma == 'S' or confirma == 's':
                    conn.commit()
                    cabeçalho('Saida cadastrada com sucesso')
                    
                    False
                else:
                    conn.rollback()
                    cabeçalho('Saida nao registrada')
                    
                    True               
            else:
                cabeçalho('Aluno ainda nao realizou presenca')
        else:
                cabeçalho('Codigo aluno invalido')
        sleep(2)

#Gera presença Com Dados
def gera_presenca_alt():
        if valida_cod_aluno() == True:
            dt_presenca = input('Digite a data de presenca [DD-MM-AAAA]')  
            hr_presenca = input('Digite a hora de presenca [09:20]')
            hrsaida_presenca = input('Digite a hora de saida [09:20]') 
            cur.execute("insert into aluno_presenca (cod_aluno, dt_presenca, hr_presenca, hrsaida_presenca) values (%s,%s,%s,%s);",(cod_aluno_valida, dt_presenca, hr_presenca, hrsaida_presenca))
            confirma = input('Deseja confirmar presenca do aluno? [s ou n]: ')
            if confirma == 'S' or confirma == 's':
                conn.commit()
                cabeçalho('Presenca registrada com sucesso')
                sleep(3)
                False
            else:
                conn.rollback()
                cabeçalho('Presenca nao registrada')
                sleep(3)
                True
        else:
            print('Codigo aluno invalido')
            sleep(3)

#Gera acompanhamento aluno
def gera_acompanhamento():
        if valida_cod_aluno() == True:
            if valida_cod_prof() == True:
                peso = input('Digite o peso do aluno, apenas o numero: ')
                altura = input('Digite a altura [1.73]: ')
                massamagra = input('Digite a massa magra: ')
                perc_gordura = input('Digite a porcentagem de gordura, ex 10% = 0.10, ou 20% = 0.20: ')
                med_braco = input('Digite a medida do braco, apenas numero: ')
                med_ante = input('Digite a medida do antebraco: ')
                med_peito = input('Digite a medida do peito: ')
                med_quadris = input('Digite a medida do quadris: ')
                med_cintura = input('Digite a medida do antebraco: ')
                med_panturrilha = input('Digite a medida da panturrilha: ')
                cur.execute("insert into acompanhamento_aluno (cod_acomp, data_acomp, peso, altura, massamagra, perc_gordura, med_braco, med_ante, med_peito, med_quadris, med_cintura, med_panturrilha, cod_aluno, cod_prof) values (default,current_date,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);",(peso, altura, massamagra, perc_gordura, med_braco, med_ante, med_peito, med_quadris, med_cintura, med_panturrilha, cod_aluno_valida, cod_prof_valida))
                confirma = input('\033[32mDeseja confirmar o registro de acompanhamento do aluno? [s ou n]: \033[m')
                if confirma == 'S' or confirma == 's':
                    conn.commit()
                    print('\n')
                    cabeçalho('\033[32mAcompanhamento registrado com sucesso com sucesso\033[m')
                    sleep(3)
                    False
                else:
                    conn.rollback()
                    print('\n')
                    cabeçalho('\033[31mAcompanhamento nao registrado\033[m')
                    sleep(3)
                    True
            else:
                print('\n')
                cabeçalho('\033[31mCodigo professor invalido\033[m')
        else:
            print('\n')
            cabeçalho('\033[31mCodigo aluno invalido\033[m')
            sleep(3)
    

###################################             Consultas                 ###################################################

#######################################         Consulta Aluno       ########################################################

#Consulta todos Alunos
def exibe_aluno():
    cur.execute("SELECT * FROM aluno;")
    resultado = cur.fetchall() #colocar resultados em um resultset
    for res in resultado:
        print(res)
    
    confirmadnvo = input('\n\033[31mDeseja sair do aplicativo? [s ou n]: \033[m')
    if confirmadnvo == 'S' or confirmadnvo == 's':
        print("\n" * os.get_terminal_size().lines)
        cabeçalho('\033[1;36m\n  ENCERRANDO APLICATIVO...\n\033[m')
        quit()
    else:
        cabeçalho('\033[33m\n     Voltando para o menu principal\n\033[m')
        False
        sleep(1)

#Consulta Aluno por CPF
def exibe_aluno_cpf():
    if valida_cpf_aluno() == True:
        cur.execute("SELECT * FROM aluno WHERE cpf_aluno=%s;",(cpf_aluno_valida, ))
        resultado = cur.fetchall() #colocar resultados em um resultset
        for res in resultado:
            print(res)
    else:
        cabeçalho('\033[31m\nCodigo CPF Invalido, nao cadastrado no sistema\n\033[m')
    
    confirmadnvo = input('\n\033[32mDeseja realizar nova consulta? [s ou n]: \033[m')
    if confirmadnvo == 'S' or confirmadnvo == 's':
        print("\n" * os.get_terminal_size().lines)
        cabeçalho('\033[1;36m        SMARTGYM APP\033[m') 
        cabeçalho('\033[36m         Consulta Aluno\033[m')
        exibe_aluno_cpf()
            
    else:
        cabeçalho('\033[33m\n     Voltando para o menu principal\n\033[m')
        False
        sleep(1)

#Consulta Aluno por COD
def exibe_aluno_cod():
    if valida_cod_aluno() == True:
        cur.execute("SELECT * FROM aluno WHERE cod_aluno=%s;",(cod_aluno_valida, ))
        resultado = cur.fetchall() #colocar resultados em um resultset
        for res in resultado:
            print(res)
    else:
        
        cabeçalho('    \033[31m\nCodigo Invalido, nao cadastrado no sistema\n\033[m')

    confirmadnvo = input('\n\033[32mDeseja realizar nova consulta? [s ou n]: \033[m')
    if confirmadnvo == 'S' or confirmadnvo == 's':
        print("\n" * os.get_terminal_size().lines)
        cabeçalho('\033[1;36m        SMARTGYM APP\033[m') 
        cabeçalho('\033[36m         Consulta Aluno\033[m')
        exibe_aluno_cod()
        
    else:
        cabeçalho('\033[33m\n     Voltando para o menu principal\n\033[m')
        False
        sleep(1)
    

##########################################    Consulta Professor   ###################################################

#Consulta todos Professores
def exibe_prof():
    cur.execute("SELECT * FROM professor;")
    resultado = cur.fetchall() #colocar resultados em um resultset
    for res in resultado:
        print(res)
    confirmadnvo = input('\n\033[31mDeseja sair do aplicativo? [s ou n]: \033[m')
    if confirmadnvo == 'S' or confirmadnvo == 's':
        print("\n" * os.get_terminal_size().lines)
        cabeçalho('\033[1;36m\n  ENCERRANDO APLICATIVO...\n\033[m') 
        quit()
    else:
        cabeçalho('\033[33m\n     Voltando para o menu principal\n\033[m')
        False
        sleep(1) 

#Consulta professor por cod
def exibe_prof_cod():
    if valida_cod_prof() == True:
        cur.execute("SELECT * FROM professor WHERE cod_prof=%s;",(cod_prof_valida, ))
        resultado = cur.fetchall() #colocar resultados em um resultset
        for res in resultado:
            print(res)
    else:
        
        cabeçalho('    \033[31m\nCodigo Invalido, nao cadastrado no sistema\n\033[m')

    confirmadnvo = input('\n\033[32mDeseja realizar nova consulta? [s ou n]: \033[m')
    if confirmadnvo == 'S' or confirmadnvo == 's':
        print("\n" * os.get_terminal_size().lines)
        cabeçalho('\033[1;36m        SMARTGYM APP\033[m') 
        cabeçalho('\033[36m         Consulta Professor\033[m')
        exibe_prof_cod()
        
    else:
        cabeçalho('\033[33m\n     Voltando para o menu principal\n\033[m')
        False
        sleep(1)

#Consulta Professores por CPF
def exibe_prof_cpf():
    if valida_cpf_prof() == True:
        cur.execute("SELECT * FROM professor WHERE cpf_prof=%s;",(cpf_prof_pego, ))
        resultado = cur.fetchall() #colocar resultados em um resultset
        for res in resultado:
            print(res)

    else:
        cabeçalho('    \033[31m\nCPF Invalido, nao cadastrado no sistema\n\033[m')
    
    confirmadnvo = input('\n\033[32mDeseja realizar nova consulta? [s ou n]: \033[m')
    if confirmadnvo == 'S' or confirmadnvo == 's':
        print("\n" * os.get_terminal_size().lines)
        cabeçalho('\033[1;36m        SMARTGYM APP\033[m') 
        cabeçalho('\033[36m         Consulta Treino por Aluno\033[m')
        exibe_prof_cpf()
        
    else:
        cabeçalho('\033[33m\n     Voltando para o menu principal\n\033[m')
        False
        sleep(1)

##########################################   Consulta Treino   ###################################################

#Consulta treino por Professor
def exibe_treino_prof():
    if valida_cod_prof() == True:
        cur.execute("SELECT * FROM treino WHERE cod_prof=%s;",(cod_prof_valida, ))
        resultado = cur.fetchall() #colocar resultados em um resultset
        for res in resultado:
            print(res)
    else:
        cabeçalho('    \033[31m\nCodigo Invalido, nao cadastrado no sistema\n\033[m')
    
    confirmadnvo = input('\n\033[32mDeseja realizar nova consulta? [s ou n]: \033[m')
    if confirmadnvo == 'S' or confirmadnvo == 's':
        print("\n" * os.get_terminal_size().lines)
        cabeçalho('\033[1;36m        SMARTGYM APP\033[m') 
        cabeçalho('\033[36m         Consulta Professor\033[m')
        exibe_treino_prof()
        
    else:
        cabeçalho('\033[33m\n     Voltando para o menu principal\n\033[m')
        False
        sleep(1)

#Consulta treino por Alunos
def exibe_treino_aluno():
    if valida_cod_aluno() == True:
        cur.execute("SELECT * FROM treino WHERE cod_prof=%s;",(cod_aluno_valida, ))
        resultado = cur.fetchall() #colocar resultados em um resultset
        for res in resultado:
            print(res)
    else:
        
        cabeçalho('    \033[31m\nCodigo Invalido, nao cadastrado no sistema\n\033[m')

    confirmadnvo = input('\n\033[32mDeseja realizar nova consulta? [s ou n]: \033[m')
    if confirmadnvo == 'S' or confirmadnvo == 's':
        print("\n" * os.get_terminal_size().lines)
        cabeçalho('\033[1;36m        SMARTGYM APP\033[m') 
        cabeçalho('\033[36m         Consulta Treino por Professor\033[m')
        exibe_treino_aluno()
        
    else:
        cabeçalho('\033[33m\n     Voltando para o menu principal\n\033[m')
        False
        sleep(1)

##########################################   Consulta Plano   ###################################################

def exibe_plano():
    cur.execute("SELECT * FROM plano;")
    resultado = cur.fetchall() #colocar resultados em um resultset
    for res in resultado:
        print(res)
    confirmadnvo = input('\n\033[31mDeseja sair do aplicativo? [s ou n]: \033[m')
    if confirmadnvo == 'S' or confirmadnvo == 's':
        print("\n" * os.get_terminal_size().lines)
        cabeçalho('\033[1;36m\n  ENCERRANDO APLICATIVO...\n\033[m') 
        quit()
    else:
        cabeçalho('\033[33m\n     Voltando para o menu principal\n\033[m')
        False
        sleep(1) 

def exibe_plano_aluno():
    if valida_cod_aluno() == True:
        cur.execute("SELECT * FROM matricula WHERE cod_aluno=%s;",(cod_aluno_valida, ))
        resultado = cur.fetchall() #colocar resultados em um resultset
        for res in resultado:
            print(res)
    else:
        cabeçalho('    \033[31m\nCodigo Invalido, nao cadastrado no sistema\n\033[m')
    
    confirmadnvo = input('\n\033[32mDeseja realizar nova consulta? [s ou n]: \033[m')
    if confirmadnvo == 'S' or confirmadnvo == 's':
        print("\n" * os.get_terminal_size().lines)
        cabeçalho('\033[1;36m        SMARTGYM APP\033[m') 
        cabeçalho('\033[36m         Consulta Matricula\033[m')
        exibe_plano_aluno()
        
    else:
        cabeçalho('\033[33m\n     Voltando para o menu principal\n\033[m')
        False
        sleep(1)

##########################################   Consulta Matricula   ###################################################

#Consulta todas as Matriculas
def exibe_matricula():
    cur.execute("SELECT * FROM matricula;")
    resultado = cur.fetchall() #colocar resultados em um resultset
    for res in resultado:
        print(res)
    confirmadnvo = input('\n\033[31mDeseja sair do aplicativo? [s ou n]: \033[m')
    if confirmadnvo == 'S' or confirmadnvo == 's':
        print("\n" * os.get_terminal_size().lines)
        cabeçalho('\033[1;36m\n  ENCERRANDO APLICATIVO...\n\033[m') 
        quit()
    else:
        cabeçalho('\033[33m\n     Voltando para o menu principal\n\033[m')
        False
        sleep(1)

def exibe_matricula_aluno():
    if valida_cod_aluno() == True:
        cur.execute("SELECT * FROM matricula WHERE cod_aluno=%s;",(cod_aluno_valida, ))
        resultado = cur.fetchall() #colocar resultados em um resultset
        for res in resultado:
            print(res)
    else:
        cabeçalho('    \033[31m\nCodigo Invalido, nao cadastrado no sistema\n\033[m')
    
    confirmadnvo = input('\n\033[32mDeseja realizar nova consulta? [s ou n]: \033[m')
    if confirmadnvo == 'S' or confirmadnvo == 's':
        print("\n" * os.get_terminal_size().lines)
        cabeçalho('\033[1;36m        SMARTGYM APP\033[m') 
        cabeçalho('\033[36m         Consulta Matricula\033[m')
        exibe_matricula_aluno()
        
    else:
        cabeçalho('\033[33m\n     Voltando para o menu principal\n\033[m')
        False
        sleep(1)

##########################################   Consulta Mensalidade   ###################################################
#Exibe todas mensalidades
def exibe_mensalidade():
    cur.execute("SELECT * FROM mensalidade;")
    resultado = cur.fetchall() #colocar resultados em um resultset
    for res in resultado:
        print(res)
    confirmadnvo = input('\n\033[31mDeseja sair do aplicativo? [s ou n]: \033[m')
    if confirmadnvo == 'S' or confirmadnvo == 's':
        print("\n" * os.get_terminal_size().lines)
        cabeçalho('\033[1;36m\n  ENCERRANDO APLICATIVO...\n\033[m') 
        quit()
    else:
        cabeçalho('\033[33m\n     Voltando para o menu principal\n\033[m')
        False
        sleep(1)

#Exibe mensalidade por aluno
def exibe_mensalidade_aluno():
    if valida_cod_aluno() == True:
        cur.execute("SELECT * FROM mensalidade WHERE cod_aluno=%s;",(cod_aluno_valida, ))
        resultado = cur.fetchall() #colocar resultados em um resultset
        for res in resultado:
            print(res)
    else:
        cabeçalho('    \033[31m\nCodigo Invalido, nao cadastrado no sistema\n\033[m')
    
    confirmadnvo = input('\n\033[32mDeseja realizar nova consulta? [s ou n]: \033[m')
    if confirmadnvo == 'S' or confirmadnvo == 's':
        print("\n" * os.get_terminal_size().lines)
        cabeçalho('\033[1;36m        SMARTGYM APP\033[m') 
        cabeçalho('\033[36m         Consulta Matricula\033[m')
        exibe_matricula_aluno()
        
    else:
        cabeçalho('\033[33m\n     Voltando para o menu principal\n\033[m')
        False
        sleep(1)

def exibe_mensalidade_datapago():
    if valida_cod_aluno() == True:
        dtinicio = input('\nDigite a data de inicio de intervalo de busca: ')
        dtfim = input('Digite a data fim de intervalo de busca: ')
        cur.execute("SELECT * FROM mensalidade WHERE dt_pago BETWEEN %s AND %s",(dtinicio, dtfim))
        resultado = cur.fetchall() #colocar resultados em um resultset
        for res in resultado:
            print(res)
    else:
        cabeçalho('    \033[31m\nCodigo Invalido, nao cadastrado no sistema\n\033[m')
    
    confirmadnvo = input('\n\033[32mDeseja realizar nova consulta? [s ou n]: \033[m')
    if confirmadnvo == 'S' or confirmadnvo == 's':
        print("\n" * os.get_terminal_size().lines)
        cabeçalho('\033[1;36m        SMARTGYM APP\033[m') 
        cabeçalho('\033[36m         Consulta Mensalidade por Data Pagamento\033[m')
        exibe_mensalidade_datapago()
        
    else:
        cabeçalho('\033[33m\n     Voltando para o menu principal\n\033[m')
        False
        sleep(1)


#Exibe por data vencimento
def exibe_mensalidade_datavence():
    if valida_cod_aluno() == True:
        dtinicio = input('\nDigite a data de inicio de intervalo de busca: ')
        dtfim = input('Digite a data fim de intervalo de busca: ')
        cur.execute("SELECT * FROM mensalidade WHERE dt_vence BETWEEN %s AND %s",(dtinicio, dtfim))
        resultado = cur.fetchall() #colocar resultados em um resultset
        for res in resultado:
            print(res)
    else:
        cabeçalho('    \033[31m\nCodigo Invalido, nao cadastrado no sistema\n\033[m')
    
    confirmadnvo = input('\n\033[32mDeseja realizar nova consulta? [s ou n]: \033[m')
    if confirmadnvo == 'S' or confirmadnvo == 's':
        print("\n" * os.get_terminal_size().lines)
        cabeçalho('\033[1;36m        SMARTGYM APP\033[m') 
        cabeçalho('\033[36m         Consulta Mensalidade por Data Vencimento\033[m')
        exibe_mensalidade_datavence()
        
    else:
        cabeçalho('\033[33m\n     Voltando para o menu principal\n\033[m')
        False
        sleep(1)

##########################################   Consulta Presenca   ###################################################

#Exibe todas as presencas
def exibe_presenca():
    cur.execute("SELECT * FROM aluno_presenca;")
    resultado = cur.fetchall() #colocar resultados em um resultset
    for res in resultado:
        print(res)
    confirmadnvo = input('\n\033[31mDeseja sair do aplicativo? [s ou n]: \033[m')
    if confirmadnvo == 'S' or confirmadnvo == 's':
        print("\n" * os.get_terminal_size().lines)
        cabeçalho('\033[1;36m\n  ENCERRANDO APLICATIVO...\n\033[m')
        quit() 
    else:
        cabeçalho('\033[33m\n     Voltando para o menu principal\n\033[m')
        False
        sleep(1)
        
#Exibe Presenca Por Aluno          
def exibe_presenca_aluno():
    if valida_cod_aluno() == True:
        cod_aluno = cod_aluno_valida
        cur.execute("SELECT * FROM aluno_presenca WHERE cod_aluno=%s;",(cod_aluno))
        resultado = cur.fetchall() #colocar resultados em um resultset
        for res in resultado:
            print(res)
    else:
        cabeçalho('Codigo do aluno invalido')
    confirmadnvo = input('\n\033[32mDeseja realizar nova consulta? [s ou n]: \033[m')
    if confirmadnvo == 'S' or confirmadnvo == 's':
        print("\n" * os.get_terminal_size().lines)
        cabeçalho('\033[1;36m        SMARTGYM APP\033[m') 
        cabeçalho('\033[36m         Consulta Presenca Aluno\033[m')
        exibe_presenca_aluno()
        
    else:
        cabeçalho('\033[33m\n     Voltando para o menu principal\n\033[m')
        False
    sleep(2)

#Exibe presencas por data 
def exibe_presenca_data(): 
    dtinicio = input('\nDigite a data de inicio de intervalo de busca: ')
    dtfim = input('Digite a data fim de intervalo de busca: ')
    cur.execute("SELECT * FROM aluno_presenca WHERE dt_presenca BETWEEN %s AND %s",(dtinicio,dtfim))
    if cur.rowcount != 0:
        resultado = cur.fetchall() #colocar resultados em um resultset
        for res in resultado:
            print(res)
    else:
        print('\n')
        cabeçalho('Nenhuma presenca cadastrada')

    confirmadnvo = input('\n\033[32mDeseja realizar nova consulta? [s ou n]: \033[m')
    if confirmadnvo == 'S' or confirmadnvo == 's':
        print("\n" * os.get_terminal_size().lines)
        cabeçalho('\033[1;36m        SMARTGYM APP\033[m') 
        cabeçalho('\033[36m         Consulta Presenca Aluno\033[m')
        exibe_presenca_data()
        
    else:
        cabeçalho('\033[33m\n     Voltando para o menu principal\n\033[m')
        False
    sleep(2)

##########################################   Consulta Acompanhamentos   ###################################################
#Consulta todos acompanhamentos
def exibe_acompanhamento():
    cur.execute("SELECT * FROM acompanhamento_aluno;")
    resultado = cur.fetchall() #colocar resultados em um resultset
    for res in resultado:
        print(res)
    confirmadnvo = input('\n\033[31mDeseja sair do aplicativo? [s ou n]: \033[m')
    if confirmadnvo == 'S' or confirmadnvo == 's':
        print("\n" * os.get_terminal_size().lines)
        cabeçalho('\033[1;36m\n  ENCERRANDO APLICATIVO...\n\033[m') 
        quit()
    else:
        cabeçalho('\033[33m\n     Voltando para o menu principal\n\033[m')
        False
        sleep(1)

#Consulta acompanhamentos por aluno
def exibe_acompanhamento_aluno():
    if valida_cod_aluno() == True:
        cod_aluno = cod_aluno_valida
        cur.execute("SELECT * FROM acompanhamento_aluno WHERE cod_aluno=%s;",(cod_aluno))
        resultado = cur.fetchall() #colocar resultados em um resultset
        for res in resultado:
            print(res)
    else:
        cabeçalho('\033[33m     Codigo aluno invalido\033[m')
        sleep(3)

    confirmadnvo = input('\n\033[32mDeseja realizar nova consulta? [s ou n]: \033[m')
    if confirmadnvo == 'S' or confirmadnvo == 's':
        print("\n" * os.get_terminal_size().lines)
        cabeçalho('\033[1;36m        SMARTGYM APP\033[m') 
        cabeçalho('\033[36m         Consulta Acompanhamento por Aluno\033[m')
        exibe_acompanhamento_aluno()
        
    else:
        cabeçalho('\033[33m\n     Voltando para o menu principal\n\033[m')
        False
    sleep(2)

#Consulta acompanhamentos por professor
def exibe_acompanhamento_prof():
    if valida_cod_prof() == True:
        cod_prof = cod_prof_valida
        cur.execute("SELECT * FROM acompanhamento_aluno WHERE cod_prof=%s;",(cod_prof))
        resultado = cur.fetchall() #colocar resultados em um resultset
        for res in resultado:
            print(res)
    else:
        cabeçalho('\033[33m     Codigo professor invalido\033[m')
        sleep(3)

    confirmadnvo = input('\n\033[32mDeseja realizar nova consulta? [s ou n]: \033[m')
    if confirmadnvo == 'S' or confirmadnvo == 's':
        print("\n" * os.get_terminal_size().lines)
        cabeçalho('\033[1;36m        SMARTGYM APP\033[m') 
        cabeçalho('\033[36m         Consulta Acompanhamento por Professor\033[m')
        exibe_acompanhamento_prof()
        
    else:
        cabeçalho('\033[33m\n     Voltando para o menu principal\n\033[m')
        False
    sleep(2)

##########################################   Validações   ###################################################

#Valida CPF Aluno
def valida_cpf_aluno():
            global cpf_aluno_valida
            cpf_aluno_valida = input('\033[32mDigite o CPF do Aluno: \033[m')
            cur.execute("SELECT cpf_aluno FROM aluno WHERE cpf_aluno=%s;",(cpf_aluno_valida, ))
            if cur.rowcount == 1:
                return True
            else:
                return False

#Valida COD Acomp
def valida_cod_acomp():
            global cod_acomp_valida 
            cod_acomp_valida = input('\033[32mDigite o CODIGO do Acompanhamento: \033[m')
            cur.execute("SELECT cod_acomp FROM acompanhamento_aluno WHERE cod_acomp=%s;",(cod_acomp_valida, ))
            if cur.rowcount == 1:
                return True
            else:
                return False

#Valida COD Aluno
def valida_cod_aluno():
            global cod_aluno_valida
            cod_aluno_valida = input('\033[32mDigite o CODIGO do Aluno: \033[m')
            cur.execute("SELECT cod_aluno FROM aluno WHERE cod_aluno=%s;",(cod_aluno_valida, ))
            if cur.rowcount == 1:
                return True
            else:
                return False


#Valida CPF Professor
def valida_cpf_prof():
            global cpf_prof_pego
            cpf_prof_pego = int(input('\033[32mDigite o CPF do Professor: \033[m'))
            cur.execute("SELECT cpf_prof FROM professor WHERE cpf_prof=%s;",(cpf_prof_pego, ))
            if cur.rowcount == 1:
                return True               
            else:
                return False

#Valida Codigo Prof
def valida_cod_prof():
            global cod_prof_valida
            cod_prof_valida = input('\033[32mDigite o CODIGO do Professor: \033[m')
            cur.execute("SELECT cod_prof FROM professor WHERE cod_prof=%s;",(cod_prof_valida, ))
            if cur.rowcount == 1:
                return True
            else:
                return False

#Valida Codigo Treino
def valida_treino():
            global cod_treino_valida
            cod_treino_valida = input('\033[32mDigite o código do treino que deseja realizar a operacao: \033[m')
            cur.execute("SELECT cod_treino FROM treino WHERE cod_treino=%s;",(cod_treino_valida, ))
            if cur.rowcount == 1:
                return True
            else:
                return False

#Valida Codigo Plano
def valida_plano():
            global cod_plano_valida
            cod_plano_valida = input('\033[32mDigite o código do plano que deseja realizar a operacao: \033[m')
            cur.execute("SELECT cod_plano FROM plano WHERE cod_plano=%s;",(cod_plano_valida, ))
            if cur.rowcount == 1:
                return True
            else:
                return False

#Valida Codigo Mensalidade
def valida_mensalidade():
            global cod_mensalidade_valida
            cod_mensalidade_valida = input('\033[32mDigite o código da mensalidade que deseja realizar a operacao: \033[m')
            cur.execute("SELECT cod_mensalidade FROM mensalidade WHERE cod_mensalidade=%s;",(cod_mensalidade_valida, ))
            if cur.rowcount == 1:
                return True
            else:
                return False


##########################################   ATUALIZAR DADOS ALUNO   ###################################################

#Atualizar dados Aluno por codigo
def atualiza_aluno(novovalor_aluno):
    if valida_cod_aluno() == True:
        print('\n\033[36mCampo a ser alterado: \033[m',novovalor_aluno)
        valoratualiza = input('\033[36mDigite o novo valor a ser atualizado: \033[m')
        cur.execute("UPDATE aluno SET "+novovalor_aluno+" = %s WHERE cod_aluno = %s",(valoratualiza, cod_aluno_valida))
        confirma = input('\n\33[32mDeseja confirmar a atualizacao? [s ou n]: \033[m')
        if confirma == 'S' or confirma == 's':
            conn.commit()
            print('\033[32m\nCampo> ',novovalor_aluno,', foi atualizado com sucesso\033[m')
            False
        else:
            conn.rollback()
            print('\033[33m\nCampo> ',novovalor_aluno,', não atualizado\033[m')
            True
    else:
        cabeçalho('\033[33m Codigo Aluno invalido')
        sleep(3)
    denovo = input('\nDeseja realizar uma nova atualizacao? [s ou n]: ')
    if denovo == 's' or denovo =='S':
        print("\n" * os.get_terminal_size().lines)
        cabeçalho('\033[1;36m        SMARTGYM APP\033[m') 
        cabeçalho('\033[36m         Atualizar Aluno\033[m')
        atualiza_aluno(novovalor_aluno)
    else:
        print('\n')
        cabeçalho('\033[33m\n     Voltando para o menu principal\n\033[m')
        False
        sleep(1)

#Atualizar dados Aluno por CPF
def atualiza_aluno_cpf(novovalor_aluno):
    if valida_cpf_aluno() == True:
        print('\n\033[36mCampo a ser alterado: \033[m',novovalor_aluno)
        valoratualiza = input('\033[36mDigite o novo valor a ser atualizado: \033[m')
        cur.execute("UPDATE aluno SET "+novovalor_aluno+" = %s WHERE cpf_aluno = %s",(valoratualiza, cpf_aluno_valida))
        confirma = input('\n\33[32mDeseja confirmar a atualizacao? [s ou n]: \033[m')
        if confirma == 'S' or confirma == 's':
            conn.commit()
            print('\033[32m\nCampo> ',novovalor_aluno,', foi atualizado com sucesso\033[m')
            False
        else:
            conn.rollback()
            print('\033[33m\nCampo> ',novovalor_aluno,', não atualizado\033[m')
            True
    else:
        cabeçalho('\033[33m Codigo Aluno invalido')
        sleep(3)
    denovo = input('\nDeseja realizar uma nova atualizacao? [s ou n]: ')
    if denovo == 's' or denovo =='S':
        print("\n" * os.get_terminal_size().lines)
        cabeçalho('\033[1;36m        SMARTGYM APP\033[m') 
        cabeçalho('\033[36m         Atualizar Aluno\033[m')
        atualiza_aluno_cpf(novovalor_aluno)
    else:
        print('\n')
        cabeçalho('\033[33m\n     Voltando para o menu principal\n\033[m')
        False
        sleep(1)


##########################################   ATUALIZAR DADOS Professor   ###################################################

#Atualizar dados Professor por cpf
def atualiza_prof_cpf(novovalor_prof):
    if valida_cpf_prof() == True:
        print('\n\033[36mCampo a ser alterado: \033[m',novovalor_prof)
        valoratualiza = input('\033[36mDigite o novo valor a ser atualizado: \033[m')
        cur.execute("UPDATE professor SET "+novovalor_prof+" = %s WHERE cpf_prof = %s",(valoratualiza, cpf_prof_pego))
        confirma = input('\n\33[32mDeseja confirmar a atualizacao? [s ou n]: \033[m')
        if confirma == 'S' or confirma == 's':
            conn.commit()
            print('\033[32m\nCampo>',novovalor_prof,', foi atualizado com sucesso\033[m')
            False
        else:
            conn.rollback()
            print('\033[33m\nCampo>',novovalor_prof,', não atualizado\033[m')
            True
    else:
        cabeçalho('\033[33m Codigo Professor invalido')
        sleep(3)
    denovo = input('\nDeseja realizar uma nova atualizacao? [s ou n]: ')
    if denovo == 's' or denovo =='S':
        print("\n" * os.get_terminal_size().lines)
        cabeçalho('\033[1;36m        SMARTGYM APP\033[m') 
        cabeçalho('\033[36m         Atualizar Professor\033[m')
        atualiza_prof_cpf(novovalor_prof)
    else:
        print('\n')
        cabeçalho('\033[33m\n     Voltando para o menu principal\n\033[m')
        False


#Atualizar dados Professor por codigo
def atualiza_prof(novovalor_prof):
    if valida_cod_prof() == True:
        print('\n\033[36mCampo a ser alterado: \033[m',novovalor_prof)
        valoratualiza = input('\033[36mDigite o novo valor a ser atualizado: \033[m')
        cur.execute("UPDATE professor SET "+novovalor_prof+" = %s WHERE cod_prof = %s",(valoratualiza, cod_prof_valida))
        confirma = input('\n\33[32mDeseja confirmar a atualizacao? [s ou n]: \033[m')
        if confirma == 'S' or confirma == 's':
            conn.commit()
            print('\033[32m\nCampo>',novovalor_prof,', foi atualizado com sucesso\033[m')
            False
        else:
            conn.rollback()
            print('\033[33m\nCampo>',novovalor_prof,', não atualizado\033[m')
            True
    else:
        cabeçalho('\033[33m Codigo Professor invalido')
        sleep(3)
    denovo = input('\nDeseja realizar uma nova atualizacao? [s ou n]: ')
    if denovo == 's' or denovo =='S':
        print("\n" * os.get_terminal_size().lines)
        cabeçalho('\033[1;36m        SMARTGYM APP\033[m') 
        cabeçalho('\033[36m         Atualizar Professor\033[m')
        atualiza_prof(novovalor_prof)
    else:
        print('\n')
        cabeçalho('\033[33m\n     Voltando para o menu principal\n\033[m')
        False


##########################################   ATUALIZAR DADOS Treino   ###################################################

#Atualizar dados Treino
def atualiza_treino(novovalor_treino):
    if valida_treino() == True:
        print('\n\033[36mCampo a ser alterado: \033[m',novovalor_treino)
        valoratualiza = input('\033[36mDigite o novo valor a ser atualizado: \033[m')
        cur.execute("UPDATE treino SET "+novovalor_treino+" = %s WHERE cod_treino = %s",(valoratualiza, cod_treino_valida))
        confirma = input('\n\33[32mDeseja confirmar a atualizacao? [s ou n]: \033[m')
        if confirma == 'S' or confirma == 's':
            conn.commit()
            print('\033[32m\nCampo>',novovalor_treino,', foi atualizado com sucesso\033[m')
            False
        else:
            conn.rollback()
            print('\033[33m\nCampo>',novovalor_treino,', não atualizado\033[m')
            True
    else:
        cabeçalho('\033[33m Codigo Professor invalido')
        sleep(3)
    denovo = input('\nDeseja realizar uma nova atualizacao? [s ou n]: ')
    if denovo == 's' or denovo =='S':
        print("\n" * os.get_terminal_size().lines)
        cabeçalho('\033[1;36m        SMARTGYM APP\033[m') 
        cabeçalho('\033[36m         Atualizar Professor\033[m')
        atualiza_treino(novovalor_treino)
    else:
        print('\n')
        cabeçalho('\033[33m\n     Voltando para o menu principal\n\033[m')
        False


##########################################   ATUALIZAR DADOS Plano   ###################################################

#Atualizar dado Desconto Plano
def atualiza_plano_desconto():
    if valida_plano() == True:
        valoratualiza = input('Digite o novo desconto, ex: 0.10 para 10%: ')
        cur.execute("UPDATE plano SET desconto_plano=%s WHERE cod_plano=%s",(valoratualiza, cod_plano_valida))
    else:
        cabeçalho('\033[33mPlano invalido')
        sleep(3)
        


##########################################   ATUALIZAR DADOS MATRICULA   ###################################################
#Atualizar dado Matricula Status
def atualiza_matricula_status(cod_aluno, valoratualiza):
    cur.execute("UPDATE matricula SET status_matricula=%s WHERE cod_aluno=%s",(valoratualiza, cod_aluno))

def atualiza_matricula_status_plano(cod_aluno, valoratualiza):
    cur.execute("UPDATE matricula SET status_plano=%s WHERE cod_aluno=%s",(valoratualiza, cod_aluno))

##########################################   ATUALIZAR DADOS MENSALIDADE   ###################################################
#Atualizar dados Mensalidade
def atualiza_mensalidade(novovalor_mensalidade):
    if valida_mensalidade() == True:
        print('\n\033[36mCampo a ser alterado: \033[m',novovalor_mensalidade)
        valoratualiza = input('\033[36mDigite o novo valor a ser atualizado: \033[m')
        cur.execute("UPDATE mensalidade SET "+novovalor_mensalidade+" = %s WHERE cod_mensalidade = %s",(valoratualiza, cod_mensalidade_valida))
        confirma = input('\n\33[32mDeseja confirmar a atualizacao? [s ou n]: \033[m')
        if confirma == 'S' or confirma == 's':
            conn.commit()
            print('\033[32m\nCampo>',novovalor_mensalidade,', foi atualizado com sucesso\033[m')
            False
        else:
            conn.rollback()
            print('\033[33m\nCampo>',novovalor_mensalidade,', não atualizado\033[m')
            True
    else:
        cabeçalho('\033[31m   Codigo Mensalidade invalido')
        sleep(3)
    denovo = input('\nDeseja realizar uma nova atualizacao? [s ou n]: ')
    if denovo == 's' or denovo =='S':
        print("\n" * os.get_terminal_size().lines)
        cabeçalho('\033[1;36m        SMARTGYM APP\033[m') 
        cabeçalho('\033[36m         Atualizar Mensalidade\033[m')
        atualiza_mensalidade(novovalor_mensalidade)
    else:
        print('\n')
        cabeçalho('\033[33m\n     Voltando para o menu principal\n\033[m')
        False

##########################################   ATUALIZAR DADOS Acompanhamento Aluno   ###################################################

#Atualizar dados acompanhamento
def atualiza_acomp(novovalor_acomp):
    if valida_cod_acomp() == True:
        print('\n\033[36mCampo a ser alterado: \033[m',novovalor_acomp)
        valoratualiza = input('\033[36mDigite o novo valor a ser atualizado: \033[m')
        cur.execute("UPDATE acompanhamento_aluno SET "+novovalor_acomp+" = %s WHERE cod_acomp = %s",(valoratualiza, cod_acomp_valida))
        confirma = input('\n\33[32mDeseja confirmar a atualizacao? [s ou n]: \033[m')
        if confirma == 'S' or confirma == 's':
            conn.commit()
            print('\033[36m\nCampo> ',novovalor_acomp,', do acompanhamento do aluno foi atualizado com sucesso\033[m')
            False
        else:
            conn.rollback()
            print('\033[36m\nCampo> ',novovalor_acomp,', do acompanhamento do aluno não atualizado\033[m')
            True
    else:
        cabeçalho('Codigo de acompanhamento invalido')
        sleep(3)

##########################################   Estetica   ###################################################

#Ler opção e mostrar erros
def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):       
            print('\033[31mErro: por favor, digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n

#Tamanho da moldura
def linha(tam = 42):
    return '-' * tam

#Cabeçalho
def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

#Menu
def menu(lista):
    c=1
    for item in lista:
        print(f'\033[33m{c} - {item}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('\033[37mSua Opção: \033[m')
    return opc
