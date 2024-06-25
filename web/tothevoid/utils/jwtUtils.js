const jwt = require('jsonwebtoken');

const secret = 'your_jwt_secret';

exports.generateToken = (user) => {
  return jwt.sign({ username: user.username, admin: user.admin }, secret, { expiresIn: '1h' });
};

exports.verifyToken = (token) => {
  return jwt.verify(token, secret);
};
