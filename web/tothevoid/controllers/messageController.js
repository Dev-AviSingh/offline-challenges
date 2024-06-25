const { messages, Message } = require('../models/messageModel');
const { verifyToken } = require('../utils/jwtUtils');
// const { resizeAndConvertImage } = require('../utils/imageUtils');

exports.postMessage = async (req, res) => {
  const token = req.headers.authorization.split(' ')[1];
  const decoded = verifyToken(token);
  const { content, profilePic } = req.body;

  // const resizedPic = await resizeAndConvertImage(profilePic);
  const message = new Message(content, decoded.username, profilePic);
  messages.push(message);

  res.status(201).json(message);
};

exports.getMessages = (req, res) => {
  const currentDate = new Date();
  const filteredMessages = messages.filter(message => {
    const messageDate = new Date(message.date);
    const differenceInTime = currentDate - messageDate;
    const differenceInDays = differenceInTime / (1000 * 3600 * 24);
    return differenceInDays <= 2;
  });

  res.render('messages', { messages: filteredMessages });
};
