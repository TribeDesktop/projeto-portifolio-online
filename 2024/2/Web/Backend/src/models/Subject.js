import { DataTypes } from 'sequelize';
import sequelize from '../config/database.js';

const Subject = sequelize.define(
  'Materia',
  {
    id_materia: {
      type: DataTypes.BIGINT,
      primaryKey: true,
      autoIncrement: true,
    },
    nome_materia: {
      type: DataTypes.TEXT,
      allowNull: false,
    },
    professor_materia: {
      type: DataTypes.TEXT,
      allowNull: false,
    },
    objetivo: {
      type: DataTypes.TEXT,
    },
    ementa: {
      type: DataTypes.TEXT,
    },
    carga_horaria: {
      type: DataTypes.INTEGER,
    },
    id_curso: {
      type: DataTypes.BIGINT,
    },
  },
  {
    tableName: 'materias',
    timestamps: false,
  }
);

export default Subject;
