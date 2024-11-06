import { DataTypes } from 'sequelize';
import sequelize from '../config/database.js';

const RollCall = sequelize.define(
  'Chamada',
  {
    id_chamada: {
      type: DataTypes.BIGINT,
      primaryKey: true,
      autoIncrement: true,
    },
    id_aluno: {
      type: DataTypes.BIGINT,
    },
    id_turma: {
      type: DataTypes.BIGINT,
    },
    id_materia: {
      type: DataTypes.BIGINT,
    },
    data_chamada: {
      type: DataTypes.DATE,
      allowNull: false,
    },
    presenca: {
      type: DataTypes.BOOLEAN,
      allowNull: false,
    },
    justificativa: {
      type: DataTypes.TEXT,
    },
    horario_chamada: {
      type: DataTypes.TIME,
      allowNull: false,
    },
    observacoes: {
      type: DataTypes.TEXT,
    },
  },
  {
    tableName: 'chamada',
    timestamps: true,
  }
);

export default RollCall;
