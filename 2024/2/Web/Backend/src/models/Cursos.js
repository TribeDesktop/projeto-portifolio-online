import { DataTypes } from 'sequelize';
import sequelize from '../config/database.js';

const Courses = sequelize.define(
  'Cursos',
  {
    id_curso: {
      type: DataTypes.BIGINT,
      primaryKey: true,
      autoIncrement: true,
    },
    nome_curso: {
      type: DataTypes.TEXT,
      allowNull: false,
    },
    descricao_curso: {
      type: DataTypes.TEXT,
    },
    duracao: {
      type: DataTypes.TEXT,
    },
    categoria: {
      type: DataTypes.TEXT,
    },
    nivel: {
      type: DataTypes.TEXT,
    },
    carga_horaria: {
      type: DataTypes.INTEGER,
    },
    data_inicio: {
      type: DataTypes.DATE,
    },
    data_fim: {
      type: DataTypes.DATE,
    },
  },
  {
    tableName: 'cursos',
    timestamps: true,
  }
);

export default Courses;
