import logging
import sys
from datetime import datetime
from typing import Any, Dict
import streamlit as st

class StreamlitLogHandler(logging.Handler):
    """Custom log handler for Streamlit."""
    
    def emit(self, record):
        """Emit log record to Streamlit."""
        log_entry = self.format(record)
        
        if record.levelno >= logging.ERROR:
            st.error(f"🚨 {log_entry}")
        elif record.levelno >= logging.WARNING:
            st.warning(f"⚠️ {log_entry}")
        elif record.levelno >= logging.INFO:
            st.info(f"ℹ️ {log_entry}")

def setup_logger(name: str) -> logging.Logger:
    """Setup advanced logger with multiple handlers."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    
    # Clear existing handlers
    logger.handlers.clear()
    
    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)
    
    # Streamlit handler
    streamlit_handler = StreamlitLogHandler()
    streamlit_handler.setLevel(logging.WARNING)
    
    # Formatter
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    console_handler.setFormatter(formatter)
    streamlit_handler.setFormatter(formatter)
    
    logger.addHandler(console_handler)
    logger.addHandler(streamlit_handler)
    
    return logger

class PerformanceLogger:
    """Performance monitoring and logging."""
    
    def __init__(self):
        self.start_times = {}
        self.metrics = []
    
    def start_timer(self, operation: str):
        """Start timing an operation."""
        self.start_times[operation] = datetime.now()
    
    def end_timer(self, operation: str) -> float:
        """End timing and return duration."""
        if operation not in self.start_times:
            return 0.0
        
        duration = (datetime.now() - self.start_times[operation]).total_seconds()
        self.metrics.append({
            'operation': operation,
            'duration': duration,
            'timestamp': datetime.now().isoformat()
        })
        
        del self.start_times[operation]
        return duration
    
    def get_metrics(self) -> list:
        """Get performance metrics."""
        return self.metrics
