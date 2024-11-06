import { DataTypes } from 'sequelize';
import sequelize from '../config/database.js';

const Roles = sequelize.define(
  'Roles',
  {
    id_role: {
      type: DataTypes.BIGINT,
      primaryKey: true,
      autoIncrement: true,
    },
    id_usuario: {
      type: DataTypes.BIGINT,
      allowNull: false,
    },
    id_permissao: {
      type: DataTypes.BIGINT,
    },
  },
  {
    tableName: 'roles',
    timestamps: true,
  }
);

export default Roles;
