import { DataTypes } from 'sequelize';
import sequelize from '../config/database.js';

const Students = sequelize.define(
  'Alunos',
  {
    id_aluno: {
      type: DataTypes.BIGINT,
      primaryKey: true,
      autoIncrement: true,
    },
    nome_completo: {
      type: DataTypes.TEXT,
      allowNull: false,
      validate: {
        notNull: { msg: 'Nome completo é obrigatório' },
        len: [3, 255],
      },
    },
    RA: {
      type: DataTypes.BIGINT,
      allowNull: false,
    },
    senha: {
      type: DataTypes.TEXT,
      allowNull: false,
      validate: {
        notEmpty: {
          msg: 'A senha é obrigatória.',
        },
        len: {
          args: [6, 255],
          msg: 'A senha deve ter no minímo 6 caracteres.',
        },
      },
    },
    data_nascimento: {
      type: DataTypes.DATE,
      validate: {
        isDate: true,
      },
    },
    genero: {
      type: DataTypes.TEXT,
    },
    endereco: {
      type: DataTypes.TEXT,
    },
    email: {
      type: DataTypes.TEXT,
      validate: {
        isEmail: { msg: 'Email inválido.' },
      },
    },
    telefone: {
      type: DataTypes.TEXT,
    },
    documento_identidade: {
      type: DataTypes.TEXT,
      unique: true,
      allowNull: false,
    },
    cpf: {
      type: DataTypes.TEXT,
      unique: true,
      validate: {
        len: [11, 11],
        isNumeric: { msg: 'CPF deve conter apenas números.' },
      },
    },
    data_matricula: {
      type: DataTypes.DATE,
    },
    numero_matricula: {
      type: DataTypes.TEXT,
    },
    id_curso: {
      type: DataTypes.BIGINT,
      references: {
        model: 'cursos',
        key: 'id_curso',
      },
    },
    id_turma: {
      type: DataTypes.BIGINT,
      references: {
        model: 'turmas',
        key: 'id_turma',
      },
    },
    caminho_da_foto: {
      type: DataTypes.TEXT,
    },
  },
  {
    tableName: 'alunos',
    timestamps: true,
  }
);

export default Students;
