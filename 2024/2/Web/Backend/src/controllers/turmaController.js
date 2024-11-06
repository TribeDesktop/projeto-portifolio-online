import Classes from '../models/Turmas.js';
import { response, handleError } from '../Utils/Utils.js';

const getTurmas = async (req, res) => {
  try {
    const classes = await Classes.findAll();
    return response(res, classes);
  } catch (error) {
    return handleError(res, error);
  }
};

const createTurma = async (req, res) => {
  try {
    const { class_name, academic_year, course_id, schedule, room, responsible_teacher, max_capacity } = req.body;

    // TODO: preciso criar uma logica para verificar se um professor ja tem uma turma num determinado horario
    // estou esperando o banco criar uma tabela professor

    const newClass = await Classes.create({
      nome_turma: class_name,
      ano_letivo: academic_year,
      id_curso: course_id,
      horario: schedule,
      sala: room,
      professor_responsavel: responsible_teacher,
      capacidade_maxima: max_capacity,
    });

    return response(res, newClass, 201);
  } catch (error) {
    return handleError(res, error);
  }
};

const getTurmaById = async (req, res) => {
  try {
    const { id } = req.params;

    const classById = await Classes.findByPk(id);
    if (!classById) {
      return response(res, { message: 'Class not found.' }, 404);
    }
    return response(res, classById);
  } catch (error) {
    return handleError(res, error);
  }
};

const updateTurma = async (req, res) => {
  try {
    const { id } = req.params;
    const { class_name, academic_year, course_id, schedule, room, responsible_teacher, max_capacity } = req.body;

    const classById = await Classes.findByPk(id);
    if (!classById) {
      return response(res, { message: 'Class not found.' }, 404);
    }

    const updatedClass = await Classes.create({
      nome_turma: class_name,
      ano_letivo: academic_year,
      id_curso: course_id,
      horario: schedule,
      sala: room,
      professor_responsavel: responsible_teacher,
      capacidade_maxima: max_capacity,
    });

    await Classes.update(updatedClass, { where: { id_turma: id } });
    return response(res, { message: 'Class updated successfully.' });
  } catch (error) {
    return handleError(res, error);
  }
};

const deleteTurma = async (req, res) => {
  try {
    const { id } = req.params;
    const deleted = await Classes.destroy({ where: { id_turma: id } });
    if (!deleted) {
      return response(res, { message: 'Class not found.' }, 404);
    }
    res.status(204).send();
  } catch (error) {
    return handleError(res, error);
  }
};

export { getTurmas, createTurma, getTurmaById, updateTurma, deleteTurma };
