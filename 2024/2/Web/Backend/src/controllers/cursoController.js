// ./controllers/cursoController.js

import Courses from '../models/Cursos.js';
import { handleError, response } from '../Utils/Utils.js';

const getCourses = async (req, res) => {
  try {
    const courses = await Courses.findAll();
    return response(res, courses);
  } catch (error) {
    return handleError(res, error);
  }
};

const createCourse = async (req, res) => {
  try {
    const course = await Courses.create(req.body);
    return response(res, course, 201);
  } catch (error) {
    return handleError(res, error);
  }
};

const getCourseById = async (req, res) => {
  const { id } = req.params;
  try {
    const course = await Courses.findByPk(id);
    if (!course) {
      return response(res, { message: 'Curso não encontrado' }, 404);
    }
    return response(res, course);
  } catch (error) {
    return handleError(res, error);
  }
};

const updateCourse = async (req, res) => {
  const { id } = req.params;
  try {
    const [updated] = await Courses.update(req.body, { where: { id_curso: id } });
    if (!updated) {
      return response(res, { message: 'Curso não encontrado' }, 404);
    }
    const updatedCourse = await Courses.findByPk(id);
    return response(res, updatedCourse);
  } catch (error) {
    handleError(res, error);
  }
};

const deleteCourse = async (req, res) => {
  const { id } = req.params;
  try {
    const deleted = await Courses.destroy({ where: { id_curso: id } });
    if (!deleted) {
      return response(res, { message: 'Curso não encontrado' }, 404);
    }
    res.status(204).send();
  } catch (error) {
    handleError(res, error);
  }
};

export { getCourses, createCourse, getCourseById, updateCourse, deleteCourse };
