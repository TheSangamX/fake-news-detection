# Fake News Detection System - Flowchart

## System Architecture & Workflow Diagram

```mermaid
flowchart TD
    A[🚀 Start Application] --> B[📱 Streamlit App Launch]
    B --> C[🎨 Load Custom CSS & UI Config]
    C --> D[📊 Initialize Sidebar]
    
    D --> E{📂 Load CSV Files}
    E -->|Success| F[📄 Load Fake.csv & True.csv]
    E -->|Error| Z1[❌ Display Error Message]
    
    F --> G[🏷️ Add Class Labels]
    G --> H1[Fake.csv → class = 0]
    G --> H2[True.csv → class = 1]
    
    H1 --> I[🔄 Merge Datasets]
    H2 --> I
    
    I --> J[🗑️ Remove Unnecessary Columns]
    J --> K[🔀 Shuffle Dataset]
    K --> L[🧹 Text Preprocessing]
    
    L --> M[📝 Text Processing Steps]
    M --> M1[Convert to Lowercase]
    M --> M2[Remove URLs & HTML Tags]
    M --> M3[Remove Punctuation]
    M --> M4[Remove Numbers]
    M --> M5[Remove Special Characters]
    
    M5 --> N[✂️ Train-Test Split]
    N --> O[📊 TF-IDF Vectorization]
    O --> P[🤖 Train 4 ML Models]
    
    P --> P1[🔵 Logistic Regression]
    P --> P2[🌳 Decision Tree]
    P --> P3[📈 Gradient Boosting]
    P --> P4[🌲 Random Forest]
    
    P1 --> Q[💾 Cache Trained Models]
    P2 --> Q
    P3 --> Q
    P4 --> Q
    
    Q --> R[📊 Display Model Accuracies]
    R --> S[🖥️ Show Main Interface]
    
    S --> T[👤 User Input Section]
    T --> U{📰 News Text Input?}
    
    U -->|No Text| U1[⚠️ Show Warning Message]
    U -->|Text Provided| V[🔍 Analyze Button Clicked]
    
    V --> W[🧹 Preprocess Input Text]
    W --> X[🔤 Convert to TF-IDF Vector]
    X --> Y[🤖 Run All 4 Models]
    
    Y --> Y1[🔵 LR Prediction & Confidence]
    Y --> Y2[🌳 DT Prediction & Confidence]
    Y --> Y3[📈 GBC Prediction & Confidence]
    Y --> Y4[🌲 RF Prediction & Confidence]
    
    Y1 --> AA[🎯 Calculate Consensus]
    Y2 --> AA
    Y3 --> AA
    Y4 --> AA
    
    AA --> BB{📊 Majority Vote}
    BB -->|≥2 Models Predict Fake| CC[🔴 Final Verdict: FAKE NEWS]
    BB -->|<2 Models Predict Fake| DD[🟢 Final Verdict: REAL NEWS]
    
    CC --> EE[📊 Display Results Grid]
    DD --> EE
    
    EE --> FF[📈 Generate Plotly Visualization]
    FF --> GG[🎨 Show Confidence Bar Chart]
    GG --> HH[📝 Display Sample Articles]
    HH --> II[💡 Show Detection Tips]
    II --> JJ[📊 Show System Statistics]
    
    JJ --> KK{🔄 Continue Using App?}
    KK -->|Yes| U
    KK -->|No| LL[👋 End Session]
    
    U1 --> U
    Z1 --> LL
    
    style A fill:#e1f5fe
    style CC fill:#ffebee,color:#d32f2f
    style DD fill:#e8f5e8,color:#2e7d32
    style P1 fill:#e3f2fd,color:#1976d2
    style P2 fill:#f3e5f5,color:#7b1fa2
    style P3 fill:#fff3e0,color:#f57c00
    style P4 fill:#e0f2f1,color:#388e3c
```

## Detailed Component Breakdown

### 1. 📱 Application Initialization
```mermaid
flowchart LR
    A[Streamlit Config] --> B[Page Title & Icon]
    B --> C[Layout: Wide]
    C --> D[Sidebar: Expanded]
    D --> E[Custom CSS Styling]
```

