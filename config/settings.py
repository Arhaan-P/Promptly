import os
from dataclasses import dataclass
from typing import Dict, Any
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

@dataclass
class AIModels:
    """AI model configurations."""
    GEMINI_PRO = "gemini-1.5-flash"

class AppConfig:
    """Centralized configuration management."""
    
    def __init__(self):
        self.google_api_key = os.getenv("GOOGLE_API_KEY") or st.secrets.get("GOOGLE_API_KEY")
        
    @property
    def is_configured(self) -> bool:
        """Check if minimum configuration is present."""
        return bool(self.google_api_key)
    
    def get_model_config(self) -> Dict[str, Any]:
        """Get AI model configuration for free tier."""
        return {
            "temperature": 0.1,  # Lower for more consistent results
            "max_tokens": 1000,  # Reduced for free tier
            "top_p": 0.8,
        }
    
    def default_preferences(self) -> Dict[str, Any]:
        """Default user preferences."""
        return {
            "theme": "dark",
            "analysis_depth": "comprehensive",
            "auto_save": True,
            "show_analytics": True
        }