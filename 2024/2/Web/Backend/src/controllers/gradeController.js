import Grade from '../models/Grade.js';

// Criar uma nova nota
const createGrade = async (req, res) => {
  try {
    const grade = await Grade.create(req.body);
    res.status(201).json(grade);
  } catch (error) {
    res.status(500).json({ error: 'Error creating grade' });
  }
};

// Listar todas as notas
const getAllGrades = async (req, res) => {
  try {
    const grades = await Grade.findAll();
    res.status(200).json(grades);
  } catch (error) {
    res.status(500).json({ error: 'Error fetching grades' });
  }
};

// Pegar nota pelo id
const getGradeById = async (req, res) => {
  try {
    const grade = await Grade.findByPk(req.params.id);
    if (grade) {
      res.status(200).json(grade);
    } else {
      res.status(404).json({ error: 'Grade not found' });
    }
  } catch (error) {
    res.status(500).json({ error: 'Error fetching grade' });
  }
};

// Atualizar nota
const updateGrade = async (req, res) => {
  try {
    const grade = await Grade.findByPk(req.params.id);
    if (grade) {
      await grade.update(req.body);
      res.status(200).json(grade);
    } else {
      res.status(404).json({ error: 'Grade not found' });
    }
  } catch (error) {
    res.status(500).json({ error: 'Error updating grade' });
  }
};

// Deletar nota
const deleteGrade = async (req, res) => {
  try {
    const grade = await Grade.findByPk(req.params.id);
    if (grade) {
      await grade.destroy();
      res.status(204).send();
    } else {
      res.status(404).json({ error: 'Grade not found' });
    }
  } catch (error) {
    res.status(500).json({ error: 'Error deleting grade' });
  }
};

export { createGrade, getAllGrades, getGradeById, updateGrade, deleteGrade };
