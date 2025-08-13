import streamlit as st
import requests
import json
import io
import zipfile
import os

# --- Page Configuration ---
st.set_page_config(
    page_title="AI TS-to-JS Converter",
    page_icon="",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- UI Styling ---
st.markdown("""
<style>
    /* Import sleek fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
    
    /* Root Variables for consistent theming */
    :root {
        --pitch-black: #000000;
        --deep-black: #0a0a0a;
        --charcoal: #1a1a1a;
        --dark-grey: #2a2a2a;
        --mid-grey: #404040;
        --light-grey: #707070;
        --silver: #c0c0c0;
        --bright-silver: #e8e8e8;
        --platinum: #f5f5f5;
        --accent-glow: rgba(192, 192, 192, 0.3);
        --shadow-glow: rgba(192, 192, 192, 0.1);
    }

    /* Main App Background */
    .stApp {
        background: var(--pitch-black);
        color: var(--silver);
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
        font-weight: 400;
    }
    
    /* Main Content Container */
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        background: linear-gradient(135deg, var(--pitch-black) 0%, var(--deep-black) 50%, var(--charcoal) 100%);
        border-radius: 1rem;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.8);
    }

    /* Sidebar Styling */
    .css-1d391kg {
        background: linear-gradient(180deg, var(--deep-black) 0%, var(--charcoal) 100%);
        border-right: 1px solid var(--dark-grey);
    }

    /* Tab Styling - Ultra Slick */
    button[data-baseweb="tab"] {
        background: transparent;
        color: var(--light-grey);
        border: none;
        border-bottom: 2px solid transparent;
        font-weight: 500;
        font-size: 1rem;
        padding: 1rem 1.5rem;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        overflow: hidden;
    }
    
    button[data-baseweb="tab"]::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, var(--accent-glow), transparent);
        transition: left 0.6s ease;
    }
    
    button[data-baseweb="tab"]:hover::before {
        left: 100%;
    }
    
    button[data-baseweb="tab"]:hover {
        color: var(--bright-silver);
        transform: translateY(-2px);
        box-shadow: 0 4px 20px var(--shadow-glow);
    }
    
    button[data-baseweb="tab"][aria-selected="true"] {
        border-bottom: 2px solid var(--silver) !important;
        color: var(--platinum);
        background: linear-gradient(135deg, var(--charcoal), var(--dark-grey));
        font-weight: 600;
        box-shadow: 0 4px 20px var(--shadow-glow);
    }

    /* File Uploader - Sleek Design */
    .stFileUploader {
        background: linear-gradient(135deg, var(--deep-black), var(--charcoal));
        border: 2px dashed var(--mid-grey);
        border-radius: 1rem;
        padding: 2rem;
        transition: all 0.3s ease;
    }
    
    .stFileUploader:hover {
        border-color: var(--silver);
        background: linear-gradient(135deg, var(--charcoal), var(--dark-grey));
        box-shadow: 0 8px 32px var(--shadow-glow);
    }
    
    .stFileUploader > div > div > button {
        background: linear-gradient(135deg, var(--dark-grey), var(--mid-grey));
        border: 1px solid var(--silver);
        color: var(--bright-silver);
        font-weight: 600;
        border-radius: 0.75rem;
        padding: 0.75rem 2rem;
        transition: all 0.3s ease;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        font-size: 0.9rem;
    }
    
    .stFileUploader > div > div > button:hover {
        background: linear-gradient(135deg, var(--mid-grey), var(--light-grey));
        transform: translateY(-2px);
        box-shadow: 0 6px 25px var(--accent-glow);
    }
    
    .stFileUploader > div > div > div {
        color: var(--silver);
        font-weight: 500;
    }

    /* Button Styling - Premium Look */
    div[data-testid="stButton"] > button, 
    div[data-testid="stDownloadButton"] > button {
        background: linear-gradient(135deg, var(--charcoal) 0%, var(--dark-grey) 25%, var(--mid-grey) 75%, var(--silver) 100%);
        color: var(--pitch-black);
        font-weight: 700;
        font-size: 1rem;
        border: none;
        border-radius: 1rem;
        padding: 1rem 2rem;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        text-transform: uppercase;
        letter-spacing: 1px;
        position: relative;
        overflow: hidden;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.5);
    }
    
    div[data-testid="stButton"] > button::before,
    div[data-testid="stDownloadButton"] > button::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
        transition: left 0.6s ease;
    }
    
    div[data-testid="stButton"] > button:hover::before,
    div[data-testid="stDownloadButton"] > button:hover::before {
        left: 100%;
    }
    
    div[data-testid="stButton"] > button:hover,
    div[data-testid="stDownloadButton"] > button:hover {
        transform: translateY(-3px) scale(1.02);
        box-shadow: 0 8px 40px var(--accent-glow);
        background: linear-gradient(135deg, var(--dark-grey) 0%, var(--mid-grey) 25%, var(--light-grey) 75%, var(--bright-silver) 100%);
    }
    
    div[data-testid="stButton"] > button:active,
    div[data-testid="stDownloadButton"] > button:active {
        transform: translateY(-1px) scale(0.98);
        transition: all 0.1s ease;
    }
    
    div[data-testid="stButton"] > button:disabled,
    div[data-testid="stDownloadButton"] > button:disabled {
        background: linear-gradient(135deg, var(--deep-black), var(--charcoal));
        color: var(--dark-grey);
        cursor: not-allowed;
        transform: none;
        box-shadow: none;
    }

    /* Header Styling - Stunning Gradient Text */
    h1, h2, h3 {
        background: linear-gradient(135deg, var(--platinum) 0%, var(--bright-silver) 25%, var(--silver) 50%, var(--bright-silver) 75%, var(--platinum) 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-weight: 800;
        font-family: 'Inter', sans-serif;
        letter-spacing: -0.025em;
        line-height: 1.2;
        margin-bottom: 1.5rem;
        text-shadow: 0 0 30px var(--shadow-glow);
    }
    
    h1 {
        font-size: 3rem;
        background: linear-gradient(135deg, var(--platinum) 0%, var(--silver) 50%, var(--platinum) 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        filter: drop-shadow(0 0 20px var(--accent-glow));
    }

    /* Input Fields */
    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea,
    .stNumberInput > div > div > input {
        background: linear-gradient(135deg, var(--deep-black), var(--charcoal));
        border: 1px solid var(--dark-grey);
        color: var(--silver);
        border-radius: 0.75rem;
        padding: 0.75rem 1rem;
        font-weight: 500;
        transition: all 0.3s ease;
    }
    
   
    .stTextInput > div > div > input:focus,
    .stTextArea > div > div > textarea:focus,
    .stNumberInput > div > div > input:focus {
        border-color: var(--silver);
        box-shadow: 0 0 20px var(--shadow-glow);
        background: linear-gradient(135deg, var(--charcoal), var(--dark-grey));
    }

    /* Select Boxes */
    .stSelectbox > div > div > select {
        background: linear-gradient(135deg, var(--deep-black), var(--charcoal));
        border: 1px solid var(--dark-grey);
        color: var(--silver);
        border-radius: 0.75rem;
    }

    /* Progress Bars */
    .stProgress .st-bo {
        background: var(--dark-grey);
    }
    
    .stProgress .st-bp {
        background: linear-gradient(90deg, var(--silver), var(--bright-silver));
        box-shadow: 0 0 10px var(--accent-glow);
    }

    /* Metrics */
    div[data-testid="metric-container"] {
        background: linear-gradient(135deg, var(--deep-black), var(--charcoal));
        border: 1px solid var(--dark-grey);
        border-radius: 1rem;
        padding: 1.5rem;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.5);
        transition: all 0.3s ease;
    }
    
    div[data-testid="metric-container"]:hover {
        border-color: var(--mid-grey);
        box-shadow: 0 8px 32px var(--shadow-glow);
        transform: translateY(-2px);
    }

    /* Data Frame Styling */
    .dataframe {
        background: var(--deep-black);
        border: 1px solid var(--dark-grey);
        color: var(--silver);
    }
    
    .dataframe th {
        background: linear-gradient(135deg, var(--charcoal), var(--dark-grey));
        color: var(--bright-silver);
        font-weight: 600;
    }
    
    .dataframe td {
        border-color: var(--dark-grey);
    }

    /* Chart Background Fix */
    .js-plotly-plot .plotly .modebar {
        background: var(--charcoal);
    }

    /* Scrollbars */
    ::-webkit-scrollbar {
        width: 8px;
        height: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: var(--deep-black);
    }
    
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(135deg, var(--dark-grey), var(--mid-grey));
        border-radius: 4px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(135deg, var(--mid-grey), var(--light-grey));
    }

    /* Success/Error Messages */
    .stSuccess {
        background: linear-gradient(135deg, var(--deep-black), var(--charcoal));
        border-left: 4px solid #10b981;
        color: var(--silver);
    }
    
    .stError {
        background: linear-gradient(135deg, var(--deep-black), var(--charcoal));
        border-left: 4px solid #ef4444;
        color: var(--silver);
    }
    
    .stWarning {
        background: linear-gradient(135deg, var(--deep-black), var(--charcoal));
        border-left: 4px solid #f59e0b;
        color: var(--silver);
    }
    
    .stInfo {
        background: linear-gradient(135deg, var(--deep-black), var(--charcoal));
        border-left: 4px solid #3b82f6;
        color: var(--silver);
    }

    /* Animation for loading states */
    @keyframes shimmer {
        0% { transform: translateX(-100%); }
        100% { transform: translateX(100%); }
    }
    
    .loading-shimmer {
        position: relative;
        overflow: hidden;
    }
    
    .loading-shimmer::after {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, var(--accent-glow), transparent);
        animation: shimmer 2s infinite;
    }

</style>
""", unsafe_allow_html=True)


# --- Ollama API Call Function ---
def call_ollama(prompt: str):
    """Sends a prompt to the local Ollama server and returns the response."""
    ollama_api_url = "http://localhost:11434/api/generate"
    payload = {
        "model": "llama3",
        "prompt": prompt,
        "stream": False,
    }
    try:
        response = requests.post(ollama_api_url, json=payload)
        response.raise_for_status()
        last_line = response.text.strip().split('\n')[-1]
        return json.loads(last_line).get("response", "")
    except requests.exceptions.RequestException as e:
        st.error(f"Error connecting to Ollama: {e}. Is the Ollama server running?")
        return None
    except json.JSONDecodeError:
        st.error("Failed to decode JSON from Ollama response.")
        return None


# --- Main Application UI ---
st.title("AI TypeScript Converter")
st.markdown("Powered by a local **Llama 3** model via Ollama.")

with st.expander("How to Use This Tool"):
    st.markdown("""
        **Prerequisite:** Make sure your local Ollama server is running with the Llama 3 model. You can start it by running `ollama run llama3` in your terminal.

        ---

        ### Convert Folder
        1.  Click the **"Browse files"** button.
        2.  Navigate to your project folder.
        3.  Select all the `.ts` and `.tsx` files you want to convert. You can select multiple files by holding `Cmd` (Mac) or `Ctrl` (Windows), or by pressing `Cmd+A` / `Ctrl+A` to select all files in the folder.
        4.  Click the **"Convert Files to JavaScript"** button.
        5.  Once the progress bar is complete, a **"Download JavaScript Files (.zip)"** button will appear. Click it to download your converted files.

        ---

        ### Convert Single Snippet
        1.  Paste your TypeScript code into the left-hand text area.
        2.  Click the **"Convert Snippet"** button.
        3.  The converted, pure JavaScript code will appear in the right-hand text area.
    """)

# Initialize session state for both features
if 'zip_buffer' not in st.session_state:
    st.session_state.zip_buffer = None
if 'js_code_snippet' not in st.session_state:
    st.session_state.js_code_snippet = ""

# --- Create Tabs for different features ---
tab1, tab2 = st.tabs([" Convert Folder", " Convert Single Snippet"])

# --- Tab 1: Folder Conversion ---
with tab1:
    st.header("Convert Entire Folder")
    uploaded_files = st.file_uploader(
        "Upload your TypeScript files (.ts, .tsx)",
        accept_multiple_files=True,
        type=['ts', 'tsx'],
        key="folder_uploader"
    )

    if st.button("Convert Files to JavaScript", use_container_width=True, disabled=not uploaded_files, key="folder_convert_button"):
        if uploaded_files:
            progress_bar = st.progress(0, text="Starting conversion...")
            st.session_state.zip_buffer = None
            
            zip_buffer = io.BytesIO()
            with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zipf:
                total_files = len(uploaded_files)
                for i, uploaded_file in enumerate(uploaded_files):
                    file_name = uploaded_file.name
                    progress_text = f"Converting {file_name} ({i+1}/{total_files})..."
                    progress_bar.progress((i + 1) / total_files, text=progress_text)

                    ts_code = uploaded_file.getvalue().decode("utf-8")
                    
                    conversion_prompt = f"""You are an expert code transpiler. Your sole task is to convert the following TypeScript code into clean, modern JavaScript. RULES: 1. Remove all TypeScript type annotations. 2. Remove all interfaces and type declarations. 3. Keep the code logic and structure identical. 4. Do NOT add any explanations, comments, or markdown formatting. 5. Your output must be ONLY the raw JavaScript code. TypeScript Code to Convert: ```typescript\n{ts_code}\n```"""
                    
                    converted_code = call_ollama(conversion_prompt)
                    
                    if converted_code:
                        cleaned_code = converted_code.replace("```javascript\n", "").replace("```", "").strip()
                        base_name, _ = os.path.splitext(file_name)
                        js_file_name = f"{base_name}.js"
                        zipf.writestr(js_file_name, cleaned_code)

            st.session_state.zip_buffer = zip_buffer
            progress_bar.progress(1.0, text="Conversion complete! Ready for download.")

    if st.session_state.zip_buffer:
        st.download_button(
            label=" Download JavaScript Files (.zip)",
            data=st.session_state.zip_buffer.getvalue(),
            file_name="converted_js_files.zip",
            mime="application/zip",
            use_container_width=True,
            key="folder_download_button"
        )

# --- Tab 2: Single Snippet Conversion ---
with tab2:
    st.header("Convert Single Code Snippet")
    
    default_ts_code = (
        'function greet(name: string): string {\n'
        '  return `Hello, ${name}!`;\n'
        '}\n\n'
        'const user: { name: string; age: number } = {\n'
        '  name: "Alice",\n'
        '  age: 30,\n'
        '};'
    )
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("TypeScript Code")
        ts_code_snippet = st.text_area("TS Snippet", value=default_ts_code, height=300, label_visibility="collapsed")

    with col2:
        st.subheader("JavaScript Output")
        js_code_snippet_output = st.text_area("JS Snippet", value=st.session_state.js_code_snippet, height=300, placeholder="Converted JavaScript will appear here...", label_visibility="collapsed")

    if st.button("Convert Snippet", use_container_width=True, key="snippet_convert_button"):
        if not ts_code_snippet.strip():
            st.warning("Please enter some TypeScript code to convert.")
        else:
            with st.spinner("Converting..."):
                conversion_prompt = f"""You are an expert code transpiler. Your sole task is to convert the following TypeScript code into clean, modern JavaScript. RULES: 1. Remove all TypeScript type annotations. 2. Remove all interfaces and type declarations. 3. Keep the code logic and structure identical. 4. Do NOT add any explanations, comments, or markdown formatting. 5. Your output must be ONLY the raw JavaScript code. TypeScript Code to Convert: ```typescript\n{ts_code_snippet}\n```"""
                
                converted_code = call_ollama(conversion_prompt)
                
                if converted_code:
                    cleaned_code = converted_code.replace("```javascript\n", "").replace("```", "").strip()
                    st.session_state.js_code_snippet = cleaned_code
                    st.rerun()
