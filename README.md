# 📰 Fake News Detection System

A sophisticated machine learning-powered web application built with Streamlit that can detect fake news articles using multiple ML algorithms.

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-239120?style=for-the-badge&logo=plotly&logoColor=white)

## 🚀 Live Demo

**[Try the App Live on Streamlit Cloud](https://your-app-name.streamlit.app)** *(Update this link after deployment)*

## ✨ Features

- 🤖 **4 ML Models**: Logistic Regression, Decision Tree, Gradient Boosting, Random Forest
- 📊 **Interactive Dashboard**: Beautiful visualizations with Plotly
- 🎯 **Consensus Prediction**: Combines predictions from all models
- 📈 **Confidence Scores**: Shows model confidence levels
- 💾 **Model Persistence**: Saves trained models for faster loading
- 🎨 **Professional UI**: Custom CSS styling with responsive design
- 📱 **Mobile Friendly**: Works on all device sizes

## 🖼️ Screenshots

### Main Interface
![Main Interface](https://via.placeholder.com/800x400?text=Add+Screenshot+Here)

### Prediction Results
![Prediction Results](https://via.placeholder.com/800x400?text=Add+Screenshot+Here)

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/fake-news-detection.git
   cd fake-news-detection
   ```

2. **Create virtual environment** (recommended)
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   streamlit run app.py
   ```

5. **Open your browser** to `http://localhost:8501`

### Quick Setup Script

For faster setup, you can use the included quick fix script:

```bash
python quick_fix.py
```

## 🌐 Deployment

### Deploy to Streamlit Cloud (Recommended)

1. **Fork this repository** to your GitHub account

2. **Go to [share.streamlit.io](https://share.streamlit.io)**

3. **Click "New app"**

4. **Connect your GitHub repository**
   - Repository: `yourusername/fake-news-detection`
   - Branch: `main`
   - Main file path: `app.py`

5. **Click "Deploy"**

6. **Your app will be live** at `https://your-app-name.streamlit.app`

### Alternative Deployment Options

#### Heroku
```bash
# Install Heroku CLI, then:
heroku create your-app-name
git push heroku main
```

#### Docker
```bash
docker build -t fake-news-detection .
docker run -p 8501:8501 fake-news-detection
```

## 📊 Dataset

The application uses two datasets:
- **Fake.csv**: ~23,490 fake news articles
- **True.csv**: ~21,418 real news articles

**Sources**: The datasets contain news articles from various sources, preprocessed and labeled for machine learning training.

## 🧠 Machine Learning Models

### Model Architecture

1. **Text Preprocessing**
   - Lowercasing
   - URL removal
   - HTML tag removal
   - Punctuation removal
   - Number removal

2. **Feature Extraction**
   - TF-IDF Vectorization
   - Max features: 2,000
   - Min document frequency: 2
   - Max document frequency: 95%

3. **Models Used**
   - **Logistic Regression**: Linear classification with L2 regularization
   - **Decision Tree**: Rule-based classification with max depth 10
   - **Gradient Boosting**: Ensemble method with 50 estimators
   - **Random Forest**: Ensemble of 50 decision trees

### Performance Metrics

| Model | Accuracy | Training Time |
|-------|----------|---------------|
| Logistic Regression | ~94% | Fast |
| Decision Tree | ~92% | Fast |
| Gradient Boosting | ~95% | Medium |
| Random Forest | ~94% | Medium |

## 🔧 Configuration

### Streamlit Configuration

The app includes a `.streamlit/config.toml` file for customization:

```toml
[theme]
primaryColor = "#1f77b4"
backgroundColor = "#ffffff"
secondaryBackgroundColor = "#f0f2f6"
textColor = "#262730"

[server]
runOnSave = true
```

### Environment Variables

You can set these environment variables:

- `STREAMLIT_SERVER_PORT`: Port number (default: 8501)
- `STREAMLIT_SERVER_ADDRESS`: Server address (default: localhost)

## 📁 Project Structure

```
fake-news-detection/
│
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── Fake.csv              # Fake news dataset
├── True.csv              # Real news dataset
├── fake-news-detection.ipynb  # Jupyter notebook (development)
└── README.md             # This file
```

## 🔧 Technical Details

### Models Used
- **Logistic Regression**: Linear classification for baseline performance
- **Decision Tree**: Rule-based classification with interpretable results
- **Gradient Boosting**: Ensemble method for improved accuracy
- **Random Forest**: Robust ensemble of decision trees

### Text Preprocessing
- Lowercase conversion
- URL removal
- HTML tag removal
- Punctuation removal
- Number removal
- Special character cleaning

### Features
- **TF-IDF Vectorization**: Converts text to numerical features
- **Cross-validation**: Ensures model reliability
- **Confidence Scoring**: Provides prediction certainty
- **Consensus Voting**: Combines multiple model predictions

## 🎯 Usage

1. **Input Text**: Paste or type the news article you want to analyze
2. **Click Analyze**: The system will process the text through all models
3. **View Results**: See individual model predictions and consensus verdict
4. **Interpret Confidence**: Higher confidence indicates more certain predictions

## 📊 Model Performance

The system displays real-time accuracy metrics for each model, typically achieving:
- Overall accuracy: 85-95%
- Precision: High for both fake and real news detection
- Recall: Balanced across both classes

## ⚠️ Important Notes

- This tool is for educational and research purposes
- Always verify news from multiple credible sources
- The models are trained on specific datasets and may have limitations
- Consider the confidence scores when interpreting results

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📝 License

This project is open source and available under the MIT License.

## 🆘 Support

If you encounter any issues:
1. Check that all CSV files are in the correct location
2. Ensure all dependencies are installed correctly
3. Verify Python version compatibility (3.7+)
4. Check Streamlit Cloud deployment logs for errors

## 🔮 Future Enhancements

- Additional ML models (Neural Networks, BERT)
- Real-time news feed integration
- Multi-language support
- Advanced visualization dashboards
- API endpoint for integration
- Mobile-responsive design improvements

---

Made with ❤️ using Streamlit and scikit-learn