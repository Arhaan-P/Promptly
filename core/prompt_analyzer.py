import json
import re
from typing import Dict, List, Any
from dataclasses import dataclass, asdict

@dataclass
class AnalysisMetrics:
    """Structured analysis metrics."""
    clarity_score: float
    specificity_score: float
    context_score: float
    constraint_score: float
    goal_orientation_score: float
    overall_score: float
    word_count: int
    sentence_count: int
    complexity_level: str

@dataclass
class AnalysisResult:
    """Complete analysis result structure."""
    metrics: AnalysisMetrics
    strengths: List[str]
    weaknesses: List[str]
    suggestions: List[str]
    improved_prompt: str
    confidence_level: float

class AdvancedPromptAnalyzer:
    """Advanced prompt analysis with multiple evaluation criteria."""
    
    def __init__(self):
        self.meta_prompts = self._load_meta_prompts()
        self.debug = True  # Enable debug logging
        
    def _load_meta_prompts(self) -> Dict[str, str]:
        """Load different meta-prompts for various analysis types."""
        return {
            "comprehensive": """
You are an expert prompt engineering consultant. Analyze the following prompt and provide scores from 1-10 for each dimension.

IMPORTANT: Return scores as NUMBERS, not arrays. Example: "clarity": 7, NOT "clarity": [7]

Respond ONLY with valid JSON in this exact format:
{
    "scores": {
        "clarity": 7,
        "specificity": 5, 
        "context": 4,
        "constraints": 3,
        "goal_orientation": 8,
        "overall": 6
    },
    "analysis": {
        "strengths": ["strength1", "strength2", "strength3"],
        "weaknesses": ["weakness1", "weakness2", "weakness3"], 
        "suggestions": ["suggestion1", "suggestion2", "suggestion3"]
    },
    "improved_prompt": "Your improved version of the prompt here",
    "confidence": 0.8
}

PROMPT TO ANALYZE:
""",
            
            "creative": """
            Focus on creative and innovative aspects of the prompt...
            """,
            
            "technical": """
            Evaluate technical precision and implementation clarity...
            """
        }
    
    def comprehensive_analysis(self, prompt: str) -> AnalysisResult:
        """Perform comprehensive prompt analysis."""
        if self.debug:
            print(f"=== ANALYZING PROMPT ===")
            print(f"Prompt length: {len(prompt)} characters")
            print(f"Prompt: {prompt[:100]}{'...' if len(prompt) > 100 else ''}")
        
        # Basic metrics
        word_count = len(prompt.split())
        sentence_count = len(re.split(r'[.!?]+', prompt.strip()))
        complexity = self._assess_complexity(prompt)
        
        # Try AI-powered analysis first
        ai_analysis = self._get_ai_analysis(prompt, "comprehensive")
        
        # FIXED: Check if AI analysis actually worked
        if not ai_analysis or not self._is_valid_ai_analysis(ai_analysis):
            if self.debug:
                print("❌ AI analysis failed, using rule-based fallback")
            ai_analysis = self._rule_based_analysis(prompt)
        else:
            if self.debug:
                print("✅ AI analysis successful")
        
        # Combine results
        scores = ai_analysis.get("scores", {})
        metrics = AnalysisMetrics(
            clarity_score=scores.get("clarity", 5),
            specificity_score=scores.get("specificity", 5),
            context_score=scores.get("context", 5),
            constraint_score=scores.get("constraints", 5),
            goal_orientation_score=scores.get("goal_orientation", 5),
            overall_score=scores.get("overall", 5),
            word_count=word_count,
            sentence_count=sentence_count,
            complexity_level=complexity
        )
        
        if self.debug:
            print(f"Final scores: {scores}")
        
        return AnalysisResult(
            metrics=metrics,
            strengths=ai_analysis.get("analysis", {}).get("strengths", []),
            weaknesses=ai_analysis.get("analysis", {}).get("weaknesses", []),
            suggestions=ai_analysis.get("analysis", {}).get("suggestions", []),
            improved_prompt=ai_analysis.get("improved_prompt", prompt),
            confidence_level=ai_analysis.get("confidence", 0.5)
        )
    
    def _assess_complexity(self, prompt: str) -> str:
        """Assess prompt complexity level."""
        word_count = len(prompt.split())
        
        if word_count < 20:
            return "Simple"
        elif word_count < 50:
            return "Moderate"
        elif word_count < 100:
            return "Complex"
        else:
            return "Advanced"
    
    def _rule_based_analysis(self, prompt: str) -> Dict[str, Any]:
        """FIXED: More dynamic rule-based analysis as fallback."""
        if self.debug:
            print("🔄 Running rule-based analysis...")
        
        word_count = len(prompt.split())
        sentence_count = len(re.split(r'[.!?]+', prompt.strip()))
        
        # FIXED: More varied scoring that doesn't always return ~5.6
        clarity_score = self._calculate_clarity_score(prompt)
        specificity_score = self._calculate_specificity_score(prompt)
        context_score = self._calculate_context_score(prompt)
        constraint_score = self._calculate_constraint_score(prompt)
        goal_score = self._calculate_goal_score(prompt)
        
        overall_score = (clarity_score + specificity_score + context_score + constraint_score + goal_score) / 5
        
        if self.debug:
            print(f"Individual scores: clarity={clarity_score:.1f}, specificity={specificity_score:.1f}, context={context_score:.1f}, constraints={constraint_score:.1f}, goal={goal_score:.1f}")
            print(f"Overall score: {overall_score:.1f}")
        
        # Generate feedback based on analysis
        strengths = self._identify_strengths(prompt, clarity_score, specificity_score, context_score, constraint_score, goal_score)
        weaknesses = self._identify_weaknesses(prompt, clarity_score, specificity_score, context_score, constraint_score, goal_score)
        suggestions = self._generate_suggestions(prompt, weaknesses)
        improved_prompt = self._improve_prompt(prompt, weaknesses)
        
        return {
            "scores": {
                "clarity": round(clarity_score, 1),
                "specificity": round(specificity_score, 1),
                "context": round(context_score, 1),
                "constraints": round(constraint_score, 1),
                "goal_orientation": round(goal_score, 1),
                "overall": round(overall_score, 1)
            },
            "analysis": {
                "strengths": strengths,
                "weaknesses": weaknesses,
                "suggestions": suggestions
            },
            "improved_prompt": improved_prompt,
            "confidence": 0.7  # Rule-based analysis confidence
        }
    
    def _calculate_clarity_score(self, prompt: str) -> float:
        """FIXED: More dynamic clarity scoring."""
        # Start based on prompt length and structure
        word_count = len(prompt.split())
        if word_count < 5:
            score = 3.0  # Very short prompts are unclear
        elif word_count < 15:
            score = 5.0  # Short prompts are okay
        elif word_count < 50:
            score = 7.0  # Medium prompts are good
        else:
            score = 8.0  # Long prompts usually have clarity
        
        # Check for vague words - more penalty
        vague_words = ['thing', 'stuff', 'something', 'anything', 'maybe', 'perhaps', 'might', 'kinda', 'sorta']
        vague_count = sum(1 for word in vague_words if word in prompt.lower())
        score -= vague_count * 1.0  # Increased penalty
        
        # Check for clear action words - bonus
        clear_words = ['create', 'write', 'analyze', 'explain', 'describe', 'list', 'compare', 'summarize']
        clear_count = sum(1 for word in clear_words if word in prompt.lower())
        score += clear_count * 0.5
        
        # Check for question marks (questions are clearer)
        if '?' in prompt:
            score += 0.5
        
        return max(1.0, min(10.0, score))
    
    def _calculate_specificity_score(self, prompt: str) -> float:
        """FIXED: More dynamic specificity scoring."""
        word_count = len(prompt.split())
        
        # Base score on length
        if word_count < 10:
            score = 3.0  # Very short = not specific
        elif word_count < 30:
            score = 5.0  # Medium = somewhat specific
        else:
            score = 7.0  # Long = likely specific
        
        # Reward specific numbers, measurements, formats
        numbers = re.findall(r'\d+', prompt)
        score += min(len(numbers) * 0.8, 2.0)  # Increased bonus
        
        # Reward specific formats mentioned
        format_words = ['json', 'csv', 'markdown', 'html', 'pdf', 'bullet points', 'numbered list', 'table', 'report', 'essay']
        format_count = sum(1 for word in format_words if word.lower() in prompt.lower())
        score += min(format_count * 1.0, 2.0)  # Increased bonus
        
        # Reward specific domains/topics
        domain_words = ['business', 'technical', 'academic', 'marketing', 'sales', 'finance', 'education', 'health']
        domain_count = sum(1 for word in domain_words if word.lower() in prompt.lower())
        score += min(domain_count * 0.5, 1.5)
        
        # Heavy penalty for very vague requests
        vague_requests = ['help me', 'can you', 'please do', 'make it good', 'do something', 'fix this']
        vague_count = sum(1 for phrase in vague_requests if phrase in prompt.lower())
        score -= vague_count * 1.5  # Increased penalty
        
        return max(1.0, min(10.0, score))
    
    def _calculate_context_score(self, prompt: str) -> float:
        """FIXED: More dynamic context scoring."""
        word_count = len(prompt.split())
        
        # Base score heavily dependent on length
        if word_count < 8:
            score = 2.0  # Very short = no context
        elif word_count < 20:
            score = 4.0  # Short = little context
        elif word_count < 50:
            score = 6.0  # Medium = some context
        else:
            score = 8.0  # Long = good context
        
        # Reward context-providing words
        context_words = ['background', 'context', 'situation', 'purpose', 'goal', 'because', 'since', 'for', 'I need', 'I want']
        context_count = sum(1 for word in context_words if word.lower() in prompt.lower())
        score += min(context_count * 0.8, 2.0)  # Increased bonus
        
        # Reward personal details or specific scenarios
        personal_words = ['I am', 'my', 'our', 'we are', 'company', 'project', 'team']
        personal_count = sum(1 for word in personal_words if word.lower() in prompt.lower())
        score += min(personal_count * 0.3, 1.0)
        
        return max(1.0, min(10.0, score))
    
    def _calculate_constraint_score(self, prompt: str) -> float:
        """FIXED: More dynamic constraint scoring."""
        score = 4.0  # Lower starting point
        
        # Reward explicit formatting instructions
        format_instructions = ['format as', 'write in', 'use style', 'include', 'structure', 'organize', 'make it']
        format_count = sum(1 for instruction in format_instructions if instruction in prompt.lower())
        score += min(format_count * 1.0, 3.0)  # Increased bonus
        
        # Reward length specifications
        length_specs = ['words', 'characters', 'pages', 'paragraphs', 'sentences', 'bullet points', 'brief', 'detailed', 'long', 'short']
        length_count = sum(1 for spec in length_specs if spec in prompt.lower())
        score += min(length_count * 0.8, 2.0)
        
        # Reward tone/style specifications
        style_specs = ['tone', 'style', 'formal', 'casual', 'professional', 'friendly', 'technical', 'simple', 'advanced']
        style_count = sum(1 for spec in style_specs if spec in prompt.lower())
        score += min(style_count * 0.6, 2.0)
        
        # Reward audience specifications
        audience_specs = ['for', 'audience', 'beginner', 'expert', 'student', 'client', 'manager']
        audience_count = sum(1 for spec in audience_specs if spec in prompt.lower())
        score += min(audience_count * 0.5, 1.0)
        
        return max(1.0, min(10.0, score))
    
    def _calculate_goal_score(self, prompt: str) -> float:
        """FIXED: More dynamic goal scoring."""
        score = 4.0  # Lower starting point
        
        # Strong reward for clear action words
        action_words = ['create', 'write', 'analyze', 'design', 'develop', 'build', 'generate', 'produce', 'make', 'explain', 'describe']
        action_count = sum(1 for word in action_words if word in prompt.lower())
        score += min(action_count * 1.0, 3.0)  # Strong bonus
        
        # Reward outcome specifications
        outcome_words = ['result', 'output', 'deliverable', 'final', 'end goal', 'objective', 'want', 'need']
        outcome_count = sum(1 for word in outcome_words if word.lower() in prompt.lower())
        score += min(outcome_count * 0.8, 2.0)
        
        # Reward specific verbs that indicate clear intent
        intent_words = ['show', 'tell', 'find', 'solve', 'fix', 'improve', 'optimize', 'compare']
        intent_count = sum(1 for word in intent_words if word in prompt.lower())
        score += min(intent_count * 0.6, 1.5)
        
        # Heavy penalty for very unclear goals
        unclear_words = ['somehow', 'whatever', 'anything', 'something', 'help', 'please']
        unclear_count = sum(1 for word in unclear_words if word in prompt.lower())
        score -= unclear_count * 0.8
        
        return max(1.0, min(10.0, score))
    
    def _identify_strengths(self, prompt: str, clarity: float, specificity: float, context: float, constraints: float, goal: float) -> List[str]:
        """Identify prompt strengths based on scores."""
        strengths = []
        
        if clarity >= 7:
            strengths.append("Clear and unambiguous language")
        if specificity >= 7:
            strengths.append("Specific requirements and details provided")
        if context >= 7:
            strengths.append("Sufficient background context")
        if constraints >= 7:
            strengths.append("Well-defined formatting and style constraints")
        if goal >= 7:
            strengths.append("Clear goal and desired outcome")
        
        word_count = len(prompt.split())
        if word_count > 50:
            strengths.append("Comprehensive and detailed prompt")
        
        # Check for specific structural elements
        if any(word in prompt.lower() for word in ['include', 'format', 'structure']):
            strengths.append("Good structural guidance provided")
        
        if not strengths:
            strengths.append("Basic prompt structure in place")
        
        return strengths[:5]  # Limit to top 5 strengths
    
    def _identify_weaknesses(self, prompt: str, clarity: float, specificity: float, context: float, constraints: float, goal: float) -> List[str]:
        """Identify prompt weaknesses based on scores."""
        weaknesses = []
        
        if clarity < 6:
            weaknesses.append("Language could be clearer and less ambiguous")
        if specificity < 6:
            weaknesses.append("Needs more specific requirements and details")
        if context < 6:
            weaknesses.append("Lacks sufficient background context")
        if constraints < 6:
            weaknesses.append("Missing clear formatting and style guidelines")
        if goal < 6:
            weaknesses.append("Desired outcome could be more clearly defined")
        
        word_count = len(prompt.split())
        if word_count < 15:
            weaknesses.append("Prompt is too brief and lacks detail")
        
        # Check for vague language
        vague_words = ['thing', 'stuff', 'good', 'nice', 'help']
        if any(word in prompt.lower() for word in vague_words):
            weaknesses.append("Contains vague language that could be more specific")
        
        if not weaknesses:
            weaknesses.append("Minor improvements possible in overall clarity")
        
        return weaknesses[:5]  # Limit to top 5 weaknesses
    
    def _generate_suggestions(self, prompt: str, weaknesses: List[str]) -> List[str]:
        """Generate improvement suggestions based on identified weaknesses."""
        suggestions = []
        
        for weakness in weaknesses:
            if "clearer" in weakness or "ambiguous" in weakness:
                suggestions.append("Replace vague terms with specific, concrete language")
            elif "specific" in weakness or "details" in weakness:
                suggestions.append("Add specific numbers, formats, or measurable criteria")
            elif "context" in weakness:
                suggestions.append("Provide background information about your situation or goals")
            elif "formatting" in weakness or "guidelines" in weakness:
                suggestions.append("Specify desired output format (length, style, structure)")
            elif "outcome" in weakness or "goal" in weakness:
                suggestions.append("Clearly state what success looks like for this task")
            elif "brief" in weakness or "detail" in weakness:
                suggestions.append("Expand the prompt with more context and requirements")
            elif "vague" in weakness:
                suggestions.append("Replace general terms with specific, actionable language")
        
        # Add general suggestions if no specific ones were generated
        if not suggestions:
            suggestions.extend([
                "Consider adding more specific details about your requirements",
                "Include context about your intended audience or use case",
                "Specify the desired format and length of the output"
            ])
        
        return suggestions[:5]  # Limit to top 5 suggestions
    
    def _improve_prompt(self, prompt: str, weaknesses: List[str]) -> str:
        """Generate an improved version of the prompt."""
        if len(prompt.split()) < 15:
            # For very short prompts, provide a more detailed template
            return f"""
{prompt}

Please provide a comprehensive response that includes:
- Clear explanations with specific examples
- Structured format with headings or bullet points
- Relevant context and background information
- Actionable insights or recommendations
- Sources or references where applicable

Target length: 200-500 words
Tone: Professional and informative
""".strip()
        
        # For longer prompts, make minimal improvements
        improved = prompt
        
        # Add formatting request if missing
        if "format" not in prompt.lower():
            improved += "\n\nPlease format your response with clear headings and structure."
        
        # Add length specification if missing
        if not any(word in prompt.lower() for word in ['words', 'length', 'brief', 'detailed']):
            improved += " Aim for a comprehensive response of 300-500 words."
        
        return improved
    
    def _get_ai_analysis(self, prompt: str, analysis_type: str) -> Dict[str, Any]:
        """FIXED: Get AI-powered analysis with better error handling."""
        if self.debug:
            print("🤖 Attempting AI analysis...")
        
        try:
            from core.ai_service import AIServiceManager, AIServiceError
            
            service_manager = AIServiceManager()
            service = service_manager.get_service()
            full_prompt = self.meta_prompts[analysis_type] + prompt
            
            if self.debug:
                print(f"Full prompt length: {len(full_prompt)} characters")
            
            raw_response = service.generate_response(full_prompt)
            
            if self.debug:
                print(f"Raw AI response: {raw_response[:200]}{'...' if len(raw_response) > 200 else ''}")
            
            # Clean and parse JSON response
            clean_response = re.sub(r'```json\s*|\s*```', '', raw_response).strip()
            
            # Try to find JSON in the response if it's embedded in text
            json_match = re.search(r'\{.*\}', clean_response, re.DOTALL)
            if json_match:
                clean_response = json_match.group(0)
            
            parsed_response = json.loads(clean_response)
            
            if self.debug:
                print(f"Parsed JSON keys: {list(parsed_response.keys())}")
            
            # Validate the response structure
            if self._validate_ai_response(parsed_response):
                if self.debug:
                    print("✅ AI response validation passed")
                return parsed_response
            else:
                if self.debug:
                    print("❌ AI response validation failed")
                return None
            
        except json.JSONDecodeError as e:
            if self.debug:
                print(f"❌ JSON decode error: {e}")
            return None
        except Exception as e:
            if self.debug:
                print(f"❌ AI Analysis error: {type(e).__name__}: {e}")
            return None
    
    def _validate_ai_response(self, response: Dict[str, Any]) -> bool:
        """Validate that AI response has the expected structure."""
        required_keys = ["scores", "analysis", "improved_prompt", "confidence"]
        score_keys = ["clarity", "specificity", "context", "constraints", "goal_orientation", "overall"]
        analysis_keys = ["strengths", "weaknesses", "suggestions"]
        
        # Check main structure
        if not all(key in response for key in required_keys):
            if self.debug:
                missing = [key for key in required_keys if key not in response]
                print(f"Missing main keys: {missing}")
            return False
        
        # Check scores structure
        scores = response.get("scores", {})
        if not all(key in scores for key in score_keys):
            if self.debug:
                missing = [key for key in score_keys if key not in scores]
                print(f"Missing score keys: {missing}")
            return False
        
        # Check analysis structure
        analysis = response.get("analysis", {})
        if not all(key in analysis for key in analysis_keys):
            if self.debug:
                missing = [key for key in analysis_keys if key not in analysis]
                print(f"Missing analysis keys: {missing}")
            return False
        
        # Check that values are reasonable - handle arrays from Gemini
        for key, score in scores.items():
            # Extract number from array if needed
            if isinstance(score, list) and len(score) == 1:
                score = score[0]
                scores[key] = score  # Fix the score in place
            
            if not isinstance(score, (int, float)) or not 1 <= score <= 10:
                if self.debug:
                    print(f"Invalid score for {key}: {score}")
                return False
        
        confidence = response.get("confidence", 0)
        if not isinstance(confidence, (int, float)) or not 0 <= confidence <= 1:
            if self.debug:
                print(f"Invalid confidence: {confidence}")
            return False
        
        return True
    
    def _is_valid_ai_analysis(self, ai_analysis: Dict[str, Any]) -> bool:
        """Check if AI analysis is valid and not a fallback."""
        if not ai_analysis:
            return False
        
        scores = ai_analysis.get("scores", {})
        overall_score = scores.get("overall", 0)
        
        # If overall score is exactly 5.0 or between 5.5-5.7, it might be fallback
        if overall_score == 5.0 or (5.5 <= overall_score <= 5.7):
            if self.debug:
                print(f"⚠️  Suspicious overall score: {overall_score} (might be fallback)")
            # Additional checks to confirm it's real AI analysis
            confidence = ai_analysis.get("confidence", 0)
            if confidence == 0.7:  # Rule-based confidence
                return False
        
        return True