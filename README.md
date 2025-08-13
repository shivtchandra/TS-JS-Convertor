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
git clone https://github.com/shivtchandra/TS-JS-Convertor.git
cd TS-JS-Convertor
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
2.  Click the **"Browse files"** button and select your `.ts` or `.tsx` files.
3.  Click the **"Convert Files to JavaScript"** button.
4.  Monitor the progress bar during conversion.
5.  Download the converted files as a ZIP archive.

#### Convert Single Snippet

1.  Navigate to the "Convert Single Snippet" tab.
2.  Paste your TypeScript code into the left panel.
3.  Click the **"Convert Snippet"** button.
4.  View the converted JavaScript code in the right panel.

-----

## Project Structure

```
TS-JS-Convertor/
├── app.py                  # Main Streamlit application
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

### Dependencies

  - `streamlit` - Web application framework
  - `requests` - HTTP library for Ollama API calls
  - `zipfile` - ZIP file creation and handling
  - `json` - JSON parsing and manipulation
  - `io` - Input/output operations

-----

## Configuration

### Ollama API Settings

The application connects to Ollama at `http://localhost:11434` by default. To modify the connection settings, update the `ollama_api_url` variable in `app.py`.

### Model Configuration

The app uses the `llama3` model by default. To use a different model, modify the payload in the `call_ollama` function in `app.py`.

-----

## Contributing

Contributions are welcome. Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

-----

## Troubleshooting

### Common Issues

  - **"Error connecting to Ollama"**: Ensure Ollama is installed and running (`ollama serve`).
  - **"Failed to decode JSON from Ollama response"**: This may indicate an issue with the Ollama model. Try restarting the Ollama server.
  - **"Files not converting properly"**: Make sure uploaded files are valid TypeScript (`.ts` or `.tsx`).

-----

## Acknowledgments

  - **Streamlit** for the web application framework.
  - **Ollama** for local AI model serving.
  - **Meta** for the Llama 3 model.
