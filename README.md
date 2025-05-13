# HeartWise - Heart Disease Prediction

**HeartWise** is a web application designed to predict the risk of heart disease using machine learning. The goal is to help users detect potential risks early by analyzing clinical parameters such as age, sex, blood pressure, cholesterol levels, and more.

## 🎯 Features:

- Achieve a prediction accuracy of over **80%**
- Provide a **simple and intuitive interface** accessible to non-technical users
- Store data to track and improve the model's performance

## 🛠️ Technologies Used

### Backend
- **Python** (machine learning model)
- **Flask** (web framework)
- **Scikit-learn**, **Pandas**, **NumPy** (data processing and model training)
- **MongoDB** (for storing prediction data)
- **PyMongo** (to connect Python with MongoDB)

### Frontend
- **HTML/CSS** : `index.html`, `formulaire.html`, `result.html`

## 🧪 Dataset Used

The model was trained using `heart_disease_data.csv`, which includes clinical attributes such as:
- `age`, `sex`, `cp` (chest pain type), `chol` (cholesterol), `thalach` (max heart rate), and more
- `target` : 1 = heart disease present, 0 = no heart disease


## 🚀 How to Run the App

1. **clone the repository:**
   git clone https://github.com/zayneb-hamdi/Heart-Disease-Prediction-Project.git   
   cd Heart-Disease-Prediction-Project

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
3. **Set Up MongoDB:**  
  *Install MongoDB on your system.  
  *Start the MongoDB service.  
  *Create a database named prediction_db with a collection named cases.  
4. **run the application:**
   ```bash
   python app.py
6. **open your browser at:**
   ```bash
    http://localhost:5000/


