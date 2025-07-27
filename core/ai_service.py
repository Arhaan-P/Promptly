import google.generativeai as genai
import time
from abc import ABC, abstractmethod
from typing import Dict, Any, Optional
from config.settings import AppConfig, AIModels

class AIServiceInterface(ABC):
    """Abstract interface for AI services."""
    
    @abstractmethod
    def generate_response(self, prompt: str, **kwargs) -> str:
        pass

class GeminiService(AIServiceInterface):
    """Google Gemini AI service with rate limiting for free tier."""
    
    def __init__(self, api_key: str):
        self.debug = True
        self.last_request_time = 0
        self.min_request_interval = 2  # Wait 2 seconds between requests
        
        if self.debug:
            print(f"🔑 Initializing Gemini with API key: {api_key[:10]}...{api_key[-5:] if len(api_key) > 15 else 'SHORT_KEY'}")
        
        try:
            genai.configure(api_key=api_key)
            self.model = genai.GenerativeModel(AIModels.GEMINI_PRO)
            
            if self.debug:
                print("✅ Gemini service initialized successfully")
                print(f"🚦 Rate limiting enabled: {self.min_request_interval}s between requests")
                
        except Exception as e:
            if self.debug:
                print(f"❌ Failed to initialize Gemini: {e}")
            raise AIServiceError(f"Failed to initialize Gemini: {e}")
    
    def _wait_for_rate_limit(self):
        """Ensure we don't exceed rate limits."""
        current_time = time.time()
        time_since_last = current_time - self.last_request_time
        
        if time_since_last < self.min_request_interval:
            wait_time = self.min_request_interval - time_since_last
            if self.debug:
                print(f"⏳ Rate limiting: waiting {wait_time:.1f}s...")
            time.sleep(wait_time)
        
        self.last_request_time = time.time()
        
    def generate_response(self, prompt: str, **kwargs) -> str:
        # Rate limiting
        self._wait_for_rate_limit()
        
        if self.debug:
            print(f"📤 Sending request to Gemini...")
            print(f"Prompt length: {len(prompt)} characters")
        
        try:
            # Optimized config for free tier
            generation_config = {
                'temperature': 0.1,  # Lower temperature for consistency
                'top_p': 0.8,
                'top_k': 40,
                'max_output_tokens': 1500,  # Reduced for free tier
            }
            
            response = self.model.generate_content(
                prompt,
                generation_config=generation_config
            )
            
            if self.debug:
                print(f"📥 Received response from Gemini")
                print(f"Response length: {len(response.text)} characters")
            
            return response.text
            
        except Exception as e:
            if self.debug:
                print(f"❌ Gemini API error: {type(e).__name__}: {e}")
            
            # Handle quota exceeded gracefully
            if "429" in str(e) or "quota" in str(e).lower():
                if self.debug:
                    print("💡 Quota exceeded - consider waiting or using rule-based analysis")
                
            raise AIServiceError(f"Gemini API error: {e}")

class AIServiceError(Exception):
    """Custom exception for AI service errors."""
    pass

class AIServiceManager:
    """Manages AI services with free tier optimizations."""
    
    def __init__(self):
        self.debug = True
        self.config = AppConfig()
        
        if self.debug:
            print("🚀 Initializing AI Service Manager (Free Tier Mode)...")
            print(f"Google API key available: {'Yes' if self.config.google_api_key else 'No'}")
        
        self.services = self._initialize_services()
        self.primary_service = "gemini"
        
    def _initialize_services(self) -> Dict[str, AIServiceInterface]:
        services = {}
        
        if self.config.google_api_key:
            try:
                services["gemini"] = GeminiService(self.config.google_api_key)
                if self.debug:
                    print("✅ Gemini service added successfully")
            except Exception as e:
                if self.debug:
                    print(f"❌ Failed to add Gemini service: {e}")
        else:
            if self.debug:
                print("❌ No Google API key found")
        
        return services
    
    def get_service(self, service_name: Optional[str] = None) -> AIServiceInterface:
        """Get AI service with fallback logic."""
        service_name = service_name or self.primary_service
        
        if self.debug:
            print(f"🎯 Requesting service: {service_name}")
        
        if service_name not in self.services:
            available_services = list(self.services.keys())
            if self.debug:
                print(f"❌ Service {service_name} not available")
                print(f"Available services: {available_services}")
            
            raise AIServiceError(f"Service {service_name} not available. Available: {available_services}")
            
        return self.services[service_name]