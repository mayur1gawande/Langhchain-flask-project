/**
 * Scrolls the chat container to the very bottom.
 */
function scrollToBottom() {
    const chatContainer = document.getElementById("chat");
    chatContainer.scrollTop = chatContainer.scrollHeight;
}

/**
 * Handles sending a message to the backend and displaying the response.
 * @param {Event} e The form submission event.
 */
async function sendMessage(e) {
    // Prevent the form from submitting the traditional way
    e.preventDefault(); 
    
    const input = document.getElementById("message-input");
    const chat = document.getElementById("chat");
    const explanationLength = document.getElementById("explanation-length-select").value;
    const userMessage = input.value.trim();

    if (!userMessage) return; // Don't send empty messages

    // 1. Append the user's message to the chat
    const userDiv = document.createElement("div");
    userDiv.className = "message user";
    userDiv.innerHTML = `<p>${userMessage}</p>`; // Use .textContent for security
    chat.appendChild(userDiv);
    
    // Clear the input field and scroll down
    input.value = "";
    scrollToBottom();

    // 2. Display a "typing" indicator for better UX (optional, but nice)
    const typingDiv = document.createElement("div");
    typingDiv.className = "message bot typing-indicator";
    typingDiv.innerHTML = `
        <img src="/static/assistant.png" class="avatar" />
        <p><span>.</span><span>.</span><span>.</span></p>
    `;
    chat.appendChild(typingDiv);
    scrollToBottom();

    // 3. Send the user's message to the Flask backend
    try {
        const response = await fetch("/chat", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ message: userMessage, explaination_length: explanationLength })
        });

        if (!response.ok) {
            throw new Error(`Server responded with status: ${response.status}`);
        }

        const data = await response.json();

        // 4. Create a new div for the bot's actual response
        const botDiv = document.createElement("div");
        botDiv.className = "message bot";
        
        // This is the corrected part:
        // - Use a static path for the image src.
        // - Place the bot's HTML response directly inside a container div.
        botDiv.innerHTML = `
            <img src="/static/assistant.png" class="avatar" />
            <div class="bot-content">${data.response}</div>
        `;
        
        // Replace the "typing" indicator with the actual message
        chat.replaceChild(botDiv, typingDiv);
        scrollToBottom();

    } catch (err) {
        // If an error occurs, show an error message
        typingDiv.innerHTML = `
            <img src="/static/assistant.png" class="avatar" />
            <p>Sorry, I encountered an error. Please try again.</p>
        `;
        console.error("Error contacting assistant:", err);
    }
}