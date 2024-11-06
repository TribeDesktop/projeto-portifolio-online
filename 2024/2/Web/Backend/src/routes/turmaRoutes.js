import express from 'express';
import { getTurmas, createTurma, getTurmaById, updateTurma, deleteTurma } from '../controllers/turmaController.js';

const router = express.Router();

/**
 * @swagger
 * tags:
 *   name: Turmas
 *   description: Rota para gerenciamento de turmas
 */


/**
 * @swagger
 * /turmas:
 *   get:
 *     summary: Obtém todas as turmas
 *     tags: [Turmas]
 *     responses:
 *       200:
 *         description: Lista de todas as turmas
 *       500:
 *         description: Erro ao obter as turmas
 */
router.get('/turmas', getTurmas);


/**
 * @swagger
 * /create-turma:
 *   post:
 *     summary: Cria uma nova turma
 *     tags: [Turmas]
 *     requestBody:
 *       required: true
 *       content:
 *         application/json:
 *           schema:
 *             type: object
 *             properties:
 *               class_name:
 *                 type: string
 *               academic_year:
 *                 type: string
 *               course_id:
 *                 type: integer
 *               schedule:
 *                 type: string
 *               room:
 *                 type: string
 *               responsible_teacher:
 *                 type: string
 *               max_capacity:
 *                 type: integer
 *     responses:
 *       201:
 *         description: Turma criada com sucesso
 *       500:
 *         description: Erro ao criar a turma
 */
router.post('/create-turma', createTurma);

/**
 * @swagger
 * /get-turma/{id}:
 *   get:
 *     summary: Obtém uma turma pelo ID
 *     tags: [Turmas]
 *     parameters:
 *       - in: path
 *         name: id
 *         schema:
 *           type: integer
 *         required: true
 *         description: ID da turma
 *     responses:
 *       200:
 *         description: Dados da turma
 *       404:
 *         description: Turma não encontrada
 *       500:
 *         description: Erro ao buscar a turma
 */
router.get('/get-turma/:id', getTurmaById);

/**
 * @swagger
 * /update-turma/{id}:
 *   put:
 *     summary: Atualiza uma turma pelo ID
 *     tags: [Turmas]
 *     parameters:
 *       - in: path
 *         name: id
 *         schema:
 *           type: integer
 *         required: true
 *         description: ID da turma
 *     requestBody:
 *       required: true
 *       content:
 *         application/json:
 *           schema:
 *             type: object
 *             properties:
 *               class_name:
 *                 type: string
 *               academic_year:
 *                 type: string
 *               course_id:
 *                 type: integer
 *               schedule:
 *                 type: string
 *               room:
 *                 type: string
 *               responsible_teacher:
 *                 type: string
 *               max_capacity:
 *                 type: integer
 *     responses:
 *       200:
 *         description: Turma atualizada com sucesso
 *       404:
 *         description: Turma não encontrada
 *       500:
 *         description: Erro ao atualizar a turma
 */
router.put('/update-turma/:id', updateTurma);

/**
 * @swagger
 * /delete-turma/{id}:
 *   delete:
 *     summary: Exclui uma turma pelo ID
 *     tags: [Turmas]
 *     parameters:
 *       - in: path
 *         name: id
 *         schema:
 *           type: integer
 *         required: true
 *         description: ID da turma
 *     responses:
 *       204:
 *         description: Turma excluída com sucesso
 *       404:
 *         description: Turma não encontrada
 *       500:
 *         description: Erro ao excluir a turma
 */
router.delete('/delete-turma/:id', deleteTurma);

/**
 * @swagger
 * components:
 *   schemas:
 *     Turma:
 *       type: object
 *       required:
 *         - nome_turma
 *         - ano_letivo
 *         - id_curso
 *         - capacidade_maxima
 *       properties:
 *         id_turma:
 *           type: integer
 *           description: ID da turma (auto-incrementado)
 *         nome_turma:
 *           type: string
 *           description: Nome da turma
 *         ano_letivo:
 *           type: string
 *           description: Ano letivo da turma
 *         id_curso:
 *           type: integer
 *           description: ID do curso associado à turma
 *         horario:
 *           type: string
 *           description: Horário das aulas da turma
 *         sala:
 *           type: string
 *           description: Sala onde a turma terá as aulas
 *         professor_responsavel:
 *           type: string
 *           description: Nome do professor responsável pela turma
 *         capacidade_maxima:
 *           type: integer
 *           description: Capacidade máxima de alunos na turma
 *       example:
 *         nome_turma: "Turma A"
 *         ano_letivo: "2024"
 *         id_curso: 101
 *         horario: "08:00 - 12:00"
 *         sala: "A1"
 *         professor_responsavel: "Prof. João Silva"
 *         capacidade_maxima: 30
 */

export default router;
