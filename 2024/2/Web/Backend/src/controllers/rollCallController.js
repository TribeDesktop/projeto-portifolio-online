import { ValidationErrorItem } from 'sequelize';
import RollCall from '../models/RollCall.js';

const getRollCall = async (req, res) => {
  try {
    const rollCall = await RollCall.findAll();
    res.status(200).json(rollCall);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
};

const createRollCall = async (req, res) => {
  try {
    const rollCalls = await RollCall.create(req.body);
    res.status(201).json(rollCalls);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
};

const updateRollCall = async (req, res) => {
  try {
    const rollCall = await RollCall.findByPk(req.params.id);
    if (!rollCall) {
      return res.status(404).json({ error: 'Chamada não encontrada.' });
    }
    await rollCall.update(req.body);
    res.status(200).json(RollCall);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
};

const getRollCallById = async (req, res) => {
  const { id } = req.params;

  try {
    const rollCall = await RollCall.findByPk(id);
    if (!rollCall) {
      return res.status(404).json({ message: 'Chamada não encontrada.' });
    }
    res.status(200).json(rollCall);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
};

const deleteRollCall = async (req, res) => {
  try {
    const rollCall = await RollCall.findByPk(req.params.id);
    if (!rollCall) {
      return res.status(404).json({ message: 'Chamada não encontrada.' });
    }
    await rollCall.destroy();
    res.status(204).send();
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
};

export { getRollCall, createRollCall, updateRollCall, getRollCallById, deleteRollCall };
