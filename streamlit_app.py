import streamlit as st
import pandas as pd
import numpy as np
import pickle
import re
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
from sklearn.model_selection import train_test_split
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

# Set page config
st.set_page_config(
    page_title="Fake News Detection",
    page_icon="📰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #1e3d59;
        text-align: center;
        margin-bottom: 2rem;
        font-weight: bold;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #f5f0e1;
        text-align: center;
        margin-bottom: 1rem;
    }
    .prediction-box {
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
        text-align: center;
        font-weight: bold;
        font-size: 1.2rem;
    }
    .fake-news {
        background-color: #ff4444;
        color: white;
    }
    .real-news {
        background-color: #44ff44;
        color: white;
    }
    .sidebar-info {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Text preprocessing function
def wordopt(text):
    text = text.lower()
    text = re.sub(r'\[.*?\]', '', text)
    text = re.sub(r"\\W", " ", text) 
    text = re.sub(r'https?://\S+|www\.\S+', '', text)
    text = re.sub(r'<.*?>+', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub(r'\n', '', text)
    text = re.sub(r'\w*\d\w*', '', text)    
    return text

# Load and prepare data
@st.cache_data
def load_data():
    try:
        df_fake = pd.read_csv("Fake.csv")
        df_true = pd.read_csv("True.csv")
        
        # Add class labels
        df_fake["class"] = 0
        df_true["class"] = 1
        
        # Remove last 10 rows for manual testing
        df_fake = df_fake[:-10]
        df_true = df_true[:-10]
        
        # Merge datasets
        df_merge = pd.concat([df_fake, df_true], axis=0)
        
        # Remove unnecessary columns
        df = df_merge.drop(["title", "subject", "date"], axis=1)
        
        # Shuffle the dataset
        df = df.sample(frac=1).reset_index(drop=True)
        
        # Process text
        df["text"] = df["text"].apply(wordopt)
        
        return df
    except Exception as e:
        st.error(f"Error loading data: {str(e)}")
        return None

# Train models
@st.cache_resource
def train_models():
    df = load_data()
    if df is None:
        return None, None
    
    # Define features and target
    X = df["text"]
    y = df["class"]
    
    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)
    
    # Vectorize text
    vectorizer = TfidfVectorizer(max_features=5000)
    X_train_vec = vectorizer.fit_transform(X_train)
    X_test_vec = vectorizer.transform(X_test)
    
    # Train models
    models = {
        'Logistic Regression': LogisticRegression(random_state=42),
        'Decision Tree': DecisionTreeClassifier(random_state=42),
        'Gradient Boosting': GradientBoostingClassifier(random_state=42),
        'Random Forest': RandomForestClassifier(random_state=42)
    }
    
    trained_models = {}
    model_scores = {}
    
    for name, model in models.items():
        model.fit(X_train_vec, y_train)
        score = model.score(X_test_vec, y_test)
        trained_models[name] = model
        model_scores[name] = score
    
    return trained_models, vectorizer, model_scores

# Prediction function
def predict_news(text, models, vectorizer):
    processed_text = wordopt(text)
    text_vec = vectorizer.transform([processed_text])
    
    predictions = {}
    for name, model in models.items():
        pred = model.predict(text_vec)[0]
        prob = model.predict_proba(text_vec)[0]
        predictions[name] = {
            'prediction': 'Real News' if pred == 1 else 'Fake News',
            'confidence': max(prob) * 100
        }
    
    return predictions

# Main app
def main():
    # Header
    st.markdown('<h1 class="main-header">📰 Fake News Detection System</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Detect fake news using advanced machine learning algorithms</p>', unsafe_allow_html=True)
    
    # Sidebar
    with st.sidebar:
        st.header("📊 Model Information")
        
        # Load models
        with st.spinner("Loading models..."):
            models, vectorizer, model_scores = train_models()
        
        if models is None:
            st.error("Failed to load models. Please check your data files.")
            return
        
        st.success("✅ Models loaded successfully!")
        
        # Display model accuracies
        st.subheader("Model Accuracies")
        for model_name, score in model_scores.items():
            st.metric(model_name, f"{score:.3f}")
        
        # Model info
        st.markdown("""
        <div class="sidebar-info">
        <h4>📈 About the Models</h4>
        <p>This system uses 4 different machine learning algorithms to detect fake news:</p>
        <ul>
        <li><strong>Logistic Regression</strong>: Linear classification model</li>
        <li><strong>Decision Tree</strong>: Rule-based classification</li>
        <li><strong>Gradient Boosting</strong>: Ensemble boosting method</li>
        <li><strong>Random Forest</strong>: Ensemble of decision trees</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Main content
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.header("🔍 News Article Analysis")
        
        # Text input
        news_text = st.text_area(
            "Enter the news article text you want to analyze:",
            height=200,
            placeholder="Paste your news article here..."
        )
        
        # Analysis button
        if st.button("🚀 Analyze News Article", type="primary"):
            if news_text.strip():
                with st.spinner("Analyzing..."):
                    predictions = predict_news(news_text, models, vectorizer)
                
                # Display predictions
                st.subheader("📊 Analysis Results")
                
                # Create columns for each model prediction
                cols = st.columns(2)
                for i, (model_name, result) in enumerate(predictions.items()):
                    with cols[i % 2]:
                        prediction_class = "real-news" if result['prediction'] == 'Real News' else "fake-news"
                        st.markdown(f"""
                        <div class="prediction-box {prediction_class}">
                            <h4>{model_name}</h4>
                            <p>{result['prediction']}</p>
                            <p>Confidence: {result['confidence']:.1f}%</p>
                        </div>
                        """, unsafe_allow_html=True)
                
                # Consensus prediction
                fake_count = sum(1 for pred in predictions.values() if pred['prediction'] == 'Fake News')
                consensus = "Fake News" if fake_count >= 2 else "Real News"
                consensus_class = "fake-news" if consensus == "Fake News" else "real-news"
                
                st.subheader("🎯 Consensus Prediction")
                st.markdown(f"""
                <div class="prediction-box {consensus_class}">
                    <h3>Final Verdict: {consensus}</h3>
                    <p>{fake_count}/4 models predicted Fake News</p>
                </div>
                """, unsafe_allow_html=True)
                
                # Visualization
                st.subheader("📈 Model Predictions Visualization")
                
                # Prepare data for visualization
                model_names = list(predictions.keys())
                pred_values = [1 if pred['prediction'] == 'Real News' else 0 for pred in predictions.values()]
                confidences = [pred['confidence'] for pred in predictions.values()]
                
                # Create bar chart
                fig = go.Figure()
                colors = ['#44ff44' if val == 1 else '#ff4444' for val in pred_values]
                
                fig.add_trace(go.Bar(
                    x=model_names,
                    y=confidences,
                    marker_color=colors,
                    text=[f"{conf:.1f}%" for conf in confidences],
                    textposition='auto',
                ))
                
                fig.update_layout(
                    title="Model Confidence Scores",
                    xaxis_title="Models",
                    yaxis_title="Confidence (%)",
                    yaxis=dict(range=[0, 100]),
                    height=400
                )
                
                st.plotly_chart(fig, use_container_width=True)
                
            else:
                st.warning("⚠️ Please enter some news text to analyze.")
    
    with col2:
        st.header("📝 Sample News Articles")
        
        # Sample articles for testing
        sample_articles = {
            "Real News Sample": """
            Scientists at MIT have developed a new method for detecting early-stage cancer using artificial intelligence. 
            The research, published in Nature Medicine, shows promising results in clinical trials with 95% accuracy 
            in detecting malignant tumors before they become visible through traditional imaging methods.
            """,
            "Suspicious Sample": """
            BREAKING: Secret government documents reveal aliens have been living among us for decades! 
            Multiple sources confirm that world leaders are actually extraterrestrial beings controlling our planet. 
            This shocking truth has been hidden from the public for too long!
            """
        }
        
        for title, content in sample_articles.items():
            with st.expander(f"📰 {title}"):
                st.write(content)
                if st.button(f"Analyze this article", key=title):
                    st.session_state['sample_text'] = content
                    st.rerun()
        
        # Tips section
        st.header("💡 Detection Tips")
        st.markdown("""
        **Look out for these red flags:**
        - Sensational headlines with ALL CAPS
        - Lack of credible sources
        - Emotional language instead of facts
        - Claims without evidence
        - Poor grammar and spelling
        - Unusual or suspicious URLs
        """)
        
        # Statistics
        if models is not None:
            st.header("📊 System Stats")
            st.metric("Models Trained", "4")
            st.metric("Best Accuracy", f"{max(model_scores.values()):.3f}")
            st.metric("Average Accuracy", f"{np.mean(list(model_scores.values())):.3f}")

    # Footer
    st.markdown("---")
    st.markdown(
        """
        <div style='text-align: center; color: #666666; padding: 2rem;'>
            <p>🔬 Built with Streamlit | 🤖 Powered by Machine Learning</p>
            <p>⚠️ This tool is for educational purposes. Always verify news from multiple credible sources.</p>
        </div>
        """, 
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
