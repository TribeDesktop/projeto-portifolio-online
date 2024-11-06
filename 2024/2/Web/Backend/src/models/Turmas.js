import { DataTypes } from 'sequelize';
import sequelize from '../config/database.js';

const Classes = sequelize.define(
  'Turmas',
  {
    id_turma: {
      type: DataTypes.BIGINT,
      primaryKey: true,
      autoIncrement: true,
    },
    nome_turma: {
      type: DataTypes.TEXT,
      allowNull: false,
    },
    ano_letivo: {
      type: DataTypes.TEXT,
      allowNull: false,
    },
    id_curso: {
      type: DataTypes.BIGINT,
    },
    horario: {
      type: DataTypes.TEXT,
    },
    sala: {
      type: DataTypes.TEXT,
    },
    professor_responsavel: {
      type: DataTypes.TEXT,
    },
    capacidade_maxima: {
      type: DataTypes.INTEGER,
    },
  },
  {
    tableName: 'turmas',
    timestamps: true,
  }
);

export default Classes;
