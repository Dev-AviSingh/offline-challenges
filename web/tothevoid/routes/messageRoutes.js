const express = require('express');
const { postMessage, getMessages } = require('../controllers/messageController');
const { authMiddleware } = require('../middlewares/authMiddleware');

const router = express.Router();

router.post('/', authMiddleware, postMessage);
router.get('/', getMessages);

module.exports = router;
