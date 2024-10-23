import Usuarios from '../models/usuarios.js';
import bcrypt from 'bcrypt';
import jwt from 'jsonwebtoken';

const JWT_SECRET = process.env.JWT_SECRET || 'mysecret';

const login = async (email, senha) => {
  const usuario = await Usuarios.findOne({ where: { email } });
  if (!usuario) {
    throw new Error('usuário não encontrado.');
  }

  const passwd = await bcrypt.compare(senha, usuario.senha);
  if (!passwd) {
    throw new Error('senha incorreta.');
  }

  const token = jwt.sign({ id: usuario.id_usuario }, JWT_SECRET, { expiresIn: '1h' });

  return { usuario, token };
};

export { login };
