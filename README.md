# AI TypeScript to JavaScript Converter

A powerful, AI-driven tool that converts TypeScript files to clean JavaScript using a local Llama 3 model via Ollama. It features a sleek, modern dark-themed UI built with Streamlit.

-----

## Features

  - **Batch Conversion:** Upload and convert multiple TypeScript files at once.
  - **Snippet Conversion:** Convert individual TypeScript code snippets in real time.
  - **Premium Dark UI:** A sleek, modern interface with glassmorphism effects.
  - **AI-Powered:** Uses the Llama 3 model for intelligent code conversion.
  - **Easy Export:** Download converted files as a ZIP archive.
  - **Privacy-First:** All processing happens locally, with no cloud dependencies.
  - **Fast Processing:** Efficient batch processing with progress tracking.

-----

## Prerequisites

Before running this application, ensure you have:

  - Python 3.8+ installed on your system
  - Ollama installed and running locally
  - Llama 3 model downloaded via Ollama

### Installing Ollama

Visit Ollama's official website and follow the installation instructions for your operating system.

### Setting up Llama 3

After installing Ollama, download the Llama 3 model:

```bash
ollama pull llama3
```

Start the Ollama server:

```bash
ollama serve
```

-----

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/ai-ts-js-converter.git
cd ai-ts-js-converter
```

Create a virtual environment (recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

-----

## Usage

Start the Ollama server (if not already running):

```bash
ollama serve
```

Run the Streamlit application:

```bash
streamlit run app.py
```

Open your browser and navigate to `http://localhost:8501`.

### How to Use

#### Convert Multiple Files (Batch Mode)

1.  Navigate to the "Convert Folder" tab.
2.  Click "Browse files" and select your `.ts` or `.tsx` files.
3.  Click "Convert Files to JavaScript".
4.  Monitor the progress bar during conversion.
5.  Download the converted files as a ZIP archive.

#### Convert Single Snippet

1.  Navigate to the "Convert Single Snippet" tab.
2.  Paste your TypeScript code in the left panel.
3.  Click "Convert Snippet".
4.  View the converted JavaScript code in the right panel.

-----

## Project Structure

```
ai-ts-js-converter/
├── app.py                  # Main Streamlit application
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
└── assets/                 # Static assets (if any)
```

### Dependencies

  - `streamlit` - Web application framework
  - `requests` - HTTP library for Ollama API calls
  - `zipfile` - ZIP file creation and handling
  - `json` - JSON parsing and manipulation
  - `io` - Input/output operations

-----

## UI Features

The application features a premium dark theme with:

  - Glassmorphism effects with subtle transparency and blur.
  - Gradient text headers with shimmer effects.
  - Interactive buttons with hover animations and glow effects.
  - Smooth transitions and micro-interactions.
  - Responsive design that works on all screen sizes.
  - Custom scrollbars matching the dark theme.

-----

## Configuration

### Ollama API Settings

The application connects to Ollama at `http://localhost:11434` by default. To modify the connection settings, update the `ollama_api_url` variable in `app.py`:

```python
ollama_api_url = "http://localhost:11434/api/generate"
```

### Model Configuration

The app uses the `llama3` model by default. To use a different model, modify the payload in the `call_ollama` function:

```python
payload = {
    "model": "your-model-name",  # Change this
    "prompt": prompt,
    "stream": False,
}
```

-----

## Contributing

Contributions are welcome. Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

### Development Setup

1.  Fork the repository.
2.  Create a feature branch (`git checkout -b feature/amazing-feature`).
3.  Make your changes.
4.  Commit your changes (`git commit -m 'Add some amazing feature'`).
5.  Push to the branch (`git push origin feature/amazing-feature`).
6.  Open a Pull Request.

-----

## Troubleshooting

### Common Issues

#### "Error connecting to Ollama"

  - Ensure Ollama is installed and running (`ollama serve`).
  - Check if the Llama 3 model is downloaded (`ollama list`).
  - Verify the API URL is correct (default: `http://localhost:11434`).

#### "Failed to decode JSON from Ollama response"

  - This may indicate an issue with the Ollama model.
  - Try restarting the Ollama server.
  - Ensure you are using a compatible model.

#### "Files not converting properly"

  - Make sure uploaded files are valid TypeScript (`.ts` or `.tsx`).
  - Check that the files contain valid TypeScript syntax.
  - Large files may take longer to process.

-----

## Future Enhancements

  - Support for additional file types (`.d.ts`, `.vue`, etc.).
  - Custom conversion rules and preferences.
  - Real-time preview during batch conversion.
  - Integration with other AI models (GPT-4, Claude, etc.).
  - Syntax highlighting in code preview areas.
  - Export options (individual files, different formats).
  - Conversion history and session management.

-----

## Support

If you encounter any issues or have questions:

  - Check the [Issues page](https://www.google.com/search?q=https://github.com/yourusername/ai-ts-js-converter/issues).
  - Create a new issue with detailed information about your problem.
  - Include your system information and error messages.

-----

## Acknowledgments

  - Streamlit for the web application framework.
  - Ollama for local AI model serving.
  - Meta for the Llama 3 model.
  - The open-source community for inspiration and resources.
