-- Criar a tabela "Cursos"
DO $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM pg_catalog.pg_class WHERE relname = 'cursos') THEN
        CREATE TABLE Cursos (
            id_curso BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
            nome_curso TEXT NOT NULL,
            descricao_curso TEXT,
            duracao TEXT,
            categoria TEXT,
            nivel TEXT,
            carga_horaria INTEGER,
            data_inicio DATE,
            data_fim DATE,
            "createdAt" DATE,
            "updatedAt" DATE
        );
    END IF;
END $$;

-- Criar a tabela "Materias"
DO $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM pg_catalog.pg_class WHERE relname = 'materias') THEN
        CREATE TABLE Materias (
            id_materia BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
            nome_materia TEXT NOT NULL,
            professor_materia TEXT NOT NULL,
            objetivo TEXT,
            ementa TEXT,
            carga_horaria INTEGER,
            "createdAt" DATE,
            "updatedAt" DATE,
            id_curso BIGINT REFERENCES Cursos(id_curso) ON DELETE CASCADE
        );
    END IF;
END $$;

-- Criar a tabela "Turmas"
DO $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM pg_catalog.pg_class WHERE relname = 'turmas') THEN
        CREATE TABLE Turmas (
            id_turma BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
            nome_turma TEXT NOT NULL,
            ano_letivo TEXT NOT NULL,
            id_curso BIGINT REFERENCES Cursos(id_curso) ON DELETE SET NULL,
            horario TEXT,
            sala TEXT,
            professor_responsavel TEXT,
            capacidade_maxima INTEGER,
            "createdAt" DATE,
            "updatedAt" DATE
        );
    END IF;
END $$;

-- Criar a tabela "Alunos"
DO $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM pg_catalog.pg_class WHERE relname = 'alunos') THEN
        CREATE TABLE Alunos (
            id_aluno BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
            nome_completo TEXT NOT NULL,
            "RA" BIGINT NOT NULL,
            senha TEXT NOT NULL,
            data_nascimento DATE,
            genero TEXT,
            endereco TEXT,
            email TEXT,
            telefone TEXT,
            documento_identidade TEXT,
            cpf TEXT,
            data_matricula DATE,
            numero_matricula TEXT,
            "createdAt" DATE,
            "updatedAt" DATE,
            caminho_da_foto TEXT,
            id_curso BIGINT REFERENCES Cursos(id_curso) ON DELETE SET NULL,
            id_turma BIGINT REFERENCES Turmas(id_turma) ON DELETE SET NULL
        );
    END IF;
END $$;

-- Criar a tabela "Alunos_Materias"
DO $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM pg_catalog.pg_class WHERE relname = 'alunos_materias') THEN
        CREATE TABLE Alunos_Materias (
            id_aluno BIGINT REFERENCES Alunos(id_aluno) ON DELETE CASCADE,
            id_materia BIGINT REFERENCES Materias(id_materia) ON DELETE CASCADE,
            PRIMARY KEY (id_aluno, id_materia)
        );
    END IF;
END $$;

-- Criar a tabela "Usuarios"
DO $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM pg_catalog.pg_class WHERE relname = 'usuarios') THEN
        CREATE TABLE Usuarios (
            id_usuario BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
            nome_completo TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            senha BYTEA NOT NULL,
            tipo_usuario TEXT CHECK (tipo_usuario IN ('Professor', 'Secretaria', 'Administrador')) NOT NULL,
            data_criacao TIMESTAMP DEFAULT NOW(),
            status TEXT NOT NULL,
            area_atuacao TEXT,
            setor TEXT,
            data_contratacao DATE,
            "createdAt" DATE,
            "updatedAt" DATE,
            caminho_da_foto TEXT
        );
    END IF;
END $$;


-- Criar a tabela "Permissoes"
DO $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM pg_catalog.pg_class WHERE relname = 'permissoes') THEN
        CREATE TABLE Permissoes (
            id_permissao BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
            nome_permissao TEXT NOT NULL,
            descricao_permissao TEXT
        );
    END IF;
END $$;

-- Criar a tabela "Roles"
DO $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM pg_catalog.pg_class WHERE relname = 'roles') THEN
        CREATE TABLE Roles (
            id_role BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
            id_usuario BIGINT REFERENCES Usuarios(id_usuario) ON DELETE CASCADE,
            id_permissao BIGINT REFERENCES Permissoes(id_permissao) ON DELETE CASCADE
        );
    END IF;
END $$;

CREATE ROLE user_reading_create
WITH LOGIN
PASSWORD 'userreadingcreate';

GRANT SELECT ON ALL TABLES IN SCHEMA public TO user_reading_create;
GRANT INSERT ON ALL TABLES IN SCHEMA public TO user_reading_create;

CREATE ROLE user_all
WITH LOGIN
PASSWORD 'userall';

GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO user_all;

ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO user_all;


ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT SELECT, INSERT ON TABLES TO user_reading_create;


