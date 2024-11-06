import express from 'express';

import {
  createSubject,
  getAllSubjects,
  getSubjectById,
  updateSubject,
  deleteSubject,
} from '../controllers/subjectController.js';

const router = express.Router();

// Criar uma nova matéria
router.post('/', createSubject);

// Route para listar materias
router.get('/', getAllSubjects);

// Route para pegar materia pelo id
router.get('/:id', getSubjectById);

// Route para atualizar materia
router.put('/:id', updateSubject);

// Route para apagar a materia
router.delete('/:id', deleteSubject);

export default router;
