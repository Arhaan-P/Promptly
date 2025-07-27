import streamlit as st

def apply_custom_styles():
    """Apply enhanced custom CSS styling."""
    st.markdown("""
    <style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    /* Global Styles */
    .main {
        font-family: 'Inter', sans-serif;
    }
    
    /* Header Styling */
    .main-header {
        text-align: center;
        padding: 3rem 0 2rem 0;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 20px;
        margin-bottom: 2rem;
        box-shadow: 0 10px 30px rgba(102, 126, 234, 0.3);
        position: relative;
        overflow: hidden;
    }
    
    .main-header::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><circle cx="20" cy="20" r="2" fill="white" opacity="0.1"/><circle cx="80" cy="40" r="1.5" fill="white" opacity="0.1"/><circle cx="40" cy="80" r="1" fill="white" opacity="0.1"/><circle cx="90" cy="10" r="1" fill="white" opacity="0.1"/><circle cx="10" cy="90" r="2" fill="white" opacity="0.1"/></svg>');
        pointer-events: none;
    }
    
    .main-header h1 {
        font-size: 3.5rem;
        margin-bottom: 0.5rem;
        font-weight: 700;
        position: relative;
        z-index: 1;
        text-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    .subtitle {
        font-size: 1.3rem;
        opacity: 0.95;
        font-weight: 400;
        position: relative;
        z-index: 1;
    }
    
    /* Button Styling */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 12px;
        padding: 0.75rem 2rem;
        font-weight: 600;
        font-size: 1rem;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
        font-family: 'Inter', sans-serif;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.4);
        background: linear-gradient(135deg, #5a6fd8 0%, #6a4190 100%);
    }
    
    .stButton > button:active {
        transform: translateY(0);
    }
    
    .stButton > button:disabled {
        background: #cccccc;
        color: #666666;
        cursor: not-allowed;
        transform: none;
        box-shadow: none;
    }
    
    /* Text Area Styling */
    .stTextArea > div > div > textarea {
        border-radius: 12px;
        border: 2px solid #e1e5e9;
        padding: 1rem;
        font-size: 1rem;
        line-height: 1.6;
        transition: border-color 0.3s ease;
        font-family: 'Inter', sans-serif;
    }
    
    .stTextArea > div > div > textarea:focus {
        border-color: #667eea;
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
        outline: none;
    }
    
    /* Tabs Styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 12px;
        background: transparent;
        padding: 0.5rem 0;
    }
    
    .stTabs [data-baseweb="tab"] {
        background: linear-gradient(135deg, #f8f9ff 0%, #e8ecff 100%);
        color: #667eea;
        border-radius: 12px;
        border: 2px solid #e1e5e9;
        font-weight: 600;
        padding: 0.75rem 1.5rem;
        transition: all 0.3s ease;
        font-family: 'Inter', sans-serif;
    }
    
    .stTabs [data-baseweb="tab"]:hover {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        transform: translateY(-1px);
    }
    
    .stTabs [data-baseweb="tab"][aria-selected="true"] {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-color: #667eea;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
    }
    
    /* Metric Cards */
    .metric-card {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        padding: 1.5rem;
        border-radius: 15px;
        color: white;
        text-align: center;
        margin: 0.5rem 0;
        box-shadow: 0 6px 20px rgba(240, 147, 251, 0.3);
        transition: transform 0.3s ease;
    }
    
    .metric-card:hover {
        transform: translateY(-2px);
    }
    
    /* Progress Bar Styling */
    .stProgress > div > div > div {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 10px;
    }
    
    .stProgress > div > div {
        background-color: #f0f2f6;
        border-radius: 10px;
    }
    
    /* Sidebar Styling */
    .css-1d391kg {
        background: linear-gradient(180deg, #f8f9ff 0%, #e8ecff 100%);
        border-right: 1px solid #e1e5e9;
    }
    
    /* Success/Error Messages */
    .stSuccess {
        background: linear-gradient(135deg, #56ab2f 0%, #a8e6cf 100%);
        border-radius: 12px;
        border: none;
        color: white;
        font-weight: 500;
    }
    
    .stError {
        background: linear-gradient(135deg, #ff416c 0%, #ff4b2b 100%);
        border-radius: 12px;
        border: none;
        color: white;
        font-weight: 500;
    }
    
    .stWarning {
        background: linear-gradient(135deg, #ffa726 0%, #ff9800 100%);
        border-radius: 12px;
        border: none;
        color: white;
        font-weight: 500;
    }
    
    .stInfo {
        background: linear-gradient(135deg, #29b6f6 0%, #0288d1 100%);
        border-radius: 12px;
        border: none;
        color: white;
        font-weight: 500;
    }
    
    /* Expander Styling */
    .streamlit-expanderHeader {
        background: linear-gradient(135deg, #f8f9ff 0%, #e8ecff 100%);
        color: #667eea;
        border-radius: 12px;
        font-weight: 600;
        border: 2px solid #e1e5e9;
        transition: all 0.3s ease;
    }
    
    .streamlit-expanderHeader:hover {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
    }
    
    /* Code Block Styling */
    .stCodeBlock {
        background: #f8f9fa;
        border: 1px solid #e9ecef;
        border-radius: 12px;
        font-family: 'Fira Code', monospace;
    }
    
    /* Selectbox Styling */
    .stSelectbox > div > div {
        border-radius: 12px;
        border: 2px solid #e1e5e9;
        transition: border-color 0.3s ease;
    }
    
    .stSelectbox > div > div:focus-within {
        border-color: #667eea;
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
    }
    
    /* Footer Styling */
    .footer {
        text-align: center;
        padding: 3rem 0;
        color: #6c757d;
        font-size: 0.95rem;
        background: linear-gradient(135deg, #f8f9ff 0%, #e8ecff 100%);
        border-radius: 20px;
        margin-top: 2rem;
        border: 1px solid #e1e5e9;
    }
    
    .footer a {
        color: #667eea;
        text-decoration: none;
        font-weight: 500;
        transition: color 0.3s ease;
    }
    
    .footer a:hover {
        color: #764ba2;
    }
    
    /* Spinner Styling */
    .stSpinner > div {
        border-color: #667eea transparent #667eea transparent;
    }
    
    /* Card-like containers */
    .analysis-card {
        background: white;
        border-radius: 20px;
        padding: 2rem;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
        border: 1px solid #e1e5e9;
        margin: 1rem 0;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    
    .analysis-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 30px rgba(0, 0, 0, 0.12);
    }
    
    /* Plotly chart container */
    .js-plotly-plot {
        border-radius: 12px;
        overflow: hidden;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
    }
    
    /* Custom scrollbar */
    ::-webkit-scrollbar {
        width: 8px;
        height: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: #f1f1f1;
        border-radius: 4px;
    }
    
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 4px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(135deg, #5a6fd8 0%, #6a4190 100%);
    }
    
    /* Loading animation */
    @keyframes pulse {
        0% { opacity: 1; }
        50% { opacity: 0.5; }
        100% { opacity: 1; }
    }
    
    .loading-text {
        animation: pulse 2s infinite;
    }
    
    /* Responsive design */
    @media (max-width: 768px) {
        .main-header h1 {
            font-size: 2.5rem;
        }
        
        .subtitle {
            font-size: 1.1rem;
        }
        
        .stButton > button {
            padding: 0.6rem 1.5rem;
            font-size: 0.9rem;
        }
    }
    
    /* Hide Streamlit menu and footer */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Custom metric styling */
    [data-testid="metric-container"] {
        background: linear-gradient(135deg, #f8f9ff 0%, #e8ecff 100%);
        border: 1px solid #e1e5e9;
        border-radius: 12px;
        padding: 1rem;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
        transition: transform 0.3s ease;
    }
    
    [data-testid="metric-container"]:hover {
        transform: translateY(-1px);
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
    }
    
    [data-testid="metric-container"] > div {
        color: #333;
    }
    
    [data-testid="metric-container"] [data-testid="metric-value"] {
        color: #667eea;
        font-weight: 700;
    }
    </style>
    """, unsafe_allow_html=True)