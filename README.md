
# 💬 AI Chatbot with Spline Animation

An elegant and interactive AI chatbot UI built with **React.js**, styled using modern **CSS**, and enhanced visually with **Spline 3D animation**. Designed for both functionality and visual appeal.

## 🌟 Features

- ⚡ Fast, responsive chat UI
- 💡 Integrated with a modern LLM API (e.g., Gemini Pro / Together.ai)
- 🎨 Stunning real-time 3D animation using [Spline](https://spline.design/)
- 🌈 Gradient design and soft UI
- 📜 Scrollable chat history with clean layout
- 📱 Mobile responsive structure (desktop-first currently)
- 🧠 Memory-friendly, built for future API integrations

## 📁 Project Structure

```
root/
├── public/
├── src/
│   ├── components/
│   ├── App.jsx
│   ├── main.jsx
│   └── styles/
│       └── chatbot.css
├── index.html
└── vite.config.js
```

## 🚀 Getting Started

1. **Clone the repo**

```bash
git clone https://github.com/yourusername/your-chatbot-repo.git
cd your-chatbot-repo
```

2. **Install dependencies**

```bash
npm install
```

3. **Run the development server**

```bash
npm run dev
```

## 🔧 API Integration

This project is ready to support integration with any LLM API. So far, models like Gemini Pro or Together.ai’s LLaMA 4 have been integrated. For example:

```javascript
const response = await fetch("https://api.together.xyz/inference", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    Authorization: `Bearer ${your_API_key}`,
  },
  body: JSON.stringify({
    model: "meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8",
    prompt: yourPrompt,
    max_tokens: 1024,
    temperature: 0.7,
  }),
});

## 🛠 Built With

- [React.js](https://reactjs.org/)
- [Vite](https://vitejs.dev/)
- [Spline](https://spline.design/)
- [Inter Font](https://fonts.google.com/specimen/Inter)

## 📬 Contact

Have questions or feedback? Reach out on](https://www.linkedin.com/in/caamoghjain) or open an issue!

---

**MIT License** © 2025  
Made with ❤️ by C A Amogh Jain
