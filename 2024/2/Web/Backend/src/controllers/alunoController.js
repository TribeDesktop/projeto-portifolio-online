import Students from '../models/Alunos.js';
import { handleError, response } from '../Utils/Utils.js';

const getStudents = async (req, res) => {
  try {
    const students = await Students.findAll();
    return response(res, students);
  } catch (error) {
    return handleError(res, error);
  }
};

const createStudent = async (req, res) => {
  try {
    const student = await Students.create(req.body);
    return response(res, student, 201);
  } catch (error) {
    return handleError(res, error);
  }
};

const getStudentById = async (req, res) => {
  const { id } = req.params;
  try {
    const student = await Students.findByPk(id);
    if (!student) {
      return response(res, { message: 'Aluno não encontrado' }, 404);
    }
    return response(res, student);
  } catch (error) {
    console.log(error);
    return handleError(res, error);
  }
};

const updateStudent = async (req, res) => {
  const { id } = req.params;
  try {
    const [updated] = await Students.update(req.body, { where: { id_aluno: id } });
    if (!updated) {
      return response(res, { message: 'Aluno não encontrado' }, 404);
    }
    const updatedStudent = await Students.findByPk(id);
    res.json(updatedStudent);
    return response(res, updateStudent);
  } catch (error) {
    handleError(res, error);
  }
};

const deleteStudent = async (req, res) => {
  const { id } = req.params;
  try {
    const deleted = await Students.destroy({ where: { id_aluno: id } });
    if (!deleted) {
      return response(res, { message: 'Aluno não encontrado' }, 404);
    }
    res.status(204).send();
  } catch (error) {
    handleError(res, error);
  }
};

export { getStudents, createStudent, getStudentById, updateStudent, deleteStudent };
