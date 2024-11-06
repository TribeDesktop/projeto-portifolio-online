import { DataTypes } from 'sequelize';
import sequelize from '../config/database.js';

const Permissions = sequelize.define(
  'Permissoes',
  {
    id_permissao: {
      type: DataTypes.BIGINT,
      primaryKey: true,
      autoIncrement: true,
    },
    nome_permissao: {
      type: DataTypes.TEXT,
      allowNull: false,
    },
    descricao_permissao: {
      type: DataTypes.TEXT,
    },
  },
  {
    tableName: 'permissoes',
    timestamps: true,
  }
);

export default Permissions;
