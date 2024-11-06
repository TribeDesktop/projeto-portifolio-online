import express from 'express';
import {
  getRollCall,
  getRollCallById,
  createRollCall,
  updateRollCall,
  deleteRollCall,
} from '../controllers/rollCallController.js';

const router = express.Router();

router.get('/', getRollCall);
router.post('/', createRollCall);
router.get('/:id', getRollCallById);
router.put('/:id', updateRollCall);
router.delete('/:id', deleteRollCall);

export default router;
