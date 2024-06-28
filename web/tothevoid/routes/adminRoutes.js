const express = require('express');
const { updateMessage } = require('../controllers/adminController');
const { authMiddleware } = require('../middlewares/authMiddleware');

const router = express.Router();

router.put('/message', authMiddleware, updateMessage);

module.exports = router;
