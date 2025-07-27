import hashlib
import time
import json
from typing import Any, Optional, Dict
from datetime import datetime, timedelta
import streamlit as st

class CacheManager:
    """Advanced caching system for API responses."""
    
    def __init__(self, ttl_hours: int = 24):
        if 'cache_store' not in st.session_state:
            st.session_state.cache_store = {}
        self.ttl_hours = ttl_hours
        
    def generate_key(self, prompt: str) -> str:
        """Generate cache key from prompt."""
        return hashlib.md5(prompt.encode()).hexdigest()
    
    def get(self, key: str) -> Optional[Any]:
        """Retrieve from cache if not expired."""
        if key not in st.session_state.cache_store:
            return None
            
        cache_entry = st.session_state.cache_store[key]
        
        # Check expiration
        if self._is_expired(cache_entry['timestamp']):
            del st.session_state.cache_store[key]
            return None
            
        return cache_entry['data']
    
    def set(self, key: str, data: Any) -> None:
        """Store data in cache."""
        st.session_state.cache_store[key] = {
            'data': data,
            'timestamp': time.time()
        }
        
        # Cleanup old entries
        self._cleanup_expired()
    
    def _is_expired(self, timestamp: float) -> bool:
        """Check if cache entry is expired."""
        return time.time() - timestamp > (self.ttl_hours * 3600)
    
    def _cleanup_expired(self) -> None:
        """Remove expired cache entries."""
        expired_keys = [
            key for key, entry in st.session_state.cache_store.items()
            if self._is_expired(entry['timestamp'])
        ]
        
        for key in expired_keys:
            del st.session_state.cache_store[key]
    
    def get_timestamp(self) -> str:
        """Get current timestamp."""
        return datetime.now().isoformat()
    
    def get_cache_stats(self) -> Dict[str, Any]:
        """Get cache statistics."""
        return {
            'entries': len(st.session_state.cache_store),
            'size_kb': len(json.dumps(st.session_state.cache_store)) / 1024
        }
