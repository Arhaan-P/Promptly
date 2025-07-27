# app.py

import streamlit as st
from dotenv import load_dotenv

# Import modules
from config.settings import AppConfig
from ui.styles import apply_custom_styles
from core.ai_service import AIServiceError
from core.prompt_analyzer import AdvancedPromptAnalyzer
from utils.validators import PromptValidator
from utils.cache_manager import CacheManager
from utils.logger import setup_logger, PerformanceLogger
from ui.components import UIComponents

# Load environment variables
load_dotenv()

# Initialize objects
logger = setup_logger(__name__)
config = AppConfig()
ui = UIComponents()
validator = PromptValidator()
cache = CacheManager(ttl_hours=24)
perf_logger = PerformanceLogger()


def main():
    """Main application function."""
    # Page setup
    st.set_page_config(
        page_title="Promptly",
        page_icon="🚀",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    apply_custom_styles()

    # Initialize session state
    if 'evaluation_history' not in st.session_state:
        st.session_state.evaluation_history = []
    if 'current_prompt' not in st.session_state:
        st.session_state.current_prompt = ""

    # Header
    ui.render_header()

    # Main content tabs
    tab1, tab2 = st.tabs(["📝 Analysis Studio", "📈 Analytics Dashboard"])

    with tab1:
        # Prompt input
        prompt_text = ui.render_prompt_input()

        # Analysis section
        col1, col2 = st.columns([3, 1])
        
        with col1:
            analyze_button = st.button(
                "🔍 Analyze Prompt", 
                type="primary", 
                disabled=len(prompt_text.strip()) < 10,
                help="Minimum 10 characters required"
            )
        
        with col2:
            if prompt_text:
                char_count = len(prompt_text)
                word_count = len(prompt_text.split())
                st.caption(f"{word_count} words • {char_count} chars")

        # Analysis execution
        if analyze_button and prompt_text:
            perf_logger.start_timer("analysis")

            if validator.validate_prompt(prompt_text):
                cache_key = cache.generate_key(prompt_text)
                cached_result = cache.get(cache_key)

                if cached_result:
                    logger.info("Using cached result")
                    st.success("⚡ Loaded from cache")
                    analysis_result = cached_result
                else:
                    with st.spinner("🤖 Analyzing prompt..."):
                        try:
                            analyzer = AdvancedPromptAnalyzer()
                            analysis_result = analyzer.comprehensive_analysis(prompt_text)
                            cache.set(cache_key, analysis_result)
                            logger.info("Analysis completed")

                        except AIServiceError as e:
                            logger.error(f"AI Service error: {e}")
                            st.error(f"🚨 AI Service Error: {e}")
                            analysis_result = None
                        except Exception as e:
                            logger.error(f"Unexpected error: {e}")
                            st.error("🚨 An unexpected error occurred")
                            analysis_result = None

                # Display results
                if analysis_result:
                    ui.render_evaluation_results(analysis_result)
                    
                    # Add to history
                    st.session_state.evaluation_history.append({
                        "prompt": prompt_text,
                        "result": analysis_result,
                        "timestamp": cache.get_timestamp()
                    })
                    
                    st.session_state.current_prompt = prompt_text

            perf_logger.end_timer("analysis")

        # Show example prompts if no input
        elif not prompt_text:
            st.markdown("""
            ### 💡 Example Prompts
            
            **Marketing Strategy:**
            ```
            Create a comprehensive social media marketing strategy for a sustainable fashion startup 
            targeting millennials aged 25-35. Include platform-specific content ideas, engagement 
            tactics, and success metrics for Instagram, TikTok, and Pinterest.
            ```
            
            **Technical Documentation:**
            ```
            Write detailed API documentation for a user authentication endpoint. Include request/response 
            examples, error codes, rate limiting information, and security considerations. Format as 
            clear markdown with code blocks.
            ```
            
            **Creative Writing:**
            ```
            Write a compelling 800-word short story about a time traveler who accidentally changes 
            a minor historical event. Use third-person narrative, include dialogue, and create a 
            twist ending. The tone should be mysterious but optimistic.
            ```
            """)

    with tab2:
        ui.render_analytics_dashboard(st.session_state.evaluation_history)

    # Sidebar
    with st.sidebar:
        ui.render_sidebar_content()

    # Footer
    ui.render_footer()


def check_configuration():
    """Check application configuration."""
    if not config.is_configured:
        st.error("🚨 Configuration Error: GOOGLE_API_KEY not found")
        st.markdown("""
        ### Setup Instructions:
        1. Create a `.env` file in your project root
        2. Add: `GOOGLE_API_KEY=your_api_key_here`
        3. Restart the application
        
        Get your API key at [Google AI Studio](https://makersuite.google.com/app/apikey)
        """)
        return False
    return True


if __name__ == "__main__":
    if check_configuration():
        logger.info("Starting application...")
        main()
    else:
        logger.critical("Configuration incomplete")
        st.stop()