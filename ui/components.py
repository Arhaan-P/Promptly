import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from typing import List, Dict, Any

class UIComponents:
    """Professional, minimalistic UI components."""
    
    def render_header(self):
        """Render clean application header."""
        st.markdown("""
        <div class="main-header">
            <h1>🚀 Promptly</h1>
            <p class="subtitle">AI-Powered Prompt Analysis Platform</p>
        </div>
        """, unsafe_allow_html=True)
        
    def render_prompt_input(self) -> str:
        """Render clean prompt input area."""
        st.markdown("### Prompt Analysis")
        
        prompt = st.text_area(
            "Enter your prompt for analysis:",
            height=180,
            placeholder="Enter a detailed prompt that describes your task, requirements, and desired outcome...",
            help="💡 Be specific about requirements, context, and desired format for better analysis."
        )
            
        return prompt.strip() if prompt else ""
    
    def render_evaluation_results(self, result):
        """Render clean, professional evaluation results."""
        st.markdown("---")
        
        # Overall score with metrics
        col1, col2, col3, col4 = st.columns([2, 1, 1, 1])
        
        with col1:
            score_color = self._get_score_color(result.metrics.overall_score)
            st.markdown(f"""
            <div class="score-display">
                <h2>Overall Score</h2>
                <div class="score-value" style="color: {score_color};">{result.metrics.overall_score:.1f}/10</div>
                <p class="score-desc">{self._get_score_description(result.metrics.overall_score)}</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.metric("Words", result.metrics.word_count)
        with col3:
            st.metric("Sentences", result.metrics.sentence_count)
        with col4:
            confidence_pct = int(result.confidence_level * 100)
            st.metric("Confidence", f"{confidence_pct}%")
        
        # Metrics radar chart
        self._render_metrics_chart(result.metrics)
        
        # Results in clean cards
        col1, col2 = st.columns(2)
        
        with col1:
            self._render_strengths(result.strengths)
            
        with col2:
            self._render_weaknesses(result.weaknesses)
        
        # Suggestions
        self._render_suggestions(result.suggestions)
        
        # Improved prompt
        if result.improved_prompt and result.improved_prompt.strip() != result.metrics.__dict__.get('original_prompt', ''):
            st.markdown("### Optimized Prompt")
            st.code(result.improved_prompt, language="text")
            
            col1, col2 = st.columns([1, 3])
            with col1:
                if st.button("📋 Copy Optimized", key="copy_opt"):
                    st.success("Copied!")
    
    def _render_strengths(self, strengths: List[str]):
        """Render strengths in clean cards."""
        st.markdown("""
        <div class="result-card">
            <h3>✅ Strengths</h3>
        """, unsafe_allow_html=True)
        
        if strengths and strengths[0] != "Basic prompt structure":
            for strength in strengths[:4]:  # Limit to 4 items
                st.markdown(f'<div class="strength-item">• {strength}</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="strength-item">• Basic structure in place</div>', unsafe_allow_html=True)
            
        st.markdown("</div>", unsafe_allow_html=True)
    
    def _render_weaknesses(self, weaknesses: List[str]):
        """Render weaknesses in clean cards."""
        st.markdown("""
        <div class="result-card">
            <h3>⚠️ Areas for Improvement</h3>
        """, unsafe_allow_html=True)
        
        if weaknesses and weaknesses[0] != "Analysis service unavailable":
            for weakness in weaknesses[:4]:  # Limit to 4 items
                st.markdown(f'<div class="weakness-item">• {weakness}</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="weakness-item">• Minor improvements possible</div>', unsafe_allow_html=True)
            
        st.markdown("</div>", unsafe_allow_html=True)
    
    def _render_suggestions(self, suggestions: List[str]):
        """Render suggestions in clean cards."""
        st.markdown("""
        <div class="result-card">
            <h3>💡 Enhancement Suggestions</h3>
        """, unsafe_allow_html=True)
        
        if suggestions and suggestions[0] != "Try again later":
            for i, suggestion in enumerate(suggestions[:4], 1):  # Limit to 4 items
                st.markdown(f'<div class="suggestion-item">{i}. {suggestion}</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="suggestion-item">1. Add more specific details and context</div>', unsafe_allow_html=True)
            
        st.markdown("</div>", unsafe_allow_html=True)
    
    def _get_score_color(self, score: float) -> str:
        """Get color based on score."""
        if score >= 8:
            return "#10b981"  # Green
        elif score >= 6:
            return "#f59e0b"  # Amber
        else:
            return "#ef4444"  # Red
    
    def _get_score_description(self, score: float) -> str:
        """Get description based on score."""
        if score >= 8:
            return "Excellent quality"
        elif score >= 6:
            return "Good, can improve"
        else:
            return "Needs improvement"
    
    def _render_metrics_chart(self, metrics):
        """Render clean metrics radar chart."""
        st.markdown("### Quality Metrics")
        
        categories = ['Clarity', 'Specificity', 'Context', 'Constraints', 'Goal Focus']
        values = [
            metrics.clarity_score,
            metrics.specificity_score, 
            metrics.context_score,
            metrics.constraint_score,
            metrics.goal_orientation_score
        ]
        
        fig = go.Figure()
        
        fig.add_trace(go.Scatterpolar(
            r=values,
            theta=categories,
            fill='toself',
            name='Current',
            line=dict(color='#3b82f6', width=2),
            fillcolor='rgba(59, 130, 246, 0.2)'
        ))
        
        fig.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, 10],
                    tickmode='linear',
                    tick0=0,
                    dtick=2,
                    gridcolor='#e5e7eb'
                ),
                angularaxis=dict(
                    tickfont=dict(size=11, color='#6b7280')
                )
            ),
            showlegend=False,
            height=400,
            margin=dict(t=20, b=20, l=20, r=20),
            paper_bgcolor='white',
            plot_bgcolor='white',
            font=dict(family='Inter', color='#374151')
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    def render_analytics_dashboard(self, history: List[Dict]):
        """Render clean analytics dashboard."""
        if not history:
            st.markdown("""
            <div style="text-align: center; padding: 3rem; background: #f8fafc; 
                        border: 1px solid #e5e7eb; border-radius: 12px; margin: 2rem 0;">
                <h3 style="color: #374151; margin-bottom: 1rem;">📊 Analytics Dashboard</h3>
                <p style="color: #6b7280; margin: 0;">No evaluation history yet. Analyze some prompts to see your progress.</p>
            </div>
            """, unsafe_allow_html=True)
            return
            
        st.markdown("## Analytics Dashboard")
        
        # Summary stats
        scores = [h['result'].metrics.overall_score for h in history]
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Evaluations", len(history))
        with col2:
            avg_score = sum(scores) / len(scores)
            st.metric("Avg Score", f"{avg_score:.1f}/10")
        with col3:
            st.metric("Best Score", f"{max(scores):.1f}/10")
        with col4:
            improvement = scores[-1] - scores[0] if len(scores) > 1 else 0
            st.metric("Progress", f"{improvement:+.1f}")
        
        # Trend chart
        if len(history) > 1:
            fig = px.line(
                x=range(1, len(scores) + 1),
                y=scores,
                title="Score Progression",
                labels={'x': 'Evaluation', 'y': 'Score'},
                markers=True,
                color_discrete_sequence=['#3b82f6']
            )
            fig.update_layout(
                yaxis=dict(range=[0, 10]),
                height=350,
                margin=dict(t=40, b=40, l=40, r=40),
                paper_bgcolor='white',
                plot_bgcolor='white',
                font=dict(family='Inter')
            )
            st.plotly_chart(fig, use_container_width=True)
        
        # Recent evaluations
        st.markdown("### Recent Evaluations")
        for i, entry in enumerate(reversed(history[-3:]), 1):  # Show only 3 recent
            with st.expander(f"#{len(history) - i + 1} - Score: {entry['result'].metrics.overall_score:.1f}/10"):
                col1, col2 = st.columns([3, 1])
                with col1:
                    preview = entry['prompt'][:150] + "..." if len(entry['prompt']) > 150 else entry['prompt']
                    st.text(preview)
                with col2:
                    st.write(f"Words: {entry['result'].metrics.word_count}")
                    st.write(f"Complexity: {entry['result'].metrics.complexity_level}")
    
    def render_sidebar_content(self):
        """Render minimal sidebar content."""
        st.markdown("### Quick Actions")
        
        if st.button("🗑️ Clear History", help="Clear evaluation history"):
            if 'evaluation_history' in st.session_state:
                count = len(st.session_state.evaluation_history)
                st.session_state.evaluation_history = []
                st.success(f"Cleared {count} evaluations")
                st.rerun()
            
        st.markdown("### Session Stats")
        history_count = len(st.session_state.get('evaluation_history', []))
        cache_count = len(st.session_state.get('cache_store', {}))
        
        st.metric("Evaluations", history_count)
        st.metric("Cache Size", cache_count)
        
        if history_count > 0:
            scores = [h['result'].metrics.overall_score for h in st.session_state.evaluation_history]
            avg_score = sum(scores) / len(scores)
            st.metric("Average", f"{avg_score:.1f}")
    
    def render_footer(self):
        """Render minimal footer."""
        st.markdown("---")
        st.markdown("""
        <div style="text-align: center; padding: 1.5rem; color: #6b7280; font-size: 0.9rem;">
            <strong>Promptly</strong> - Professional prompt analysis platform
        </div>
        """, unsafe_allow_html=True)