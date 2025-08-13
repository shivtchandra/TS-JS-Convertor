# AI TypeScript to JavaScript Converter

A powerful, AI-driven tool that converts **TypeScript** files to clean **JavaScript** using a local **Llama 3** model via **Ollama**.  
Features a sleek, modern **dark-themed UI** built with **Streamlit**.

---

## ✨ Features
- **Batch Conversion** – Upload and convert multiple TypeScript files at once.
- **Snippet Conversion** – Convert individual TypeScript code snippets in real-time.
- **Premium Dark UI** – Sleek, modern interface with **glassmorphism effects**.
- **AI-Powered** – Uses **Llama 3** model for intelligent code conversion.
- **Easy Export** – Download converted files as a ZIP archive.
- **Privacy-First** – All processing happens locally, no cloud dependencies.
- **Fast Processing** – Efficient batch processing with progress tracking.

---

## 📋 Prerequisites
Before running this application, ensure you have:
- **Python 3.8+** installed on your system.
- **Ollama** installed and running locally.
- **Llama 3** model downloaded via Ollama.

---

## ⚡ Installing Ollama
Visit **[Ollama’s official website](https://ollama.ai)** and follow the installation instructions for your OS.

After installing, download the Llama 3 model:
```bash
ollama pull llama3
Start the Ollama server:

bash
Copy
Edit
ollama serve
📥 Installation
Clone the repository:

bash
Copy
Edit
git clone https://github.com/yourusername/ai-ts-js-converter.git
cd ai-ts-js-converter
Create a virtual environment (recommended):

bash
Copy
Edit
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
🚀 Usage
Start the Ollama server (if not already running):

bash
Copy
Edit
ollama serve
Run the Streamlit application:

bash
Copy
Edit
streamlit run app.py
Open your browser and go to:

arduino
Copy
Edit
http://localhost:8501
🖥 How to Use
Convert Multiple Files (Batch Mode)
Go to the "Convert Folder" tab.

Click "Browse files" and select .ts or .tsx files.

Click "Convert Files to JavaScript".

Watch the progress bar.

Download the converted files as a ZIP archive.

Convert Single Snippet
Go to the "Convert Single Snippet" tab.

Paste your TypeScript code in the left panel.

Click "Convert Snippet".

View the converted JavaScript code in the right panel.

📁 Project Structure
bash
Copy
Edit
ai-ts-js-converter/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── README.md           # Project documentation
└── assets/             # Static assets (if any)
📦 Dependencies
streamlit – Web application framework.

requests – HTTP library for Ollama API calls.

zipfile – ZIP file creation and handling.

json – JSON parsing and manipulation.

io – Input/output operations.

🎨 UI Features
Glassmorphism effects with subtle transparency and blur.

Gradient text headers with shimmer effects.

Interactive buttons with hover animations & glow.

Smooth transitions and micro-interactions.

Responsive design for all screen sizes.

Custom scrollbars matching the dark theme.

⚙️ Configuration
Ollama API Settings
The app connects to Ollama at:

python
Copy
Edit
ollama_api_url = "http://localhost:11434/api/generate"
Modify in app.py if needed.

Model Configuration
Uses llama3 by default.
Change in call_ollama function:

python
Copy
Edit
payload = {
    "model": "your-model-name",  # Change this
    "prompt": prompt,
    "stream": False,
}
🤝 Contributing
Contributions are welcome!

Fork the repository.

Create a branch:

bash
Copy
Edit
git checkout -b feature/amazing-feature
Make changes and commit:

bash
Copy
Edit
git commit -m "Add some amazing feature"
Push:

bash
Copy
Edit
git push origin feature/amazing-feature
Open a Pull Request.

🛠 Troubleshooting
"Error connecting to Ollama"
Ensure Ollama is installed and running:

bash
Copy
Edit
ollama serve
Check Llama 3 is downloaded:

bash
Copy
Edit
ollama list
Verify API URL is correct (default: http://localhost:11434).

"Failed to decode JSON from Ollama response"
Restart Ollama server.

Use a compatible model.

Files not converting properly
Ensure uploaded files are valid .ts or .tsx.

Check TypeScript syntax.

Large files may take longer.

🔮 Future Enhancements
Support for additional file types (.d.ts, .vue, etc.).

Custom conversion rules and preferences.

Real-time preview during batch conversion.

Integration with other AI models (GPT-4, Claude, etc.).

Syntax highlighting in preview.

Export options in multiple formats.

Conversion history and session management.

❤️ Acknowledgments
Streamlit – Web framework.

Ollama – Local AI model serving.

Meta – Llama 3 model.

Open-source community – Inspiration & resources.

⭐ Star this repo if you found it helpful!
