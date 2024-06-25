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
