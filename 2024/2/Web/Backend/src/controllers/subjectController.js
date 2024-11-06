import Subject from '../models/Subject.js';

// Criar uma nova materia
const createSubject = async (req, res) => {
  try {
    const subject = await Subject.create(req.body);
    res.status(201).json(subject);
  } catch (error) {
    res.status(500).json({ error: 'Error creating subject' });
  }
};

// listar todas as materias
const getAllSubjects = async (req, res) => {
  try {
    const subjects = await Subject.findAll();
    res.status(200).json(subjects);
  } catch (error) {
    res.status(500).json({ error: 'Error fetching subjects' });
  }
};

// Pegar materia pelo id
const getSubjectById = async (req, res) => {
  try {
    const subject = await Subject.findByPk(req.params.id);
    if (subject) {
      res.status(200).json(subject);
    } else {
      res.status(404).json({ error: 'Subject not found' });
    }
  } catch (error) {
    res.status(500).json({ error: 'Error fetching subject' });
  }
};

// Update materia
const updateSubject = async (req, res) => {
  try {
    const subject = await Subject.findByPk(req.params.id);
    if (subject) {
      await subject.update(req.body);
      res.status(200).json(subject);
    } else {
      res.status(404).json({ error: 'Subject not found' });
    }
  } catch (error) {
    res.status(500).json({ error: 'Error updating subject' });
  }
};

// Delete materia
const deleteSubject = async (req, res) => {
  try {
    const subject = await Subject.findByPk(req.params.id);
    if (subject) {
      await subject.destroy();
      res.status(204).send();
    } else {
      res.status(404).json({ error: 'Subject not found' });
    }
  } catch (error) {
    res.status(500).json({ error: 'Error deleting subject' });
  }
};

export { createSubject, getAllSubjects, getSubjectById, updateSubject, deleteSubject };
