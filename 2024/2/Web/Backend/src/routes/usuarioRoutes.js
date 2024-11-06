import express from 'express';
import {
  getUsers,
  createUser,
  getUserById,
  updateUser,
  deleteUser,
  loginUser,
} from '../controllers/usuarioController.js';

const router = express.Router();

/**
 * @swagger
 * tags:
 *   name: Usuarios
 *   description: Rota para gerenciamento de usuários
 */

/**
 * @swagger
 * /usuarios:
 *   get:
 *     summary: Obtém todos os usuários
 *     tags: [Usuarios]
 *     responses:
 *       200:
 *         description: Lista de todos os usuários
 *       500:
 *         description: Erro ao obter os usuários
 */
router.get('/usuarios', getUsers);

/**
 * @swagger
 * /usuarios:
 *   post:
 *     summary: Cria um novo usuário
 *     tags: [Usuarios]
 *     requestBody:
 *       required: true
 *       content:
 *         application/json:
 *           schema:
 *             type: object
 *             properties:
 *               nome_completo:
 *                 type: string
 *               email:
 *                 type: string
 *               senha:
 *                 type: string
 *               tipo_usuario:
 *                 type: string
 *               status:
 *                 type: string
 *               caminho_da_foto:
 *                 type: string
 *     responses:
 *       201:
 *         description: Usuário criado com sucesso
 *       400:
 *         description: Email já cadastrado
 *       500:
 *         description: Erro ao criar o usuário
 */
router.post('/usuarios', createUser);

/**
 * @swagger
 * /usuarios/{id}:
 *   get:
 *     summary: Obtém um usuário pelo ID
 *     tags: [Usuarios]
 *     parameters:
 *       - in: path
 *         name: id
 *         schema:
 *           type: integer
 *         required: true
 *         description: ID do usuário
 *     responses:
 *       200:
 *         description: Dados do usuário
 *       404:
 *         description: Usuário não encontrado
 *       500:
 *         description: Erro ao buscar o usuário
 */
router.get('/usuarios/:id', getUserById);

/**
 * @swagger
 * /usuarios/{id}:
 *   put:
 *     summary: Atualiza um usuário pelo ID
 *     tags: [Usuarios]
 *     parameters:
 *       - in: path
 *         name: id
 *         schema:
 *           type: integer
 *         required: true
 *         description: ID do usuário
 *     requestBody:
 *       required: true
 *       content:
 *         application/json:
 *           schema:
 *             type: object
 *             properties:
 *               nome_completo:
 *                 type: string
 *               email:
 *                 type: string
 *               senha:
 *                 type: string
 *               tipo_usuario:
 *                 type: string
 *               status:
 *                 type: string
 *               caminho_da_foto:
 *                 type: string
 *     responses:
 *       200:
 *         description: Usuário atualizado com sucesso
 *       404:
 *         description: Usuário não encontrado
 *       500:
 *         description: Erro ao atualizar o usuário
 */
router.put('/usuarios/:id', updateUser);

/**
 * @swagger
 * /usuarios/{id}:
 *   delete:
 *     summary: Exclui um usuário pelo ID
 *     tags: [Usuarios]
 *     parameters:
 *       - in: path
 *         name: id
 *         schema:
 *           type: integer
 *         required: true
 *         description: ID do usuário
 *     responses:
 *       204:
 *         description: Usuário excluído com sucesso
 *       404:
 *         description: Usuário não encontrado
 *       500:
 *         description: Erro ao excluir o usuário
 */
router.delete('/usuarios/:id', deleteUser);

/**
 * @swagger
 * /usuarios/login:
 *   post:
 *     summary: Realiza o login de um usuário
 *     tags: [Usuarios]
 *     requestBody:
 *       required: true
 *       content:
 *         application/json:
 *           schema:
 *             type: object
 *             properties:
 *               email:
 *                 type: string
 *               senha:
 *                 type: string
 *     responses:
 *       200:
 *         description: Login realizado com sucesso
 *       401:
 *         description: Credenciais inválidas
 *       500:
 *         description: Erro ao realizar o login
 */
router.post('/usuarios/login', loginUser);


/**
 * @swagger
 * components:
 *   schemas:
 *     Usuario:
 *       type: object
 *       required:
 *         - nome_completo
 *         - email
 *         - senha
 *       properties:
 *         id_usuario:
 *           type: integer
 *           description: ID do usuário (auto-incrementado)
 *         nome_completo:
 *           type: string
 *           description: Nome completo do usuário
 *         email:
 *           type: string
 *           description: Endereço de e-mail do usuário
 *         senha:
 *           type: string
 *           description: Senha do usuário
 *         tipo_usuario:
 *           type: string
 *           description: Tipo do usuário (admin, estudante, etc.)
 *         status:
 *           type: string
 *           description: Status do usuário (ativo ou inativo)
 *         caminho_da_foto:
 *           type: string
 *           description: Caminho para a foto de perfil do usuário
 *       example:
 *         nome_completo: "João Pereira"
 *         email: "joao@exemplo.com"
 *         senha: "senha123"
 *         tipo_usuario: "estudante"
 *         status: "ativo"
 *         caminho_da_foto: "/fotos/joao_pereira.jpg"
 */


export default router;
