import { DataTypes } from 'sequelize';
import sequelize from '../config/database.js';

const Grade = sequelize.define(
  'Nota',
  {
    id_nota: {
      type: DataTypes.BIGINT,
      primaryKey: true,
      autoIncrement: true,
    },
    id_materia: {
      type: DataTypes.BIGINT,
      allowNull: false,
    },
    id_aluno: {
      type: DataTypes.BIGINT,
      allowNull: false,
    },
    nota: {
      type: DataTypes.FLOAT,
      allowNull: false,
    },
    data_avaliacao: {
      type: DataTypes.DATE,
      allowNull: false,
    },
  },
  {
    tableName: 'notas',
    timestamps: false,
  }
);

export default Grade;
