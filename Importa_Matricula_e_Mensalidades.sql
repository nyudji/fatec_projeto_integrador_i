--Importa Mensalidade (FROM C:/TEMP/nomedo.csv), caminho onde salvar o csv exportado 
copy mensalidade(cod_mensalidade, valor_mensalidade, dt_pago, dt_vence, status_mensalidade, cod_aluno) FROM 'c:/temp/mensalidade_smart.csv' WITH DELIMITER ';' CSV HEADER;
-- Importa Matricula
copy matricula(cod_matricula, dt_matricula, status_matricula, cod_plano, cod_aluno, status_plano, fim_plano) FROM 'c:/temp/matricula_smart.csv' WITH DELIMITER ';' CSV HEADER;
