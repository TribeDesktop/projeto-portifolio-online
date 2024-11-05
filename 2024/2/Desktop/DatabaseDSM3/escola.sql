-- --------------------------------------------------------
-- Servidor:                     127.0.0.1
-- Versão do servidor:           11.4.3-MariaDB - mariadb.org binary distribution
-- OS do Servidor:               Win64
-- HeidiSQL Versão:              12.7.0.6850
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Copiando estrutura do banco de dados para escola
CREATE DATABASE IF NOT EXISTS `escola` /*!40100 DEFAULT CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci */;
USE `escola`;

-- Copiando estrutura para tabela escola.alunos
CREATE TABLE IF NOT EXISTS `alunos` (
  `raAluno` int(15) NOT NULL,
  `usuarioID` int(11) NOT NULL,
  PRIMARY KEY (`usuarioID`),
  UNIQUE KEY `codigoMatriculaAluno_UNIQUE` (`raAluno`),
  KEY `fk_ALUNOS_USUARIOS1_idx` (`usuarioID`),
  CONSTRAINT `fk_ALUNOS_USUARIOS1` FOREIGN KEY (`usuarioID`) REFERENCES `usuarios` (`usuarioID`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_general_ci;

-- Copiando dados para a tabela escola.alunos: ~0 rows (aproximadamente)
INSERT INTO `alunos` (`raAluno`, `usuarioID`) VALUES
	(1001, 1),
	(1002, 3),
	(1003, 5),
	(1004, 7);

-- Copiando estrutura para tabela escola.atividades
CREATE TABLE IF NOT EXISTS `atividades` (
  `atividadeID` int(11) NOT NULL AUTO_INCREMENT,
  `tituloAtividade` varchar(45) NOT NULL,
  `pesoAtividade` varchar(45) NOT NULL,
  `descricaoAtividade` varchar(200) DEFAULT NULL,
  `turmaID` int(11) NOT NULL,
  PRIMARY KEY (`atividadeID`),
  KEY `fk_ATIVIDADES_TURMAS1_idx` (`turmaID`),
  CONSTRAINT `fk_ATIVIDADES_TURMAS1` FOREIGN KEY (`turmaID`) REFERENCES `turmas` (`turmaID`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_general_ci;

-- Copiando dados para a tabela escola.atividades: ~0 rows (aproximadamente)
INSERT INTO `atividades` (`atividadeID`, `tituloAtividade`, `pesoAtividade`, `descricaoAtividade`, `turmaID`) VALUES
	(1, 'Trabalho de História', '2', 'Análise de eventos históricos', 1),
	(2, 'Prova de Matemática', '3', 'Prova sobre funções e equações', 1),
	(3, 'Apresentação de Ciências', '1', 'Apresentação sobre ecossistemas', 2),
	(4, 'Atividade Prática de Química', '2', 'Experimentos sobre reações químicas', 2);

-- Copiando estrutura para tabela escola.boletins
CREATE TABLE IF NOT EXISTS `boletins` (
  `boletimID` int(11) NOT NULL AUTO_INCREMENT,
  `notaFinalBoletim` decimal(3,1) NOT NULL,
  `frequenciaFinalBoletim` float NOT NULL,
  `situacaoAlunoDisciplina` enum('aprovado','reprovado') DEFAULT NULL,
  `usuarioID` int(11) NOT NULL,
  `turmaID` int(11) NOT NULL,
  PRIMARY KEY (`boletimID`),
  KEY `fk_boletins_USUARIOS1_idx` (`usuarioID`),
  KEY `fk_boletins_TURMAS1_idx` (`turmaID`),
  CONSTRAINT `fk_boletins_TURMAS1` FOREIGN KEY (`turmaID`) REFERENCES `turmas` (`turmaID`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_boletins_USUARIOS1` FOREIGN KEY (`usuarioID`) REFERENCES `usuarios` (`usuarioID`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_general_ci;

-- Copiando dados para a tabela escola.boletins: ~0 rows (aproximadamente)
INSERT INTO `boletins` (`boletimID`, `notaFinalBoletim`, `frequenciaFinalBoletim`, `situacaoAlunoDisciplina`, `usuarioID`, `turmaID`) VALUES
	(9, 9.5, 90, 'aprovado', 1, 2),
	(10, 8.7, 80.5, 'aprovado', 3, 2),
	(11, 7.0, 70, 'reprovado', 5, 1),
	(12, 6.5, 60, 'reprovado', 7, 1);

-- Copiando estrutura para tabela escola.chamadas
CREATE TABLE IF NOT EXISTS `chamadas` (
  `situacaoID` int(11) NOT NULL AUTO_INCREMENT,
  `faltasAluno` tinyint(4) NOT NULL,
  `dataChamada` date DEFAULT NULL,
  `usuarioID` int(11) NOT NULL,
  `turmaID` int(11) NOT NULL,
  PRIMARY KEY (`situacaoID`),
  KEY `fk_chamadas_USUARIOS1_idx` (`usuarioID`),
  KEY `fk_chamadas_TURMAS1_idx` (`turmaID`),
  CONSTRAINT `fk_chamadas_TURMAS1` FOREIGN KEY (`turmaID`) REFERENCES `turmas` (`turmaID`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_chamadas_USUARIOS1` FOREIGN KEY (`usuarioID`) REFERENCES `usuarios` (`usuarioID`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_general_ci;

-- Copiando dados para a tabela escola.chamadas: ~0 rows (aproximadamente)
INSERT INTO `chamadas` (`situacaoID`, `faltasAluno`, `dataChamada`, `usuarioID`, `turmaID`) VALUES
	(1, 1, '2023-09-01', 1, 2),
	(2, 0, '2023-09-01', 5, 1),
	(3, 1, '2023-09-01', 7, 1),
	(4, 0, '2023-09-01', 3, 2);

-- Copiando estrutura para tabela escola.cursos
CREATE TABLE IF NOT EXISTS `cursos` (
  `cursoID` int(11) NOT NULL AUTO_INCREMENT,
  `nomeCurso` varchar(75) NOT NULL,
  `siglaCurso` varchar(10) NOT NULL,
  `tipoDuração` enum('semestral','anual') NOT NULL,
  `periodoCurso` enum('vespertino','matutino','noturno') NOT NULL,
  `tipoGraduacaoCurso` enum('Bacharelado','Licenciatura','Tecnólogo','Mestrado','Doutorado') NOT NULL,
  `descricaoCurso` longtext,
  PRIMARY KEY (`cursoID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_general_ci;

-- Copiando dados para a tabela escola.cursos: ~0 rows (aproximadamente)
INSERT INTO `cursos` (`cursoID`, `nomeCurso`, `siglaCurso`, `tipoDuração`, `periodoCurso`, `tipoGraduacaoCurso`, `descricaoCurso`) VALUES
	(1, 'Ciência da Computação', 'CC', 'semestral', 'vespertino', 'Bacharelado', 'Curso voltado para o desenvolvimento de habilidades em programação e tecnologia.'),
	(2, 'Pedagogia', 'Ped', 'anual', 'matutino', 'Licenciatura', 'Curso destinado à formação de professores para a educação básica.');

-- Copiando estrutura para tabela escola.diasnaoletivos
CREATE TABLE IF NOT EXISTS `diasnaoletivos` (
  `diasNaoLetivosID` int(11) NOT NULL AUTO_INCREMENT,
  `dataDia` varchar(45) DEFAULT NULL,
  `descricaoDia` varchar(45) DEFAULT NULL,
  `turmaID` int(11) NOT NULL,
  PRIMARY KEY (`diasNaoLetivosID`),
  KEY `fk_diasNaoLetivos_TURMAS1_idx` (`turmaID`),
  CONSTRAINT `fk_diasNaoLetivos_TURMAS1` FOREIGN KEY (`turmaID`) REFERENCES `turmas` (`turmaID`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_general_ci;

-- Copiando dados para a tabela escola.diasnaoletivos: ~0 rows (aproximadamente)
INSERT INTO `diasnaoletivos` (`diasNaoLetivosID`, `dataDia`, `descricaoDia`, `turmaID`) VALUES
	(1, '2023-04-21', 'Tiradentes', 1),
	(2, '2023-06-15', 'Feriado de São João', 2);

-- Copiando estrutura para tabela escola.disciplinas
CREATE TABLE IF NOT EXISTS `disciplinas` (
  `disciplinaID` int(11) NOT NULL AUTO_INCREMENT,
  `nomeDisciplina` varchar(75) NOT NULL,
  `siglaDisciplina` varchar(10) NOT NULL,
  `aulasSemanaisDisciplina` int(11) NOT NULL,
  `aulasTotaisSemestreDisciplina` int(11) NOT NULL,
  `cargaHorariaDisciplina` time NOT NULL,
  `ementa` longtext NOT NULL,
  `turmaID` int(11) NOT NULL,
  `cursoID` int(11) NOT NULL,
  PRIMARY KEY (`disciplinaID`),
  KEY `fk_disciplinas_TURMAS1_idx` (`turmaID`),
  KEY `fk_disciplinas_CURSOS1_idx` (`cursoID`),
  CONSTRAINT `fk_disciplinas_CURSOS1` FOREIGN KEY (`cursoID`) REFERENCES `cursos` (`cursoID`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_disciplinas_TURMAS1` FOREIGN KEY (`turmaID`) REFERENCES `turmas` (`turmaID`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_general_ci;

-- Copiando dados para a tabela escola.disciplinas: ~0 rows (aproximadamente)
INSERT INTO `disciplinas` (`disciplinaID`, `nomeDisciplina`, `siglaDisciplina`, `aulasSemanaisDisciplina`, `aulasTotaisSemestreDisciplina`, `cargaHorariaDisciplina`, `ementa`, `turmaID`, `cursoID`) VALUES
	(1, 'Programação I', 'PROG1', 4, 60, '60:00:00', 'Introdução à programação e lógica de programação.', 1, 1),
	(2, 'Banco de Dados', 'BD', 3, 45, '45:00:00', 'Conceitos de banco de dados e SQL.', 1, 1),
	(3, 'Estruturas de Dados', 'ED', 4, 60, '60:00:00', 'Estudo de estruturas de dados e algoritmos.', 1, 1),
	(4, 'Sistemas Operacionais', 'SO', 2, 30, '30:00:00', 'Conceitos de sistemas operacionais.', 1, 1),
	(5, 'Didática', 'DID', 3, 45, '45:00:00', 'Fundamentos da didática e métodos de ensino.', 2, 2),
	(6, 'Psicologia da Educação', 'PSICO', 2, 30, '30:00:00', 'Estudo da psicologia aplicada à educação.', 2, 2),
	(7, 'Educação Inclusiva', 'EDUCI', 2, 30, '30:00:00', 'Práticas de inclusão no ambiente escolar.', 2, 2),
	(8, 'Avaliação Educacional', 'AVAL', 3, 45, '45:00:00', 'Conceitos de avaliação na educação.', 2, 2);

-- Copiando estrutura para tabela escola.emailusuarios
CREATE TABLE IF NOT EXISTS `emailusuarios` (
  `emailID` int(11) NOT NULL AUTO_INCREMENT,
  `emailUsuario` varchar(100) NOT NULL,
  `tipoEmail` varchar(60) DEFAULT NULL,
  `usuarioID` int(11) NOT NULL,
  PRIMARY KEY (`emailID`),
  UNIQUE KEY `emailAluno_UNIQUE` (`emailUsuario`),
  KEY `fk_emailUsuarios_USUARIOS1_idx` (`usuarioID`),
  CONSTRAINT `fk_emailUsuarios_USUARIOS1` FOREIGN KEY (`usuarioID`) REFERENCES `usuarios` (`usuarioID`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_general_ci;

-- Copiando dados para a tabela escola.emailusuarios: ~0 rows (aproximadamente)
INSERT INTO `emailusuarios` (`emailID`, `emailUsuario`, `tipoEmail`, `usuarioID`) VALUES
	(1, 'ana.silva@example.com', 'Pessoal', 1),
	(2, 'carlos.oliveira@example.com', 'Profissional', 2),
	(3, 'julia.costa@example.com', 'Pessoal', 3),
	(4, 'fernando.almeida@example.com', 'Profissional', 4),
	(5, 'mariana.santos@example.com', 'Pessoal', 5),
	(6, 'roberto.ferreira@example.com', 'Profissional', 6),
	(7, 'luiza.martins@example.com', 'Pessoal', 7),
	(8, 'tiago.ramos@example.com', 'Profissional', 8);

-- Copiando estrutura para tabela escola.enderecousuarios
CREATE TABLE IF NOT EXISTS `enderecousuarios` (
  `enderecoUsuarioID` int(11) NOT NULL AUTO_INCREMENT,
  `cepUsuario` varchar(10) NOT NULL,
  `bairroUsuario` varchar(45) NOT NULL,
  `logradouroUsuario` varchar(60) NOT NULL,
  `numResidenciaUsuario` int(11) NOT NULL,
  `usuarioID` int(11) NOT NULL,
  PRIMARY KEY (`enderecoUsuarioID`),
  KEY `fk_enderecoUsuarios_USUARIOS1_idx` (`usuarioID`),
  CONSTRAINT `fk_enderecoUsuarios_USUARIOS1` FOREIGN KEY (`usuarioID`) REFERENCES `usuarios` (`usuarioID`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_general_ci;

-- Copiando dados para a tabela escola.enderecousuarios: ~0 rows (aproximadamente)
INSERT INTO `enderecousuarios` (`enderecoUsuarioID`, `cepUsuario`, `bairroUsuario`, `logradouroUsuario`, `numResidenciaUsuario`, `usuarioID`) VALUES
	(1, '01000-000', 'Centro', 'Rua A', 100, 1),
	(2, '02000-000', 'Jardim', 'Rua B', 200, 2),
	(3, '03000-000', 'Vila', 'Rua C', 300, 3),
	(4, '04000-000', 'Alameda', 'Rua D', 400, 4),
	(5, '05000-000', 'Praça', 'Rua E', 500, 5),
	(6, '06000-000', 'Lagoa', 'Rua F', 600, 6),
	(7, '07000-000', 'Parque', 'Rua G', 700, 7),
	(8, '08000-000', 'Planalto', 'Rua H', 800, 8);

-- Copiando estrutura para tabela escola.horarios
CREATE TABLE IF NOT EXISTS `horarios` (
  `horarioID` int(11) NOT NULL AUTO_INCREMENT,
  `horaInicio` time DEFAULT NULL,
  `horaFim` time DEFAULT NULL,
  PRIMARY KEY (`horarioID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_general_ci;

-- Copiando dados para a tabela escola.horarios: ~0 rows (aproximadamente)
INSERT INTO `horarios` (`horaInicio`, `horaFim`) VALUES
	('08:00:00', '09:30:00'),
	('09:45:00', '11:15:00'),
	('11:30:00', '13:00:00'),
	('14:00:00', '15:30:00'),
	('08:00:00', '09:30:00'),
	('09:45:00', '11:15:00'),
	('11:30:00', '13:00:00'),
	('14:00:00', '15:30:00');

-- Copiando estrutura para tabela escola.matriculas
CREATE TABLE IF NOT EXISTS `matriculas` (
  `matriculaID` int(11) NOT NULL AUTO_INCREMENT,
  `situacaoAlunoMatricula` enum('ativo','pendente','inativo') NOT NULL,
  `dataMatricula` date NOT NULL,
  `cursoID` int(11) NOT NULL,
  `usuarioID` int(11) NOT NULL,
  PRIMARY KEY (`matriculaID`),
  KEY `fk_ALUNOS_has_CURSOS_CURSOS1_idx` (`cursoID`),
  KEY `fk_matriculas_USUARIOS1_idx` (`usuarioID`),
  CONSTRAINT `fk_ALUNOS_has_CURSOS_CURSOS1` FOREIGN KEY (`cursoID`) REFERENCES `cursos` (`cursoID`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_matriculas_USUARIOS1` FOREIGN KEY (`usuarioID`) REFERENCES `usuarios` (`usuarioID`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_general_ci;

-- Copiando dados para a tabela escola.matriculas: ~0 rows (aproximadamente)
INSERT INTO `matriculas` (`matriculaID`, `situacaoAlunoMatricula`, `dataMatricula`, `cursoID`, `usuarioID`) VALUES
	(1, 'ativo', '2023-01-10', 1, 2),
	(2, 'pendente', '2023-02-15', 1, 1),
	(3, 'inativo', '2023-03-20', 1, 3),
	(4, 'ativo', '2023-04-25', 1, 4),
	(5, 'ativo', '2023-05-30', 2, 6),
	(6, 'pendente', '2023-06-15', 2, 5),
	(7, 'inativo', '2023-07-10', 2, 7),
	(8, 'ativo', '2023-08-20', 2, 8);

-- Copiando estrutura para tabela escola.notas
CREATE TABLE IF NOT EXISTS `notas` (
  `notaID` int(11) NOT NULL AUTO_INCREMENT,
  `nota` decimal(4,2) NOT NULL,
  `atividadeID` int(11) NOT NULL,
  `usuarioID` int(11) NOT NULL,
  PRIMARY KEY (`notaID`),
  KEY `fk_ALUNOS_has_ATIVIDADES_ATIVIDADES1_idx` (`atividadeID`),
  KEY `fk_notas_USUARIOS1_idx` (`usuarioID`),
  CONSTRAINT `fk_ALUNOS_has_ATIVIDADES_ATIVIDADES1` FOREIGN KEY (`atividadeID`) REFERENCES `atividades` (`atividadeID`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_notas_USUARIOS1` FOREIGN KEY (`usuarioID`) REFERENCES `usuarios` (`usuarioID`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_general_ci;

-- Copiando dados para a tabela escola.notas: ~0 rows (aproximadamente)
INSERT INTO `notas` (`notaID`, `nota`, `atividadeID`, `usuarioID`) VALUES
	(1, 9.50, 3, 1),
	(2, 8.00, 4, 1),
	(3, 7.75, 3, 3),
	(4, 10.00, 4, 3),
	(5, 6.50, 1, 5),
	(6, 8.25, 2, 5),
	(7, 9.00, 1, 7),
	(8, 7.50, 2, 7);

-- Copiando estrutura para tabela escola.professores
CREATE TABLE IF NOT EXISTS `professores` (
  `titulacaoProfessor` varchar(45) NOT NULL,
  `formacaoProfessor` varchar(30) NOT NULL,
  `usuarioID` int(11) NOT NULL,
  PRIMARY KEY (`usuarioID`),
  KEY `fk_PROFESSORES_USUARIOS1_idx` (`usuarioID`),
  CONSTRAINT `fk_PROFESSORES_USUARIOS1` FOREIGN KEY (`usuarioID`) REFERENCES `usuarios` (`usuarioID`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_general_ci;

-- Copiando dados para a tabela escola.professores: ~0 rows (aproximadamente)
INSERT INTO `professores` (`titulacaoProfessor`, `formacaoProfessor`, `usuarioID`) VALUES
	('Mestre', 'Educação Física', 2),
	('Doutor', 'Matemática', 4),
	('Especialista', 'Química', 6),
	('Mestre', 'História', 8);

-- Copiando estrutura para tabela escola.secretarias
CREATE TABLE IF NOT EXISTS `secretarias` (
  `adminID` int(11) NOT NULL AUTO_INCREMENT,
  `usuarioAdmin` varchar(45) NOT NULL,
  `emailAdmin` varchar(50) NOT NULL,
  `senhaAdmin` varchar(30) NOT NULL,
  PRIMARY KEY (`adminID`),
  UNIQUE KEY `email_UNIQUE` (`emailAdmin`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_general_ci;

-- Copiando dados para a tabela escola.secretarias: ~0 rows (aproximadamente)
INSERT INTO `secretarias` (`adminID`, `usuarioAdmin`, `emailAdmin`, `senhaAdmin`) VALUES
	(1, 'adminPrincipal', 'admin@escola.com', 'senhaSegura123');

-- Copiando estrutura para tabela escola.telefoneadmins
CREATE TABLE IF NOT EXISTS `telefoneadmins` (
  `telefoneAdminID` int(11) NOT NULL AUTO_INCREMENT,
  `telefoneFixo` varchar(15) NOT NULL,
  `numCelular` varchar(15) NOT NULL,
  `adminID` int(11) NOT NULL,
  PRIMARY KEY (`telefoneAdminID`),
  UNIQUE KEY `telefoneFixo_UNIQUE` (`telefoneFixo`),
  UNIQUE KEY `numCelular_UNIQUE` (`numCelular`),
  KEY `fk_telefoneAdmins_ADMINISTRACOES1_idx` (`adminID`),
  CONSTRAINT `fk_telefoneAdmins_ADMINISTRACOES1` FOREIGN KEY (`adminID`) REFERENCES `secretarias` (`adminID`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_general_ci;

-- Copiando dados para a tabela escola.telefoneadmins: ~0 rows (aproximadamente)
INSERT INTO `telefoneadmins` (`telefoneAdminID`, `telefoneFixo`, `numCelular`, `adminID`) VALUES
	(1, '(11) 1234-5678', '(11) 91234-5678', 1);

-- Copiando estrutura para tabela escola.telefoneusuarios
CREATE TABLE IF NOT EXISTS `telefoneusuarios` (
  `telefoneUsuarioID` int(11) NOT NULL AUTO_INCREMENT,
  `tipoTelefone` varchar(45) DEFAULT NULL,
  `telefoneUsuario` varchar(20) NOT NULL,
  `usuarioID` int(11) NOT NULL,
  PRIMARY KEY (`telefoneUsuarioID`),
  UNIQUE KEY `telefoneAluno_UNIQUE` (`telefoneUsuario`),
  KEY `fk_telefoneAlunos_ALUNOS1_idx` (`usuarioID`),
  CONSTRAINT `fk_telefoneAlunos_ALUNOS1` FOREIGN KEY (`usuarioID`) REFERENCES `usuarios` (`usuarioID`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_general_ci;

-- Copiando dados para a tabela escola.telefoneusuarios: ~0 rows (aproximadamente)
INSERT INTO `telefoneusuarios` (`telefoneUsuarioID`, `tipoTelefone`, `telefoneUsuario`, `usuarioID`) VALUES
	(1, 'Celular', '11-91234-5678', 1),
	(2, 'Fixo', '11-1234-5678', 2),
	(3, 'Celular', '21-91234-5678', 3),
	(4, 'Fixo', '21-1234-5678', 4),
	(5, 'Celular', '31-91234-5678', 5),
	(6, 'Fixo', '31-1234-5678', 6),
	(7, 'Celular', '41-91234-5678', 7),
	(8, 'Fixo', '41-1234-5678', 8);

-- Copiando estrutura para tabela escola.turmas
CREATE TABLE IF NOT EXISTS `turmas` (
  `turmaID` int(11) NOT NULL AUTO_INCREMENT,
  `turma` varchar(45) NOT NULL,
  `siglaTurma` varchar(10) DEFAULT NULL,
  `dataInicio` date NOT NULL,
  `dataFim` date DEFAULT NULL,
  PRIMARY KEY (`turmaID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_general_ci;

-- Copiando dados para a tabela escola.turmas: ~0 rows (aproximadamente)
INSERT INTO `turmas` (`turmaID`, `turma`, `siglaTurma`, `dataInicio`, `dataFim`) VALUES
	(1, 'PED-1', 'PED', '2023-01-10', '2026-12-15'),
	(2, 'CC-1', 'CC', '2023-02-01', '2026-12-15');

-- Copiando estrutura para tabela escola.usuarios
CREATE TABLE IF NOT EXISTS `usuarios` (
  `usuarioID` int(11) NOT NULL AUTO_INCREMENT,
  `nomeUsuario` varchar(100) NOT NULL,
  `senhaUsuario` varchar(20) NOT NULL,
  `dataNascUsuario` date NOT NULL,
  `sexoUsuario` enum('f','m','outro') NOT NULL,
  `cpfUsuario` varchar(20) NOT NULL,
  `tipoUsuario` enum('aluno','professor') NOT NULL,
  `ufUsuarios` varchar(2) DEFAULT NULL,
  `ativo` tinyint(4) NOT NULL,
  `adminID` int(11) NOT NULL,
  PRIMARY KEY (`usuarioID`),
  UNIQUE KEY `cpfAluno_UNIQUE` (`cpfUsuario`),
  KEY `fk_USUARIOS_SECRETARIAS1_idx` (`adminID`),
  CONSTRAINT `fk_USUARIOS_SECRETARIAS1` FOREIGN KEY (`adminID`) REFERENCES `secretarias` (`adminID`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_general_ci;

-- Copiando dados para a tabela escola.usuarios: ~0 rows (aproximadamente)
INSERT INTO `usuarios` (`usuarioID`, `nomeUsuario`, `senhaUsuario`, `dataNascUsuario`, `sexoUsuario`, `cpfUsuario`, `tipoUsuario`, `ufUsuarios`, `ativo`, `adminID`) VALUES
	(1, 'Ana Silva', 'senha123', '2000-05-15', 'f', '123.456.789-00', 'aluno', 'SP', 1, 1),
	(2, 'Carlos Oliveira', 'senha456', '1985-08-22', 'm', '987.654.321-00', 'professor', 'RJ', 1, 1),
	(3, 'Julia Costa', 'senha789', '1998-03-10', 'f', '321.654.987-00', 'aluno', 'MG', 1, 1),
	(4, 'Fernando Almeida', 'senha101', '1979-12-05', 'm', '456.789.123-00', 'professor', 'SP', 1, 1),
	(5, 'Mariana Santos', 'senha202', '2001-01-20', 'f', '111.222.333-44', 'aluno', 'PR', 1, 1),
	(6, 'Roberto Ferreira', 'senha303', '1980-07-14', 'm', '222.333.444-55', 'professor', 'SP', 1, 1),
	(7, 'Luiza Martins', 'senha404', '1999-11-30', 'f', '333.444.555-66', 'aluno', 'BA', 1, 1),
	(8, 'Tiago Ramos', 'senha505', '1987-04-10', 'm', '444.555.666-77', 'professor', 'CE', 1, 1);

-- Copiando estrutura para tabela escola.dias
CREATE TABLE IF NOT EXISTS `escola`.`dias` (
  `nomeDia` VARCHAR(20) NOT NULL,
  `disciplinaID` INT NOT NULL,
  `horarioID` INT NOT NULL,
  INDEX `fk_dias_disciplinas1_idx` (`disciplinaID` ASC) VISIBLE,
  CONSTRAINT `fk_dias_disciplinas1`
    FOREIGN KEY (`disciplinaID`)
    REFERENCES `escola`.`disciplinas` (`disciplinaID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_dias_HORARIOS1`
    FOREIGN KEY (`horarioID`)
    REFERENCES `escola`.`HORARIOS` (`horarioID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_general_ci;

-- Copiando dados para a tabela escola.dias: ~0 rows (aproximadamente)
INSERT INTO `dias` (`nomeDia`, `disciplinaID`, `horarioID`) 
VALUES
    -- Programação I (disciplinaID = 1)
    ('Segunda-feira', 1, 1),
    ('Quarta-feira', 1, 1),
    -- Banco de Dados (disciplinaID = 2)
    ('Terça-feira', 2, 2),
    ('Quinta-feira', 2, 2),
    -- Estruturas de Dados (disciplinaID = 3)
    ('Segunda-feira', 3, 3),
    ('Quarta-feira', 3, 3),
    -- Sistemas Operacionais (disciplinaID = 4)
    ('Sexta-feira', 4, 1),
    -- Didática (disciplinaID = 5)
    ('Terça-feira', 5, 4),
    ('Quinta-feira', 5, 4),
    -- Psicologia da Educação (disciplinaID = 6)
    ('Quarta-feira', 6, 2),
    -- Educação Inclusiva (disciplinaID = 7)
    ('Segunda-feira', 7, 5),
    -- Avaliação Educacional (disciplinaID = 8)
    ('Sexta-feira', 8, 3);


/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;


select * from horarios;
select * from disciplinas;
select * from dias;
SELECT 
    d.nomeDisciplina, 
    h.horaInicio, 
    h.horaFim, 
    dia.nomeDia, 
    d.aulasTotaisSemestreDisciplina
FROM 
    disciplinas AS d
INNER JOIN 
    dias AS dia ON dia.disciplinaID = d.disciplinaID
INNER JOIN 
    horarios AS h ON h.horarioID = dia.horarioID;

