const { messages } = require('../models/messageModel');
const { verifyToken } = require('../utils/jwtUtils');

exports.updateMessage = (req, res) => {
  const token = req.headers.authorization.split(' ')[1];
  const decoded = verifyToken(token);

  if (decoded.admin !== 1) {
    return res.status(403).json({ message: 'Forbidden' });
  }

  const { id, content, date, likes } = req.body;
  const message = messages.find(msg => msg.id === id);

  if (message) {
    if (content) message.content = content;
    if (date) message.date = new Date(date);
    if (likes) message.likes = likes;
    res.status(200).json(message);
  } else {
    res.status(404).json({ message: 'Message not found' });
  }
};
