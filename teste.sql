-- This script was generated by a beta version of the ERD tool in pgAdmin 4.
-- Please log an issue at https://redmine.postgresql.org/projects/pgadmin4/issues/new if you find any bugs, including reproduction steps.
BEGIN;


CREATE TABLE IF NOT EXISTS public.aluno
(
    cpf_aluno numeric(11) NOT NULL,
    nome_aluno character varying(100) NOT NULL,
    sexo_aluno "char" NOT NULL,
    dtnasc_aluno date NOT NULL,
    rg_aluno character varying(9) NOT NULL,
    contato_aluno numeric(11) NOT NULL,
    cep_aluno numeric(8) NOT NULL,
    endereco_aluno character varying(100) NOT NULL,
    endereco_nmr_aluno numeric(9) NOT NULL,
    cod_aluno serial NOT NULL,
    PRIMARY KEY (cod_aluno),
    UNIQUE (rg_aluno, cpf_aluno)
);

COMMENT ON TABLE public.aluno
    IS 'Alunos da academia';

CREATE TABLE IF NOT EXISTS public.aluno_presenca
(
    cod_aluno integer NOT NULL,
    dt_presenca date NOT NULL,
    hr_presenca time with time zone NOT NULL,
    hrsaida_presenca time with time zone,
    status_presenca boolean
);

CREATE TABLE IF NOT EXISTS public.plano
(
    cod_plano smallserial NOT NULL,
    desc_plano character varying(150) NOT NULL,
    qt_meses integer NOT NULL,
    desconto_plano numeric(3, 2) NOT NULL,
    status_plano boolean NOT NULL,
    PRIMARY KEY (cod_plano)
);

COMMENT ON TABLE public.plano
    IS 'Tabela onde está os Planos (Mensal, Trimestral, Semestral, Anual)';

CREATE TABLE IF NOT EXISTS public.aluno_plano
(
    cod_matricula serial NOT NULL,
    dt_matricula date NOT NULL,
    cod_plano integer,
    cod_aluno integer,
    status_aluno_plano boolean NOT NULL,
    fim_plano date,
    valor_mens numeric(5, 2) NOT NULL,
    valor_matricula numeric(5, 2),
    PRIMARY KEY (cod_matricula, cod_aluno, cod_plano)
);

COMMENT ON TABLE public.aluno_plano
    IS 'Tabela da Matricula do aluno';

CREATE TABLE IF NOT EXISTS public.mensalidade
(
    cod_mensalidade serial NOT NULL,
    valor_mensalidade numeric(5, 2) NOT NULL,
    dt_pago date,
    dt_vence date,
    status_mensalidade boolean NOT NULL,
    cod_aluno integer NOT NULL,
    cod_matricula integer NOT NULL,
    PRIMARY KEY (cod_mensalidade)
);

COMMENT ON TABLE public.mensalidade
    IS 'Mensalidade do aluno';

CREATE TABLE IF NOT EXISTS public.treino
(
    cod_treino serial NOT NULL,
    atividade_treino character varying(100) NOT NULL,
    serie_treino numeric(2) NOT NULL,
    intervalo_treino numeric(3) NOT NULL,
    repeticao_treino numeric(2) NOT NULL,
    cod_aluno integer NOT NULL,
    dtinicio_treino date,
    dtfim_treino date,
    status_treino character varying(15),
    cod_prof integer NOT NULL,
    objetivo_treino character varying(100) NOT NULL,
    tempo_treino time without time zone,
    PRIMARY KEY (cod_treino)
);

COMMENT ON TABLE public.treino
    IS 'Treinos recomendados para o aluno';

CREATE TABLE IF NOT EXISTS public.acompanhamento_aluno
(
    cod_acomp serial NOT NULL,
    data_acomp date NOT NULL,
    peso numeric(5, 2) NOT NULL,
    altura numeric(3, 2) NOT NULL,
    massamagra numeric(5, 2),
    perc_gordura numeric(3, 2),
    med_braco numeric(5, 2),
    med_ante numeric(5, 2),
    med_peito numeric(5, 2),
    med_quadris numeric(5, 2),
    med_cintura numeric(5, 2),
    med_panturrilha numeric(5, 2),
    cod_aluno integer NOT NULL,
    cod_prof integer NOT NULL,
    PRIMARY KEY (cod_acomp)
);

COMMENT ON TABLE public.acompanhamento_aluno
    IS 'Tabela do Acompanhamento físico do Aluno';

CREATE TABLE IF NOT EXISTS public.professor
(
    cpf_prof numeric(11) NOT NULL,
    nome_prof character varying(100) NOT NULL,
    rg_prof character varying(9) NOT NULL,
    especializacao character varying(50) NOT NULL,
    contato_prof numeric(11) NOT NULL,
    hr_entrada_prof time(5) without time zone NOT NULL,
    hr_saida_prof time(5) without time zone NOT NULL,
    cep_prof numeric(8),
    endereco_prof character varying(100),
    endereco_nmr_prof numeric(9) NOT NULL,
    sexo_prof "char",
    dtnasc_prof date NOT NULL,
    cod_prof serial NOT NULL,
    PRIMARY KEY (cod_prof),
    UNIQUE (rg_prof)
);

COMMENT ON TABLE public.professor
    IS 'Tabela dos professores ou treinadores da academia';

ALTER TABLE IF EXISTS public.aluno_presenca
    ADD FOREIGN KEY (cod_aluno)
    REFERENCES public.aluno (cod_aluno) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


ALTER TABLE IF EXISTS public.aluno_plano
    ADD FOREIGN KEY (cod_plano)
    REFERENCES public.plano (cod_plano) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


ALTER TABLE IF EXISTS public.aluno_plano
    ADD FOREIGN KEY (cod_aluno)
    REFERENCES public.aluno (cod_aluno) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


ALTER TABLE IF EXISTS public.mensalidade
    ADD FOREIGN KEY (cod_aluno)
    REFERENCES public.aluno (cod_aluno) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


ALTER TABLE IF EXISTS public.mensalidade
    ADD FOREIGN KEY (cod_matricula)
    REFERENCES public.aluno_plano (cod_matricula) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


ALTER TABLE IF EXISTS public.treino
    ADD FOREIGN KEY (cod_prof)
    REFERENCES public.professor (cod_prof) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


ALTER TABLE IF EXISTS public.treino
    ADD FOREIGN KEY (cod_aluno)
    REFERENCES public.aluno (cod_aluno) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


ALTER TABLE IF EXISTS public.acompanhamento_aluno
    ADD FOREIGN KEY (cod_aluno)
    REFERENCES public.aluno (cod_aluno) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


ALTER TABLE IF EXISTS public.acompanhamento_aluno
    ADD FOREIGN KEY (cod_prof)
    REFERENCES public.professor (cod_prof) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;

END;