-- gerador de cpf https://www.4devs.com.br/gerador_de_cpf
-- gerador nomes https://thestoryshack.com/pt/geradores/gerador-de-nomes-brasileiros/
-- gerador rg https://geradornv.com.br/gerador-rg-sp/
-- gerador cep https://www.4devs.com.br/gerador_de_cep
-- gerador celular https://pt.calcprofi.com/gerador-de-numeros-de-telefone-aleatorio.html
-- para gerar contato > codigo do pais nao , destino > 119 > Sem Separador > Numero que quiser
-- gerador datanasc https://www.freetool.dev/pt/gerador-data-nascimento

--Populando tabela Alunos
INSERT INTO aluno VALUES ('80357965000','Alvaro Leal','M','07/03/1961','203345836','11925401524','05594170','Rua Vereador Cid Galvão da Silva','420',DEFAULT);
INSERT INTO aluno VALUES ('77424420003','Pedro Camargo','M','05/09/1980','296777808','11997466764','02995200','Rua Samuel das Neves','8119',DEFAULT);
INSERT INTO aluno VALUES ('16568776009','Rafael Paz','M','04/07/2000','385226421','11971597881','03804160','Rua João Felipe Corrêa Lisboa','1017',DEFAULT);
INSERT INTO aluno VALUES ('56454259013','Reginaldo Furtado','M','16/09/1965','330849591','11934216867','04774000','Rua Álvaro de Brito Alambert','459',DEFAULT);
INSERT INTO aluno VALUES ('65487627037','Ronaldo Salgado','M','18/10/2003','143584960','11919488234','05029050','Rua Plácido Leão','221',DEFAULT);
INSERT INTO aluno VALUES ('83082315003','Paola Brandao','F','10/12/1982','15346883X','11900498558','05029050','Rua José Torres Lima','185',DEFAULT);
INSERT INTO aluno VALUES ('83082315003','Carolina Antunes','F','03/10/1993','370172115','11936469891','03444030','Rua José Torres Lima','144',DEFAULT);
INSERT INTO aluno VALUES ('61534242015','Michele Flores','F','16/02/1987','468720157','11977289138','08223365','Rua Valéria','56',DEFAULT);
INSERT INTO aluno VALUES ('82642925005','Debora Dutra','F','20/02/1970','18430412X','11951452591','02083055','Travessa Jean de Leri','314',DEFAULT);


--Populando tabela Professores
INSERT INTO professor VALUES ('77021902808','Cristiano Meireles','322477116','Educacao fisica, fisioculturista','11939286008','08:00','16:00','69022107','Rua Ramiro Santos','111','M','11/02/1990',DEFAULT);
INSERT INTO professor VALUES ('85952998895','Geraldo Correia','378624295','Educacao fisica, nutricionismo','11903680955','08:00','15:00','02735010','Rua Ameliópolis','54','M','04/06/1981',DEFAULT);
INSERT INTO professor VALUES ('85952998895','Igor Sato','390484593','Natacao e musuculacao','11971589431','15:00','21:00','05011000','Rua Wanderley','554','M','11/02/1994',DEFAULT);
INSERT INTO professor VALUES ('85952998895','Solange Almeida','148346273','Professora educacao fisica','11954517446','15:00','21:00','08382330','Travessa Rebouças da Costa','621','F','08/04/1986',DEFAULT);


-- Serie = Serie 3(vezes)   //  Intervalo em segundos // Repeticao = repeticao da serie . EX: 20 Repeticoes  ou  em minutos 10, caso necessite de tempo//  Objetivo = Descricao ou objetivo (opcional), Tempo_treino = Tempo estimado treino (opcional)
--Populando tabela Treino
INSERT INTO treino VALUES (DEFAULT,'Flexao','3','120','20','1','14/01/2022','15/04/2022','FINALIZADO','1','Treinar Peito','0:20');
INSERT INTO treino VALUES (DEFAULT,'Flexao','4','60','25','2','14/11/2022','15/01/2023','EM ANDAMENTO','2','Treinar Peito, diversificar as 4 series','0:30');
INSERT INTO treino VALUES (DEFAULT,'Flexao','3','120','20','1','15/01/2023','15/04/2023','NAO COMECOU','3','Treinar Peito','0:23');
INSERT INTO treino VALUES (DEFAULT,'Abdominal','3','120','20','4','14/10/2022','15/12/2022','EM ANDAMENTO','4','Treinar Abdmomem, diversificar as tres series','0:20');
INSERT INTO treino VALUES (DEFAULT,'Agaxamento','3','120','20','5','14/11/2022','15/04/2023','EM ANDAMENTO','4','Treinar pernas e coxas','0:20');
INSERT INTO treino VALUES (DEFAULT,'Agaxamento com peso de 20kg','3','120','20','1','14/09/2022','15/02/2023','EM ANDAMENTO','1','Treinar pernas e coxas','0:20');
INSERT INTO treino VALUES (DEFAULT,'Esteira','2','120','12','6','14/04/2022','15/04/2023','EM ANDAMENTO','2','Velocidade: 2','0:30');
INSERT INTO treino VALUES (DEFAULT,'Esteira','3','120','15','1','14/04/2022','15/11/2022','FINALIZADO','1','Velocidade: 4','0:40');

-- https://endocrinologiaesportiva.com.br/medidas-e-proporcoes-do-corpo-masculino-perfeito/  =  Para ter noção dos valores
--Populando Acompanhamento aluno
INSERT INTO acompanhamento_aluno VALUES (DEFAULT,'15/11/2022','89','1.81','71.7','0.24','39.2','31.6','109.2','84.1','72.1','35.4','1','1');
INSERT INTO acompanhamento_aluno VALUES (DEFAULT,'15/11/2022','80','1.88','72.2','0.21','35.2','30.1','105.2','80.2','70.5','33.2','2','1');
INSERT INTO acompanhamento_aluno VALUES (DEFAULT,'15/11/2022','76','1.71','62.2','0.23','32.2','28.6','100.2','72.9','69.8','31.8','3','2');


--Populando Aluno_Preseça
INSERT INTO aluno_presenca VALUES ('1','15/11/2022','09:00','11:00');
INSERT INTO aluno_presenca VALUES ('2','15/11/2022','08:00','10:00');
INSERT INTO aluno_presenca VALUES ('3','15/11/2022','11:00','12:00');
INSERT INTO aluno_presenca VALUES ('4','15/11/2022','13:00','14:00');


--Populando Planos
INSERT INTO plano VALUES(default,'MENSAL','1','0');
INSERT INTO plano VALUES(default,'BIMESTRAL','2','0.05');
INSERT INTO plano VALUES(default,'TRIMESTRAL','3','0.10');
INSERT INTO plano VALUES(default,'SEMESTRAL','6','0.20');
INSERT INTO plano VALUES(default,'ANUAL','12','0.30');