INSERT INTO Cursos (nome_curso, descricao_curso, duracao, categoria, nivel, carga_horaria, data_inicio, data_fim, "createdAt")
VALUES 
('Engenharia de Software', 'Curso de desenvolvimento de sistemas', '4 anos', 'Tecnologia', 'Graduação', 3600, '2022-01-15', '2026-12-15', NOW()),
('Administração', 'Curso de gestão e negócios', '4 anos', 'Negócios', 'Graduação', 3200, '2022-01-15', '2026-12-15', NOW()),
('Design Gráfico', 'Curso de design e comunicação visual', '2 anos', 'Artes', 'Tecnólogo', 1600, '2022-01-15', '2024-12-15', NOW()),
('Ciência da Computação', 'Curso voltado à computação e algoritmos', '4 anos', 'Tecnologia', 'Graduação', 4000, '2022-01-15', '2026-12-15', NOW());

INSERT INTO Turmas (nome_turma, ano_letivo, id_curso, horario, sala, professor_responsavel, capacidade_maxima, "createdAt")
VALUES
('ES-2023-1', '2023', 1, '19:00-22:00', 'A101', 'Prof. João Silva', 40, NOW()),
('ADM-2023-1', '2023', 2, '08:00-12:00', 'B202', 'Prof. Carlos Souza', 30, NOW()),
('DG-2023-1', '2023', 3, '14:00-18:00', 'C303', 'Prof. Marta Lima', 25, NOW()),
('CC-2023-1', '2023', 4, '19:00-22:00', 'D404', 'Prof. Ana Ribeiro', 35, NOW()),
('ES-2024-1', '2024', 1, '19:00-22:00', 'A102', 'Prof. João Silva', 40, NOW()),
('ADM-2024-1', '2024', 2, '08:00-12:00', 'B203', 'Prof. Carlos Souza', 30, NOW()),
('DG-2024-1', '2024', 3, '14:00-18:00', 'C304', 'Prof. Marta Lima', 25, NOW()),
('CC-2024-1', '2024', 4, '19:00-22:00', 'D405', 'Prof. Ana Ribeiro', 35, NOW());


INSERT INTO Materias (nome_materia, professor_materia, objetivo, ementa, carga_horaria, id_curso, "createdAt")
VALUES
('Algoritmos e Programação', 'Prof. João Silva', 'Ensinar a lógica de programação', 'Introdução à lógica, estrutura de dados', 80, 1, NOW()),
('Banco de Dados', 'Prof. João Silva', 'Gerenciamento de dados', 'Modelagem e administração de bancos de dados relacionais e não relacionais', 80, 1, NOW()),
('Engenharia de Software', 'Prof. João Silva', 'Estudo de processos de engenharia de software', 'Metodologias de desenvolvimento de software', 80, 1, NOW()),
('Arquitetura de Computadores', 'Prof. Ana Ribeiro', 'Funcionamento de hardwares', 'Estudo de processadores, memórias e componentes de hardware', 100, 1, NOW()),
('Sistemas Operacionais', 'Prof. João Silva', 'Estudo dos sistemas operacionais', 'Gerenciamento de processos, memória, e sistemas de arquivos', 80, 1, NOW()),
('Gestão de Projetos', 'Prof. Carlos Souza', 'Gestão de equipes e projetos', 'Introdução a metodologias de gestão de projetos como Scrum, Kanban', 60, 2, NOW()),
('Contabilidade Empresarial', 'Prof. Carlos Souza', 'Entender a contabilidade', 'Gestão de finanças e contabilidade corporativa', 60, 2, NOW()),
('Recursos Humanos', 'Prof. Laura Mendes', 'Gestão de pessoas', 'Estudo das práticas de recrutamento, seleção, treinamento e desenvolvimento', 60, 2, NOW()),
('Marketing Digital', 'Prof. Júlia Prado', 'Introdução ao marketing', 'Planejamento de campanhas digitais e estratégias de marketing nas redes sociais', 60, 2, NOW()),
('Planejamento Estratégico', 'Prof. Carlos Souza', 'Estudo de planejamento e estratégias empresariais', 'Desenvolvimento de planejamento estratégico empresarial', 60, 2, NOW()),
('Tipografia', 'Prof. Marta Lima', 'Desenvolver habilidades em tipografia', 'História da tipografia, design gráfico e o uso de fontes', 60, 3, NOW()),
('Desenho Digital', 'Prof. Marta Lima', 'Técnicas de desenho digital', 'Ferramentas de design como Adobe Illustrator e Photoshop', 60, 3, NOW()),
('Design de Interfaces', 'Prof. Eduardo Pereira', 'Criação de interfaces digitais', 'Estudo de UX e UI design para aplicativos e websites', 60, 3, NOW()),
('Produção Audiovisual', 'Prof. Mariana Silva', 'Criação de conteúdos audiovisuais', 'Edição de vídeos e áudios com ferramentas como Premiere e After Effects', 60, 3, NOW()),
('Ilustração Digital', 'Prof. Marta Lima', 'Habilidades em ilustração digital', 'Técnicas avançadas de ilustração digital e pintura', 60, 3, NOW()),
('Inteligência Artificial', 'Prof. Ana Ribeiro', 'Introdução à IA', 'Conceitos de Machine Learning, Deep Learning e algoritmos de IA', 100, 4, NOW()),
('Redes de Computadores', 'Prof. Ana Ribeiro', 'Introdução às redes de computadores', 'Estudo de protocolos de redes, TCP/IP, segurança de redes', 100, 4, NOW()),
('Programação Web', 'Prof. Lucas Ferreira', 'Desenvolvimento de aplicações web', 'Frameworks de front-end e back-end, como React, Node.js', 100, 4, NOW()),
('Segurança da Informação', 'Prof. Ana Ribeiro', 'Introdução à segurança de dados', 'Criptografia, proteção de sistemas e vulnerabilidades', 80, 4, NOW()),
('Análise de Algoritmos', 'Prof. João Silva', 'Eficiência de algoritmos', 'Análise de algoritmos e estruturas de dados avançadas', 80, 4, NOW()),
('Empreendedorismo', 'Prof. Júlia Prado', 'Estudo sobre startups', 'Conceitos de criação de empresas e inovação no mercado', 60, 2, NOW()),
('Matemática Aplicada', 'Prof. Carlos Souza', 'Conceitos matemáticos aplicados', 'Estudo de cálculo diferencial e integral, e álgebra linear', 60, 4, NOW()),
('Design Digital', 'Prof. Marta Lima', 'Ferramentas para design digital', 'Photoshop, Illustrator, e outras ferramentas digitais de design', 60, 3, NOW()),
('Arquitetura de Software', 'Prof. João Silva', 'Criação de arquiteturas robustas', 'Design de sistemas escaláveis e microsserviços', 80, 1, NOW()),
('Marketing Pessoal', 'Prof. Laura Mendes', 'Estratégias de marketing pessoal', 'Desenvolvimento de marca pessoal, networking e carreira', 60, 2, NOW());