### 2. 🗄️ Data Pipeline
```mermaid
flowchart TD
    A[Raw CSV Files] --> B[Data Loading]
    B --> C[Label Assignment]
    C --> D[Data Cleaning]
    D --> E[Text Preprocessing]
    E --> F[Feature Engineering]
    
    F --> F1[TF-IDF Vectorization]
    F1 --> F2[Max Features: 5000]
    F2 --> F3[Train/Test Split: 75/25]
```

### 3. 🤖 Model Training Pipeline
```mermaid
flowchart TD
    A[Preprocessed Data] --> B[Train-Test Split]
    B --> C[TF-IDF Vectorization]
    C --> D[Parallel Model Training]
    
    D --> E1[Logistic Regression<br/>• Linear Classification<br/>• L2 Regularization<br/>• Random State: 42]
    D --> E2[Decision Tree<br/>• Rule-based Classification<br/>• Max Depth: Default<br/>• Random State: 42]
    D --> E3[Gradient Boosting<br/>• Ensemble Method<br/>• 100 Estimators<br/>• Random State: 42]
    D --> E4[Random Forest<br/>• Ensemble of Trees<br/>• 100 Estimators<br/>• Random State: 42]
    
    E1 --> F[Model Evaluation]
    E2 --> F
    E3 --> F
    E4 --> F
    
    F --> G[Cache Models with @st.cache_resource]
```

### 4. 🔍 Prediction Workflow
```mermaid
flowchart TD
    A[User Input Text] --> B[Text Preprocessing]
    B --> C[TF-IDF Transformation]
    C --> D[Multi-Model Prediction]
    
    D --> E1[LR: Prediction + Probability]
    D --> E2[DT: Prediction + Probability]
    D --> E3[GBC: Prediction + Probability]
    D --> E4[RF: Prediction + Probability]
    
    E1 --> F[Confidence Calculation]
    E2 --> F
    E3 --> F
    E4 --> F
    
    F --> G[Consensus Algorithm]
    G --> H{Majority Vote}
    H -->|≥50% Fake| I[🔴 FAKE NEWS]
    H -->|<50% Fake| J[🟢 REAL NEWS]
```

### 5. 🎨 UI Components Structure
```mermaid
flowchart TD
    A[Streamlit Main Page] --> B[Header Section]
    B --> C[Two-Column Layout]
    
    C --> D[Left Column - Analysis]
    C --> E[Right Column - Samples & Tips]
    
    D --> D1[Text Input Area]
    D --> D2[Analyze Button]
    D --> D3[Results Display]
    D --> D4[Confidence Chart]
    
    E --> E1[Sample Articles]
    E --> E2[Detection Tips]
    E --> E3[System Statistics]
    
    A --> F[Sidebar]
    F --> F1[Model Information]
    F --> F2[Accuracy Metrics]
    F --> F3[About Models]
```

### 6. 📊 Results Display System
```mermaid
flowchart TD
    A[Prediction Results] --> B[Individual Model Cards]
    B --> C[Color-Coded Display]
    C --> D[Consensus Section]
    D --> E[Interactive Plotly Chart]
    
    C --> C1[🟢 Real News: Green Background]
    C --> C2[🔴 Fake News: Red Background]
    
    E --> E1[Bar Chart: Model Confidence]
    E --> E2[X-axis: Model Names]
    E --> E3[Y-axis: Confidence %]
    E --> E4[Color: Prediction Result]
```

## 🔧 Technical Architecture

### Performance Optimizations
- **@st.cache_data**: Caches dataset loading
- **@st.cache_resource**: Caches trained models
- **Lazy Loading**: Models load only when needed
- **Efficient Vectorization**: TF-IDF with limited features

### Error Handling
- CSV file validation
- Model training error catching
- Input text validation
- Graceful degradation on failures

### Scalability Features
- Modular function design
- Configurable model parameters
- Extensible model architecture
- Deployment-ready structure

## 🚀 Deployment Flow
```mermaid
flowchart LR
    A[Local Development] --> B[GitHub Repository]
    B --> C[Streamlit Cloud]
    C --> D[Automatic Deployment]
    D --> E[Live Web Application]
    
    F[requirements.txt] --> C
    G[CSV Data Files] --> C
    H[app.py] --> C
```