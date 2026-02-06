**Project Overview**
This project is a web-based AI chatbot application built using Flask (Python backend) and a Captain America–themed interactive frontend. The chatbot integrates with Google Gemini AI (Generative AI API) to provide intelligent, real-time responses to user queries in a fun and engaging superhero-style interface.

Key Features

💬 Real-time AI Chatbot powered by Google Gemini

🎨 Stunning Captain America themed UI with shield and star design

⚡ Fast and responsive message exchange

🔄 Seamless communication between frontend and Flask backend

🧠 AI-generated intelligent responses

📜 Markdown-supported AI replies

🌐 Web-based application accessible via browser

🛠 Built with Flask, JavaScript, HTML & CSS

**Technologies Used**

Backend:

Python

Flask

Google GenAI SDK

Flask-CORS

Frontend:

HTML5

CSS3

JavaScript

Marked.js (for Markdown rendering)

How It Works

The user enters a message in the chat interface.

The message is sent to the Flask backend using a POST request.

The backend forwards the text to the Gemini AI model.

Gemini processes the input and generates a response.

The response is returned to the frontend and displayed in the chat window.

**Project Structure**
project/
│
├── main.py               # Flask backend
│
└── templates/
      └── index.html      # Captain America themed UI

**Setup Instructions**

Install required packages:

pip install flask flask-cors google-genai


Add your Gemini API key in main.py

Run the application:

python main.py


Open in browser:

http://127.0.0.1:5000

**Purpose of the Project**

This project demonstrates:

Integration of modern AI models with web applications

Building interactive chatbot systems

Frontend–backend communication using REST APIs

Creative UI design with superhero theming

Future Enhancements

Voice input support

Chat history saving

Multi-theme Avengers UI

User authentication

Typing animations

Conclusion

The Captain America AI Chatbot combines artificial intelligence with creative design to deliver a fun, interactive, and intelligent chatting experience. It is a great beginner-to-intermediate project showcasing full-stack development and AI integration.