INSERT INTO Alunos (nome_completo, "RA", senha, data_nascimento, genero, endereco, email, telefone, documento_identidade, cpf, data_matricula, numero_matricula, id_curso, id_turma, "createdAt")
VALUES
-- Alunos do curso de Engenharia de Software (Turmas ES-2023-1 e ES-2024-1)
('Pedro Henrique da Silva', 12345678, 'Senha123@', '2000-05-15', 'Masculino', 'Rua José Antônio de Campos, Registro-SP', 'pedro_henrique.tech@gmail.com', '+55 13 98765-4321', '123456789', '11122233344', '2023-01-10', '2023123456', 1, 1, NOW()),
('Lucas Pereira Santos', 23456789, 'Lucas@2023!', '2000-03-22', 'Masculino', 'Rua Waldomiro Giraldes Garcia, Registro-SP', 'lucas_pereira.dev@gmail.com', '+55 13 98765-4322', '987654321', '22233344455', '2023-01-11', '2023123457', 1, 1, NOW()),
('Mariana Costa Oliveira', 34567890, 'Mari.Costa2023$', '2001-07-10', 'Feminino', 'Rua Nelson Alonso Tomé, Cajati-SP', 'mariana_costa.code@gmail.com', '+55 13 98765-4323', '654321987', '33344455566', '2023-01-12', '2023123458', 1, 1, NOW()),
('Roberto Lima Souza', 45678901, 'RobertoLima@!', '1999-02-14', 'Masculino', 'Rua Benedito de França Filho, Cajati-SP', 'roberto.lima.dev@outlook.com', '+55 13 98765-4324', '321654987', '44455566677', '2023-01-13', '2023123459', 1, 1, NOW()),
('Juliana Mendes Ferreira', 56789012, 'Juli@mendes', '2000-08-30', 'Feminino', 'Avenida Deputado Ulisses Guimarães, Pariquera-SP', 'juliana.mendes.dev@gmail.com', '+55 13 98765-4325', '987123654', '55566677788', '2023-01-14', '2023123460', 1, 1, NOW()),
('Felipe Costa Nascimento', 67890123, 'Felipe2023!', '2000-05-18', 'Masculino', 'Rua Arthur Silva, Jacupiranga-SP', 'felipe_nascimento.tech@gmail.com', '+55 13 98765-4326', '654987321', '66677788899', '2023-01-15', '2023123461', 1, 1, NOW()),
('Bruna Alves de Souza', 78901234, 'BrunaAlves@123', '1998-12-23', 'Feminino', 'Rua Fernando Costa, Juquiá-SP', 'bruna.alves.code@hotmail.com', '+55 13 98765-4327', '321987654', '77788899900', '2023-01-16', '2023123462', 1, 5, NOW()),
('Thiago Rocha Silva', 89012345, 'Thiago123!', '2000-11-22', 'Masculino', 'Rua Emílio Ribas, Juquiá-SP', 'thiago_rocha.dev@gmail.com', '+55 13 98765-4328', '654321123', '88899911122', '2023-01-17', '2023123463', 1, 5, NOW()),
('Camila Fernanda Alves', 90123456, 'CamilaFernanda@23', '2001-04-05', 'Feminino', 'Rua São Benedito, Cananéia-SP', 'camila.fernanda.tech@outlook.com', '+55 13 98765-4329', '321654123', '99911122233', '2023-01-18', '2023123464', 1, 5, NOW()),
('Rodrigo Araújo Martins', 12345679, 'Rodrigo2023@!', '1999-09-08', 'Masculino', 'Rua São José, Registro-SP', 'rodrigo.araujo.dev@gmail.com', '+55 13 98765-4330', '987654123', '11122233355', '2023-01-19', '2023123465', 1, 5, NOW()),
('Maria Clara Oliveira', 11223344, 'MariaClara2023$', '2001-08-20', 'Feminino', 'Rua Antônio Pereira de Lima, Registro-SP', 'maria_clara.empire@hotmail.com', '+55 13 98765-4331', '112233445', '44455566677', '2023-01-10', '2023123466', 2, 2, NOW()),
('José Roberto da Silva', 22334455, 'JoseSilva2023!', '1998-07-15', 'Masculino', 'Avenida Clara Gianoti de Souza, Pariquera-SP', 'jose.roberto.bussiness@gmail.com', '+55 13 98765-4332', '223344556', '55566677788', '2023-01-11', '2023123467', 2, 2, NOW()),
('Ana Paula Santos', 33445566, 'AnaPaula2023@', '1999-11-18', 'Feminino', 'Rua José Pereira Leite, Cajati-SP', 'ana.paula.admin@outlook.com', '+55 13 98765-4333', '334455667', '66677788899', '2023-01-12', '2023123468', 2, 2, NOW()),
('Carlos Eduardo Pereira', 44556677, 'CarlosEdu@23', '2000-06-27', 'Masculino', 'Rua Américo Leite, Cananéia-SP', 'carlos.eduardo@admincorp.com', '+55 13 98765-4334', '445566778', '77788899900', '2023-01-13', '2023123469', 2, 2, NOW()),
('Fernanda Souza Silva', 55667788, 'FerSouza2023$', '2000-03-16', 'Feminino', 'Rua São João, Jacupiranga-SP', 'fernanda.souza.biz@gmail.com', '+55 13 98765-4335', '556677889', '88899911122', '2023-01-14', '2023123470', 2, 6, NOW()),
('Leonardo Alves', 66778899, 'LeoAdmin123!', '1998-12-05', 'Masculino', 'Rua São Miguel, Registro-SP', 'leonardo.alves.admin@outlook.com', '+55 13 98765-4336', '667788990', '99911122233', '2023-01-15', '2023123471', 2, 6, NOW()),
('Julia Pereira Lima', 77889900, 'JuliaPereira@23', '1999-07-11', 'Feminino', 'Rua Santa Clara, Cajati-SP', 'julia.lima.enterprize@gmail.com', '+55 13 98765-4337', '778899001', '11122233344', '2023-01-16', '2023123472', 2, 6, NOW()),
('Gabriel da Costa', 88990011, 'GabrielCosta@$', '2001-02-22', 'Masculino', 'Rua São Pedro, Juquiá-SP', 'gabriel.costa.bizz@gmail.com', '+55 13 98765-4338', '889900112', '22233344455', '2023-01-17', '2023123473', 2, 6, NOW()),
('Larissa Fernandes', 99001122, 'LariFernanda2023$', '1998-05-19', 'Feminino', 'Avenida das Flores, Jacupiranga-SP', 'larissa.fernandes.marketing@gmail.com', '+55 13 98765-4339', '990011223', '33344455566', '2023-01-18', '2023123474', 2, 6, NOW()),
('Marcelo Ferreira', 10112233, 'Marcelo2023!', '1999-03-25', 'Masculino', 'Rua Dom Pedro II, Registro-SP', 'marcelo.ferreira.admin@outlook.com', '+55 13 98765-4340', '101122334', '44455566677', '2023-01-19', '2023123475', 2, 6, NOW()),
('Beatriz Carvalho Mendes', 21223344, 'Beatriz2023@', '2000-07-20', 'Feminino', 'Rua Benedito Rui Barbosa, Registro-SP', 'beatriz_mendes.design@gmail.com', '+55 13 98765-4341', '212233445', '55566677788', '2023-01-10', '2023123476', 3, 3, NOW()),
('Eduardo Lima', 32334455, 'EduardoLima#23', '2001-09-15', 'Masculino', 'Rua Duque de Caxias, Cajati-SP', 'eduardo.lima.art@outlook.com', '+55 13 98765-4342', '323344556', '66677788899', '2023-01-11', '2023123477', 3, 3, NOW()),
('Carolina Santos da Silva', 43445566, 'CarolSantos23!', '2000-10-09', 'Feminino', 'Rua das Palmeiras, Cananéia-SP', 'carolina.santos.designer@gmail.com', '+55 13 98765-4343', '434455667', '77788899900', '2023-01-12', '2023123478', 3, 3, NOW()),
('Rafael de Souza Oliveira', 54556677, 'Rafael_2023!', '1999-01-31', 'Masculino', 'Avenida dos Trabalhadores, Juquiá-SP', 'rafael.oliveira.design@outlook.com', '+55 13 98765-4344', '545566778', '88899911122', '2023-01-13', '2023123479', 3, 3, NOW()),
('Patricia Vieira Martins', 65667788, 'PatriciaDesign@$', '2001-06-21', 'Feminino', 'Rua Princesa Isabel, Pariquera-SP', 'patricia.vieira.illustration@gmail.com', '+55 13 98765-4345', '656677889', '99911122233', '2023-01-14', '2023123480', 3, 7, NOW()),
('Daniel Pereira', 76778899, 'DanielPereira123', '2000-03-18', 'Masculino', 'Rua Capitão Alberto Mendes Júnior, Registro-SP', 'daniel.pereira.design@outlook.com', '+55 13 98765-4346', '767788990', '11122233355', '2023-01-15', '2023123481', 3, 7, NOW()),
('Fernanda Ribeiro Lima', 87889900, 'FernandaLima2023@', '2001-05-16', 'Feminino', 'Rua Manoel da Nóbrega, Jacupiranga-SP', 'fernanda.lima.graphic@gmail.com', '+55 13 98765-4347', '878899001', '22233344466', '2023-01-16', '2023123482', 3, 7, NOW()),
('Vinícius Silva Santos', 98990011, 'Vinicius@Design!', '2000-08-04', 'Masculino', 'Rua Coronel José de Andrade, Juquiá-SP', 'vinicius.santos.art@outlook.com', '+55 13 98765-4348', '989900112', '33344455577', '2023-01-17', '2023123483', 3, 7, NOW()),
('Letícia Costa Souza', 10101122, 'LeticiaDesign23@', '1998-12-03', 'Feminino', 'Rua Capitão Moisés Mendes, Pariquera-SP', 'leticia.costa.design@gmail.com', '+55 13 98765-4349', '101011223', '44455566688', '2023-01-18', '2023123484', 3, 7, NOW()),
('Fábio Almeida Santos', 11112233, 'FabioDesign@$', '1999-02-26', 'Masculino', 'Rua Sete de Setembro, Cajati-SP', 'fabio.almeida.graphic@outlook.com', '+55 13 98765-4350', '111122334', '55566677799', '2023-01-19', '2023123485', 3, 7, NOW()),
('Gabriel Henrique Souza', 22223344, 'Gabriel2023@!', '1999-05-21', 'Masculino', 'Rua João de Barros, Registro-SP', 'gabriel_henrique.cc@gmail.com', '+55 13 98765-4351', '222233445', '11122233366', '2023-01-10', '2023123486', 4, 4, NOW()),
('Luana Silva Alves', 33334455, 'Luana.Silva@!', '2000-09-15', 'Feminino', 'Rua Doutor João Batista de Carvalho, Cajati-SP', 'luana.alves.dev@outlook.com', '+55 13 98765-4352', '333344556', '22233344477', '2023-01-11', '2023123487', 4, 4, NOW()),
('Ricardo Oliveira Santos', 44445566, 'RicardoDev23$', '2001-02-12', 'Masculino', 'Rua Luiz Matias Bittencourt, Cananéia-SP', 'ricardo.santos.code@gmail.com', '+55 13 98765-4353', '444455667', '33344455588', '2023-01-12', '2023123488', 4, 4, NOW()),
('Isabela Maria Costa', 55556677, 'Isabela.Costa@!', '1998-06-30', 'Feminino', 'Rua dos Expedicionários, Pariquera-SP', 'isabela.maria.tech@outlook.com', '+55 13 98765-4354', '555566778', '44455566699', '2023-01-13', '2023123489', 4, 4, NOW()),
('Victor Hugo Carvalho', 66667788, 'VictorDev@23$', '2000-08-09', 'Masculino', 'Rua Benjamin Constant, Juquiá-SP', 'victor.hugo.code@outlook.com', '+55 13 98765-4355', '666677889', '55566677711', '2023-01-14', '2023123490', 4, 4, NOW()),
('Camila Ribeiro Souza', 77778899, 'CamilaCode2023@', '1999-03-05', 'Feminino', 'Rua Marechal Deodoro, Jacupiranga-SP', 'camila.souza.dev@gmail.com', '+55 13 98765-4356', '777788990', '66677788822', '2023-01-15', '2023123491', 4, 8, NOW()),
('Fernando Lopes Mendes', 88889900, 'Fernando.Lopes@23$', '1998-11-23', 'Masculino', 'Rua Dom Pedro I, Registro-SP', 'fernando.lopes.cc@outlook.com', '+55 13 98765-4357', '888899001', '77788899933', '2023-01-16', '2023123492', 4, 8, NOW()),
('Patrícia Lima Santos', 99990011, 'PatriciaLima@2023!', '2000-10-07', 'Feminino', 'Rua Comendador Vicente, Cajati-SP', 'patricia.lima.tech@gmail.com', '+55 13 98765-4358', '999900112', '88899911144', '2023-01-17', '2023123493', 4, 8, NOW()),
('João Carlos Oliveira', 11112244, 'JoaoCarlos2023@', '1999-04-13', 'Masculino', 'Rua Conselheiro Rodrigues Alves, Cananéia-SP', 'joao.carlos.dev@outlook.com', '+55 13 98765-4359', '111122445', '99911122255', '2023-01-18', '2023123494', 4, 8, NOW()),
('Renata Silva Fernandes', 12223355, 'RenataFernandes@!', '2001-01-29', 'Feminino', 'Rua São Vicente, Pariquera-SP', 'renata.fernandes.code@gmail.com', '+55 13 98765-4360', '122233556', '11122233366', '2023-01-19', '2023123495', 4, 8, NOW()),
('Thiago Souza Lima', 13334466, 'ThiagoLima2023$', '2001-06-11', 'Masculino', 'Rua Rio Branco, Juquiá-SP', 'thiago.lima.dev@gmail.com', '+55 13 98765-4361', '133344667', '22233344477', '2023-01-10', '2023123496', 1, 5, NOW()),
('Larissa Oliveira Santos', 14445577, 'LarissaOliveira23!', '2000-02-14', 'Feminino', 'Rua São Jorge, Jacupiranga-SP', 'larissa.santos.design@gmail.com', '+55 13 98765-4362', '144455778', '33344455588', '2023-01-11', '2023123497', 3, 7, NOW()),
('Marcelo Augusto Carvalho', 15556688, 'MarceloAugusto@23$', '1999-12-05', 'Masculino', 'Rua Nove de Julho, Registro-SP', 'marcelo.carvalho.cc@outlook.com', '+55 13 98765-4363', '155566889', '44455566699', '2023-01-12', '2023123498', 4, 4, NOW()),
('Adriana Silva Pereira', 16667799, 'AdrianaPereira2023$', '2000-05-22', 'Feminino', 'Rua dos Andrades, Cajati-SP', 'adriana.pereira.dev@gmail.com', '+55 13 98765-4364', '166677990', '55566677711', '2023-01-13', '2023123499', 1, 1, NOW()),
('Henrique Sousa Carvalho', 17778800, 'HenriqueCarvalho@$', '2000-09-10', 'Masculino', 'Rua Tertuliano Brito, Cananéia-SP', 'henrique.sousa.tech@gmail.com', '+55 13 98765-4365', '177788001', '66677788822', '2023-01-14', '2023123500', 2, 6, NOW()),
('Júlia Maria Alves', 18889911, 'JuliaAlves23!', '1999-07-07', 'Feminino', 'Rua Professor Teixeira de Carvalho, Pariquera-SP', 'julia.alves.design@outlook.com', '+55 13 98765-4366', '188899112', '77788899933', '2023-01-15', '2023123501', 3, 3, NOW()),
('Rodrigo Silva Costa', 19990022, 'RodrigoCosta@2023!', '2000-01-21', 'Masculino', 'Rua Capitão Moisés Mendes, Juquiá-SP', 'rodrigo.costa.design@gmail.com', '+55 13 98765-4367', '199900223', '88899911144', '2023-01-16', '2023123502', 3, 7, NOW()),
('Tamires Souza Lima', 21112233, 'TamiresLima2023@!', '2001-11-18', 'Feminino', 'Rua Professor Antônio Teixeira, Registro-SP', 'tamires.lima.dev@gmail.com', '+55 13 98765-4368', '211122334', '99911122255', '2023-01-17', '2023123503', 1, 1, NOW()),
('Bruno Henrique Ferreira', 22223344, 'BrunoHenrique@23$', '2001-03-15', 'Masculino', 'Rua Capitão Moisés Mendes, Cajati-SP', 'bruno.ferreira.code@gmail.com', '+55 13 98765-4369', '222233445', '11122233366', '2023-01-18', '2023123504', 4, 4, NOW()),
('Fernanda Silva Santos', 23334455, 'FernandaSilva@2023!', '1999-04-23', 'Feminino', 'Rua São Sebastião, Cananéia-SP', 'fernanda.santos.design@gmail.com', '+55 13 98765-4370', '233344556', '22233344477', '2023-01-19', '2023123505', 3, 3, NOW()),
('Lucas Silva Martins', 24445566, 'LucasMartins23@!', '1998-06-30', 'Masculino', 'Rua Prefeito José Alves de Carvalho, Pariquera-SP', 'lucas.martins.dev@gmail.com', '+55 13 98765-4371', '244455667', '33344455588', '2023-01-10', '2023123506', 1, 5, NOW()),
('Alice Costa Santos', 25556677, 'AliceSantos@2023$', '2000-08-15', 'Feminino', 'Rua Prefeito Antônio Teixeira, Jacupiranga-SP', 'alice.santos.design@outlook.com', '+55 13 98765-4372', '255566778', '44455566699', '2023-01-11', '2023123507', 3, 7, NOW()),
('Rafael Mendes Oliveira', 26667788, 'RafaelMendes@23$', '1999-09-25', 'Masculino', 'Rua Santa Maria, Juquiá-SP', 'rafael.oliveira.code@gmail.com', '+55 13 98765-4373', '266677889', '55566677711', '2023-01-12', '2023123508', 4, 4, NOW()),
('Laura Ferreira Lima', 27778899, 'LauraFerreira2023@', '2000-02-07', 'Feminino', 'Rua Expedicionários, Registro-SP', 'laura.lima.dev@gmail.com', '+55 13 98765-4374', '277788990', '66677788822', '2023-01-13', '2023123509', 1, 1, NOW()),
('André Silva Souza', 28889900, 'AndreSouza@!', '1999-10-12', 'Masculino', 'Rua Marechal Rondon, Cajati-SP', 'andre.souza.code@outlook.com', '+55 13 98765-4375', '288899001', '77788899933', '2023-01-14', '2023123510', 4, 8, NOW()),
('Isabel Cristina Costa', 29990011, 'IsabelCosta@2023@', '2001-06-17', 'Feminino', 'Rua Dom Pedro II, Cananéia-SP', 'isabel.cristina.code@gmail.com', '+55 13 98765-4376', '299900112', '88899911144', '2023-01-15', '2023123511', 4, 8, NOW()),
('José Carlos Pereira', 31112222, 'JoseCarlos2023$', '1999-11-22', 'Masculino', 'Rua Quatro de Setembro, Pariquera-SP', 'jose.pereira.cc@outlook.com', '+55 13 98765-4377', '311122223', '99911122255', '2023-01-16', '2023123512', 4, 8, NOW()),
('Camila Maria Santos', 32223333, 'CamilaMaria23!', '2000-01-09', 'Feminino', 'Rua Vinte e Um de Abril, Juquiá-SP', 'camila.maria.design@outlook.com', '+55 13 98765-4378', '322233334', '11122233366', '2023-01-17', '2023123513', 3, 7, NOW()),
('Felipe Sousa Almeida', 33334444, 'FelipeSousa@2023$', '1998-12-16', 'Masculino', 'Rua Dois de Setembro, Jacupiranga-SP', 'felipe.almeida.dev@gmail.com', '+55 13 98765-4379', '333344445', '22233344477', '2023-01-18', '2023123514', 1, 1, NOW()),
('Sofia Oliveira Silva', 34445555, 'SofiaOliveira23$', '1999-08-31', 'Feminino', 'Rua Capitão Mor, Cananéia-SP', 'sofia.silva.design@gmail.com', '+55 13 98765-4380', '344455556', '33344455588', '2023-01-19', '2023123515', 3, 3, NOW());



