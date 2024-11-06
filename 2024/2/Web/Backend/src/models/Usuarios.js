import { DataTypes } from 'sequelize';
import sequelize from '../config/database.js';

const Users = sequelize.define(
  'Usuarios',
  {
    id_usuario: {
      type: DataTypes.BIGINT,
      primaryKey: true,
      autoIncrement: true,
    },
    nome_completo: {
      type: DataTypes.TEXT,
      allowNull: false,
      validate: {
        notEmpty: {
          msg: 'O nome completo não pode estar vazio.',
        },
        len: {
          args: [3, 255],
          msg: 'O nome completo deve ter entre 3 e 255 caracteres.',
        },
      },
    },
    email: {
      type: DataTypes.TEXT,
      allowNull: false,
      validate: {
        isEmail: {
          msg: 'O email deve ser um endereço válido.',
        },
        notEmpty: {
          msg: 'O email é obrigatório.',
        },
      },
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
          msg: 'A senha deve ter no mínimo 6 caracteres.',
        },
      },
    },
    tipo_usuario: {
      type: DataTypes.TEXT,
      allowNull: false,
    },
    status: {
      type: DataTypes.TEXT,
      allowNull: false,
    },
    caminho_da_foto: {
      type: DataTypes.TEXT,
    },
  },
  {
    tableName: 'usuarios',
    timestamps: true,
  }
);

export default Users;
