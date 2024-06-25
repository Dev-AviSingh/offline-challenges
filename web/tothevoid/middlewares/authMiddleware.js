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
