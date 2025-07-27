import re
from typing import List, Tuple, Optional
import streamlit as st

class ValidationError(Exception):
    """Custom validation error."""
    pass

class PromptValidator:
    """Advanced prompt validation with detailed feedback."""
    
    def __init__(self):
        self.min_length = 10
        self.max_length = 5000
        self.suspicious_patterns = [
            r'(?i)(hack|exploit|bypass|jailbreak)',
            r'(?i)(illegal|harmful|dangerous)',
        ]
        
    def validate_prompt(self, prompt: str) -> bool:
        """Comprehensive prompt validation."""
        try:
            self._validate_length(prompt)
            self._validate_content(prompt)
            self._validate_encoding(prompt)
            self._check_suspicious_patterns(prompt)
            return True
        except ValidationError as e:
            st.error(f"❌ Validation Error: {e}")
            return False
    
    def _validate_length(self, prompt: str) -> None:
        """Validate prompt length."""
        if len(prompt.strip()) < self.min_length:
            raise ValidationError(f"Prompt too short. Minimum {self.min_length} characters required.")
        
        if len(prompt) > self.max_length:
            raise ValidationError(f"Prompt too long. Maximum {self.max_length} characters allowed.")
    
    def _validate_content(self, prompt: str) -> None:
        """Validate prompt content quality."""
        if not prompt.strip():
            raise ValidationError("Empty prompt not allowed.")
        
        # Check for meaningful content
        words = prompt.split()
        if len(words) < 3:
            raise ValidationError("Prompt should contain at least 3 words.")
        
        # Check for repeated characters (potential spam)
        if re.search(r'(.)\1{10,}', prompt):
            raise ValidationError("Excessive character repetition detected.")
    
    def _validate_encoding(self, prompt: str) -> None:
        """Validate text encoding."""
        try:
            prompt.encode('utf-8')
        except UnicodeEncodeError:
            raise ValidationError("Invalid character encoding detected.")
    
    def _check_suspicious_patterns(self, prompt: str) -> None:
        """Check for suspicious patterns."""
        for pattern in self.suspicious_patterns:
            if re.search(pattern, prompt):
                st.warning("⚠️ Prompt contains potentially sensitive content. Please review.")
                break
    
    def get_validation_score(self, prompt: str) -> float:
        """Get validation quality score (0-1)."""
        score = 1.0
        
        # Length penalty
        if len(prompt) < 50:
            score -= 0.2
        
        # Word diversity
        words = prompt.split()
        unique_words = set(words)
        diversity = len(unique_words) / len(words) if words else 0
        score -= (1 - diversity) * 0.3
        
        # Sentence structure
        sentences = re.split(r'[.!?]+', prompt)
        if len(sentences) < 2:
            score -= 0.2
        
        return max(0, score)