INSERT INTO Usuarios (nome_completo, email, senha, tipo_usuario, status, area_atuacao, setor, data_contratacao, "createdAt")
VALUES
('João Silva', 'joao.silva.professor@gmail.com', 'ProfJoao2023$', 'Professor', 'Ativo', 'Tecnologia', 'Departamento de TI', '2018-02-15', NOW()),
('Carlos Souza', 'carlos.souza.adm@outlook.com', 'AdmCarlos23$', 'Professor', 'Ativo', 'Administração', 'Departamento de Gestão', '2017-06-30', NOW()),
('Marta Lima', 'marta.lima.design@outlook.com', 'DesignMarta@23', 'Professor', 'Ativo', 'Design Gráfico', 'Departamento de Artes', '2019-03-18', NOW()),
('Ana Ribeiro', 'ana.ribeiro.ia@gmail.com', 'AnaIA2023$', 'Professor', 'Ativo', 'Tecnologia', 'Departamento de Computação', '2020-05-22', NOW()),
('Júlia Prado', 'julia.prado.mkt@outlook.com', 'MktJulia23$', 'Professor', 'Ativo', 'Administração', 'Departamento de Marketing', '2019-08-10', NOW()),
('Laura Mendes', 'laura.mendes.rh@gmail.com', 'RhLaura2023$', 'Professor', 'Ativo', 'Recursos Humanos', 'Departamento de RH', '2021-01-12', NOW()),
('Eduardo Pereira', 'eduardo.pereira.ux@outlook.com', 'EduUX2023!', 'Professor', 'Ativo', 'Design', 'Departamento de UX', '2018-11-05', NOW()),
('Mariana Silva', 'mariana.silva.video@gmail.com', 'VideoMari@23', 'Professor', 'Ativo', 'Audiovisual', 'Departamento de Mídias', '2021-02-25', NOW()),
('Paulo Henrique', 'paulo.henrique.admin@outlook.com', 'AdminPaulo23$', 'Administrador', 'Ativo', 'Gestão', 'Administração Geral', '2016-10-20', NOW()),
('Fernanda Costa', 'fernanda.costa.gestao@gmail.com', 'GestaoFer23$', 'Administrador', 'Ativo', 'Tecnologia', 'Administração Geral', '2017-05-16', NOW()),
('Roberto Fernandes', 'roberto.fernandes.sec@outlook.com', 'SecRoberto2023$', 'Administrador', 'Ativo', 'Administração', 'Secretaria Acadêmica', '2018-09-10', NOW()),
('Renata Almeida', 'renata.almeida.secretaria@gmail.com', 'SecretRenata23$', 'Secretaria', 'Ativo', 'Educação', 'Secretaria Acadêmica', '2019-04-12', NOW()),
('Cláudia Souza', 'claudia.souza.secretaria@outlook.com', 'SecClaudia23$', 'Secretaria', 'Ativo', 'Gestão', 'Secretaria Geral', '2020-07-03', NOW()),
('Ricardo Martins', 'ricardo.martins.secretaria@gmail.com', 'SecretRicardo23$', 'Secretaria', 'Ativo', 'Educação', 'Secretaria de Cursos', '2021-11-28', NOW());




