
// navbar.js.. no need for phone
document.querySelectorAll('.dropdown > a').forEach(link => {
  link.addEventListener('click', function(e) {
    if(window.innerWidth <= 768){
      e.preventDefault();
      const dropdown = this.nextElementSibling;
      dropdown.style.display = dropdown.style.display === 'block' ? 'none' : 'block';
    }
  });
});



function toggleChat() {
  const box = document.getElementById("chatBox");
  box.style.display = box.style.display === "flex" ? "none" : "flex";
}

async function sendMessage() {
  const input = document.getElementById("userInput");
  const message = input.value;
  if (!message) return;

  addMessage(message, "user");
  input.value = "";

  const response = await fetch("/chat", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message: message }),
  });

  const data = await response.json();
  addMessage(data.response, "bot");
}

function addMessage(text, sender) {
  const messages = document.getElementById("messages");
  const msgDiv = document.createElement("div");
  msgDiv.classList.add("message", sender,);
  msgDiv.innerText = text;
  messages.appendChild(msgDiv);
  messages.scrollTop = messages.scrollHeight;
}
