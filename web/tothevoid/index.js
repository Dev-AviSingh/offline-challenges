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
  console.log(`Server is running on port ${PORT}`);
});