INSERT INTO Alunos_Materias (id_aluno, id_materia)
VALUES
(1, 1), (1, 2), (1, 3), (1, 4), (1, 5),
(2, 1), (2, 2), (2, 3), (2, 4), (2, 5),
(3, 1), (3, 2), (3, 3), (3, 4), (3, 5),
(4, 1), (4, 2), (4, 3), (4, 4), (4, 5),
(5, 1), (5, 2), (5, 3), (5, 4), (5, 5),
(6, 1), (6, 2), (6, 3), (6, 4), (6, 5),
(7, 1), (7, 2), (7, 3), (7, 4), (7, 5),
(8, 1), (8, 2), (8, 3), (8, 4), (8, 5),
(9, 1), (9, 2), (9, 3), (9, 4), (9, 5),
(10, 1), (10, 2), (10, 3), (10, 4), (10, 5),
(11, 6), (11, 7), (11, 8), (11, 9), (11, 10),
(12, 6), (12, 7), (12, 8), (12, 9), (12, 10),
(13, 6), (13, 7), (13, 8), (13, 9), (13, 10),
(14, 6), (14, 7), (14, 8), (14, 9), (14, 10),
(15, 6), (15, 7), (15, 8), (15, 9), (15, 10),
(16, 6), (16, 7), (16, 8), (16, 9), (16, 10),
(17, 6), (17, 7), (17, 8), (17, 9), (17, 10),
(18, 6), (18, 7), (18, 8), (18, 9), (18, 10),
(19, 6), (19, 7), (19, 8), (19, 9), (19, 10),
(20, 6), (20, 7), (20, 8), (20, 9), (20, 10),
(21, 11), (21, 12), (21, 13), (21, 14), (21, 15),
(22, 11), (22, 12), (22, 13), (22, 14), (22, 15),
(23, 11), (23, 12), (23, 13), (23, 14), (23, 15),
(24, 11), (24, 12), (24, 13), (24, 14), (24, 15),
(25, 11), (25, 12), (25, 13), (25, 14), (25, 15),
(26, 11), (26, 12), (26, 13), (26, 14), (26, 15),
(27, 11), (27, 12), (27, 13), (27, 14), (27, 15),
(28, 11), (28, 12), (28, 13), (28, 14), (28, 15),
(29, 11), (29, 12), (29, 13), (29, 14), (29, 15),
(30, 11), (30, 12), (30, 13), (30, 14), (30, 15),
(31, 16), (31, 17), (31, 18), (31, 19), (31, 20),
(32, 16), (32, 17), (32, 18), (32, 19), (32, 20),
(33, 16), (33, 17), (33, 18), (33, 19), (33, 20),
(34, 16), (34, 17), (34, 18), (34, 19), (34, 20),
(35, 16), (35, 17), (35, 18), (35, 19), (35, 20),
(36, 16), (36, 17), (36, 18), (36, 19), (36, 20),
(37, 16), (37, 17), (37, 18), (37, 19), (37, 20),
(38, 16), (38, 17), (38, 18), (38, 19), (38, 20),
(39, 16), (39, 17), (39, 18), (39, 19), (39, 20),
(40, 16), (40, 17), (40, 18), (40, 19), (40, 20);


INSERT INTO permissoes (nome_permissao, descricao_permissao)
VALUES
('Acesso Total', 'Permissão para acessar todas as áreas e funcionalidades do sistema.'),
('Gerenciar Usuários', 'Permissão para adicionar, editar e remover usuários do sistema.'),
('Gerenciar Conteúdo', 'Permissão para criar, editar e excluir conteúdo no sistema.'),
('Visualizar Relatórios', 'Permissão para visualizar e gerar relatórios administrativos e acadêmicos.'),
('Gerenciar Permissões', 'Permissão para atribuir e remover permissões a outros usuários.');


INSERT INTO roles (id_usuario, id_permissao)
VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5),
(6, 1),
(7, 3),
(8, 4),
(9, 1),
(10, 2),
(11, 4),
(12, 5),
(13, 5),
(12, 2),
(13, 3);





