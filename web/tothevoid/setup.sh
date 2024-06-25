#!/bin/bash

# Create directories
mkdir -p controllers middlewares models routes utils views

# Create index.js
cat > index.js <<EOL
const express = require('express');
const bodyParser = require('body-parser');
const authRoutes = require('./routes/authRoutes');
const messageRoutes = require('./routes/messageRoutes');
const adminRoutes = require('./routes/adminRoutes');

const app = express();
const PORT = process.env.PORT || 3000;

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

app.set('view engine', 'ejs');

app.use('/auth', authRoutes);
app.use('/messages', messageRoutes);
app.use('/admin', adminRoutes);

app.get('/', (req, res) => {
  res.redirect('/messages');
});

app.listen(PORT, () => {
  console.log(\`Server is running on port \${PORT}\`);
});
EOL

# Create controllers/authController.js
cat > controllers/authController.js <<EOL
const bcrypt = require('bcryptjs');
const jwt = require('jsonwebtoken');
const { generateToken } = require('../utils/jwtUtils');

const users = []; // In-memory user store

exports.register = async (req, res) => {
  if (req.method === 'GET') {
    res.render('register');
  } else {
    const { username, password } = req.body;
    const hashedPassword = await bcrypt.hash(password, 10);
    const user = { username, password: hashedPassword, admin: 0 };
    users.push(user);
    const token = generateToken(user);
    res.status(201).json({ token });
  }
};

exports.login = async (req, res) => {
  if (req.method === 'GET') {
    res.render('login');
  } else {
    const { username, password } = req.body;
    const user = users.find(u => u.username === username);
    if (user && await bcrypt.compare(password, user.password)) {
      const token = generateToken(user);
      res.status(200).json({ token });
    } else {
      res.status(401).json({ message: 'Invalid username or password' });
    }
  }
};
EOL

# Create utils/jwtUtils.js
cat > utils/jwtUtils.js <<EOL
const jwt = require('jsonwebtoken');

const secret = 'your_jwt_secret';

exports.generateToken = (user) => {
  return jwt.sign({ username: user.username, admin: user.admin }, secret, { expiresIn: '1h' });
};

exports.verifyToken = (token) => {
  return jwt.verify(token, secret);
};
EOL

# Create routes/authRoutes.js
cat > routes/authRoutes.js <<EOL
const express = require('express');
const { register, login } = require('../controllers/authController');

const router = express.Router();

router.get('/register', register);
router.post('/register', register);
router.get('/login', login);
router.post('/login', login);

module.exports = router;
EOL

# Create models/messageModel.js
cat > models/messageModel.js <<EOL
const messages = []; // In-memory message store

class Message {
  constructor(content, username, profilePic) {
    this.content = content;
    this.date = new Date();
    this.username = username;
    this.likes = 0;
    this.profilePic = profilePic;
  }
}

exports.messages = messages;
exports.Message = Message;
EOL

# Create controllers/messageController.js
cat > controllers/messageController.js <<EOL
const { messages, Message } = require('../models/messageModel');
const { verifyToken } = require('../utils/jwtUtils');
const { resizeAndConvertImage } = require('../utils/imageUtils');

exports.postMessage = async (req, res) => {
  const token = req.headers.authorization.split(' ')[1];
  const decoded = verifyToken(token);
  const { content, profilePic } = req.body;

  const resizedPic = await resizeAndConvertImage(profilePic);
  const message = new Message(content, decoded.username, resizedPic);
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
EOL

# Create routes/messageRoutes.js
cat > routes/messageRoutes.js <<EOL
const express = require('express');
const { postMessage, getMessages } = require('../controllers/messageController');
const { authMiddleware } = require('../middlewares/authMiddleware');

const router = express.Router();

router.post('/', authMiddleware, postMessage);
router.get('/', getMessages);

module.exports = router;
EOL

# Create middlewares/authMiddleware.js
cat > middlewares/authMiddleware.js <<EOL
const { verifyToken } = require('../utils/jwtUtils');

exports.authMiddleware = (req, res, next) => {
  try {
    const token = req.headers.authorization.split(' ')[1];
    verifyToken(token);
    next();
  } catch (error) {
    res.status(401).json({ message: 'Unauthorized' });
  }
};
EOL

# Create controllers/adminController.js
cat > controllers/adminController.js <<EOL
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
EOL

# Create routes/adminRoutes.js
cat > routes/adminRoutes.js <<EOL
const express = require('express');
const { updateMessage } = require('../controllers/adminController');
const { authMiddleware } = require('../middlewares/authMiddleware');

const router = express.Router();

router.put('/message', authMiddleware, updateMessage);

module.exports = router;
EOL

# Create utils/imageUtils.js
cat > utils/imageUtils.js <<EOL
const sharp = require('sharp');

exports.resizeAndConvertImage = async (imageBase64) => {
  const buffer = Buffer.from(imageBase64, 'base64');
  const resizedBuffer = await sharp(buffer)
    .resize(50, 50)
    .toFormat('jpeg')
    .toBuffer();
  return resizedBuffer.toString('base64');
};
EOL

# Create views/messages.ejs
cat > views/messages.ejs <<EOL
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Messages</title>
</head>
<body>
  <h1>Messages</h1>
  <a href="/auth/register">Register</a> | <a href="/auth/login">Login</a>
  <div id="messages">
    <% if (messages.length > 0) { %>
      <ul>
        <% messages.forEach(message => { %>
          <li>
            <img src="data:image/jpeg;base64,<%= message.profilePic %>" alt="Profile Pic" width="50" height="50">
            <p><strong><%= message.username %>:</strong> <%= message.content %></p>
            <p>Posted on: <%= new Date(message.date).toLocaleString() %></p>
            <p>Likes: <%= message.likes %></p>
          </li>
        <% }); %>
      </ul>
    <% } else { %>
      <p>No messages available.</p>
    <% } %>
  </div>
</body>
</html>
EOL

# Create views/register.ejs
cat > views/register.ejs <<EOL
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Register</title>
</head>
<body>
  <h1>Register</h1>
  <form action="/auth/register" method="post">
    <div>
      <label for="username">Username:</label>
      <input type="text" id="username" name="username" required>
    </div>
    <div>
      <label for="password">Password:</label>
      <input type="password" id="password" name="password" required>
    </div>
    <button type="submit">Register</button>
  </form>
  <a href="/auth/login">Already have an account? Login</a>
</body>
</html>
EOL

# Create views/login.ejs
cat > views/login.ejs <<EOL
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Login</title>
</head>
<body>
  <h1>Login</h1>
  <form action="/auth/login" method="post">
    <div>
      <label for="username">Username:</label>
      <input type="text" id="username" name="username" required>
    </div>
    <div>
      <label for="password">Password:</label>
      <input type="password" id="password" name="password" required>
    </div>
    <button type="submit">Login</button>
  </form>
  <a href="/auth/register">Don't have an account? Register</a>
</body>
</html>
EOL

echo "Project setup completed!"
