import Users from '../models/Usuarios.js';
import bcrypt from 'bcrypt';
import login from '../services/authService.js';
import { response, handleError } from '../Utils/Utils.js';


const getUsers = async (req, res) => {
  try {
    const users = await Users.findAll();
    return response(res, users);
  } catch (error) {
    return handleError(res, error);
  }
};

const createUser = async (req, res) => {
  const { nome_completo, email, senha, tipo_usuario, status, caminho_da_foto } = req.body;

  try {
    const existingUser = await Users.findOne({ where: { email } });

    if (existingUser) {
      return response(res, { message: 'Email já cadastrado.' }, 400);
    }

    const hashedPassword = await bcrypt.hash(senha, 10);

    const user = await Users.create({
      nome_completo: nome_completo,
      email: email,
      senha: hashedPassword,
      tipo_usuario: tipo_usuario,
      status: status,
      caminho_da_foto: caminho_da_foto,
    });

    return response(res, user, 201);
  } catch (error) {
    return handleError(res, error);
  }
};

const getUserById = async (req, res) => {
  const { id } = req.params;

  try {
    const user = await Users.findByPk(id);
    if (!user) {
      return response(res, { message: 'Usuário não encontrado.' }, 404);
    }
    return response(res, user);
  } catch (error) {
    return handleError(res, error);
  }
};

const updateUser = async (req, res) => {
  const { id } = req.params;
  const { nome_completo, email, senha, tipo_usuario, status, caminho_da_foto } = req.body;

  try {
    const user = await Users.findByPk(id);
    if (!user) {
      return response(res, { message: 'Usuário não encontrado.' }, 404);
    }

    const updateData = {
      nome_completo,
      email,
      tipo_usuario,
      status, // Inclui o status na atualização
      caminho_da_foto,
    };

    if (senha) {
      updateData.senha = await bcrypt.hash(senha, 10);
    }

    await Users.update(updateData, { where: { id_usuario: id } });
    return response(res, { message: 'Usuário atualizado com sucesso.' });
  } catch (error) {
    return handleError(res, error);
  }
};

const deleteUser = async (req, res) => {
  const { id } = req.params;

  try {
    const deleted = await Users.destroy({ where: { id_usuario: id } });
    if (!deleted) {
      return response(res, { message: 'Usuário não encontrado.' }, 404);
    }
    res.status(204).send();
  } catch (error) {
    return handleError(res, error);
  }
};

const loginUser = async (req, res) => {
  const { email, senha } = req.body;

  try {
    const { user, token } = await login(email, senha);
    return response(res, { user, token });
  } catch (error) {
    return handleError(res, error, 401);
  }
};

export { getUsers, createUser, getUserById, updateUser, deleteUser, loginUser };
