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
