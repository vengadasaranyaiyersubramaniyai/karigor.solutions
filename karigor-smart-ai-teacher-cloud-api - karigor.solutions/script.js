function sendMessage() {
    const userInput = document.getElementById('user-input').value;
    displayMessage('user', userInput);
    fetch('/api/chat', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ message: userInput })
    })
    .then(response => response.json())
    .then(data => {
      displayMessage('bot', data.message);
    })
    .catch(error => {
      console.error('Error:', error);
    });
  }
  
  function displayMessage(sender, message) {
    const chatBox = document.getElementById('chat-box');
    const messageElement = document.createElement('div');
    messageElement.classList.add(sender === 'user' ? 'user-message' : 'bot-message');
    messageElement.innerText = message;
    chatBox.appendChild(messageElement);
  }
  