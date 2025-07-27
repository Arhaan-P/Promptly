# 🚀 Promptly - AI-Powered Prompt Analysis Platform

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://promptly-analyzer.streamlit.app)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> **Transform your prompts into powerful, professional instructions with AI-driven analysis and optimization.**

Promptly is a comprehensive web application that analyzes prompt quality using advanced AI models and provides actionable insights to improve your AI interactions. Built with modern Python architecture and deployed on Streamlit Cloud.

## ✨ Features

### 🎯 **Core Analysis Engine**
- **Multi-Dimensional Scoring**: Clarity, Specificity, Context, Constraints, and Goal Orientation
- **AI-Powered Insights**: Google Gemini integration with intelligent fallback systems
- **Real-Time Feedback**: Instant analysis with detailed recommendations
- **Smart Caching**: Optimized performance with built-in response caching

### 📊 **Advanced Analytics**
- **Interactive Radar Charts**: Visual representation of prompt quality metrics
- **Progress Tracking**: Monitor improvement over time with trend analysis
- **Performance Metrics**: Detailed statistics on prompt effectiveness
- **Export Capabilities**: Download analysis results and reports

### 🎨 **Professional UI/UX**
- **Modern Design**: Clean, minimalist interface with gradient aesthetics
- **Responsive Layout**: Optimized for desktop and mobile devices
- **Interactive Components**: Hover effects, smooth animations, and transitions
- **Dark Mode Support**: Professional styling with custom themes

### 🔧 **Technical Excellence**
- **Robust Architecture**: Modular design with clear separation of concerns
- **Error Handling**: Comprehensive validation and graceful degradation
- **Rate Limiting**: Smart API usage management for free tier optimization
- **Logging System**: Advanced monitoring and debugging capabilities

## 📋 Quick Start

### Prerequisites
- Python 3.8 or higher
- Google Gemini API key (free tier available)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/promptly.git
   cd promptly
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   ```bash
   # Create .env file
   echo "GOOGLE_API_KEY=your_gemini_api_key_here" > .env
   ```

4. **Run the application**
   ```bash
   streamlit run app.py
   ```

5. **Open your browser**
   ```
   http://localhost:8501
   ```

## 🔑 Getting Your Free API Key

1. Visit [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Sign in with your Google account
3. Click "Create API Key" → "Create API key in new project"
4. Copy the generated key and add it to your `.env` file

**Free Tier Limits:**
- 1,500 requests per day
- 15 requests per minute
- 32,000 tokens per minute

## 🏗️ Architecture

```
promptly/
├── 📁 config/
│   └── settings.py          # Configuration management
├── 📁 core/
│   ├── ai_service.py        # AI service integration
│   └── prompt_analyzer.py   # Analysis engine
├── 📁 ui/
│   ├── components.py        # UI components
│   └── styles.py           # Custom styling
├── 📁 utils/
│   ├── cache_manager.py    # Caching system
│   ├── logger.py           # Logging utilities
│   └── validators.py       # Input validation
├── app.py                  # Main application
├── requirements.txt        # Dependencies
└── README.md              # Documentation
```

### 🔧 Core Components

- **AI Service Layer**: Modular AI provider integration with fallback support
- **Analysis Engine**: Multi-dimensional prompt evaluation with rule-based backup
- **Caching System**: Smart response caching for performance optimization
- **UI Framework**: Professional Streamlit components with custom styling
- **Validation Layer**: Comprehensive input sanitization and error handling

## 📊 Analysis Metrics

Promptly evaluates prompts across five key dimensions:

| Metric | Description | Weight |
|--------|-------------|---------|
| **Clarity** | Language clarity and ambiguity reduction | 20% |
| **Specificity** | Detailed requirements and constraints | 20% |
| **Context** | Background information and situational awareness | 20% |
| **Constraints** | Format, style, and structural guidelines | 20% |
| **Goal Orientation** | Clear outcome definition and actionability | 20% |

### Scoring System
- **8-10**: Excellent quality, ready for production use
- **6-7**: Good quality with minor improvements needed
- **4-5**: Moderate quality requiring significant enhancement
- **1-3**: Poor quality needing complete restructuring

## 🛠️ Configuration

### Environment Variables
```bash
# Required
GOOGLE_API_KEY=your_gemini_api_key

# Optional
LOG_LEVEL=INFO
CACHE_TTL_HOURS=24
MAX_PROMPT_LENGTH=5000
```

### Model Configuration
```python
# settings.py
@dataclass
class AIModels:
    GEMINI_PRO = "gemini-1.5-flash"  # Fast, cost-effective
    # GEMINI_PRO = "gemini-1.5-pro"  # More accurate, slower
```

## 📈 Performance Optimization

### Built-in Optimizations
- **Smart Caching**: Avoids redundant API calls for identical prompts
- **Rate Limiting**: Prevents quota exhaustion with intelligent delays
- **Fallback System**: Rule-based analysis when AI service is unavailable
- **Token Management**: Optimized prompt engineering for cost efficiency

### Monitoring
```python
# Performance tracking
from utils.logger import PerformanceLogger

perf_logger = PerformanceLogger()
perf_logger.start_timer("analysis")
# ... analysis code ...
duration = perf_logger.end_timer("analysis")
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

[⭐ Star this repo](https://github.com/Arhaan-P/Promptly) • [🐛 Report Bug](https://github.com/Arhaan-P/Promptly/issues) • [💡 Request Feature](https://github.com/Arhaan-P/Promptly/issues)

</div>
