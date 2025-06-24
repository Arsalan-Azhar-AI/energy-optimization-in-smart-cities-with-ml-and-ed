# 🔌 Energy Optimization in Smart Cities using Machine Learning & Deep Learning

> A smart solution to detect anomalies in electricity consumption using Random Forest and Deep Learning models.

---

## 📘 Project Description

This project is designed to optimize energy consumption in smart cities by detecting **anomalous usage patterns**. It uses machine learning models to analyze electricity usage data alongside environmental conditions (temperature, humidity, etc.) and classify whether the pattern is **normal** or **anomalous**.

---

## 🧠 Technologies Used

- Python
- Flask (for Web App)
- Pandas, NumPy
- Scikit-learn
- XGBoost
- HTML, CSS (Glassmorphism UI)
- Docker (for containerization)

---

## 📂 Folder Structure


---

## 📈 Dataset Features

| Feature                  | Description                   |
|--------------------------|-------------------------------|
| `Electricity_Consumed`   | Current usage in kWh          |
| `Temperature`            | Temperature in °C             |
| `Humidity`               | Percentage humidity           |
| `Wind_Speed`             | Wind speed in m/s             |
| `Avg_Past_Consumption`   | Past average consumption      |
| `Anomaly_Label`          | 0 = Normal, 1 = Anomaly       |

---

## ⚙️ Project Workflow

1. ✅ **Data Loading and Preprocessing**
   - CSV from Kaggle
   - Dropped timestamp
   - Label encoding for classification

2. ⚖️ **Balancing Dataset**
   - Undersampled majority class to 250 records

3. 📊 **Feature Selection**
   - Correlation matrix
   - Chi-Square, ANOVA, Mutual Info
   - Model-based: Random Forest, XGBoost, Lasso

4. 🔍 **Model Training**
   - Logistic Regression (58%)
   - SVM (69%)
   - Bi-LSTM (74%)
   - Decision Tree (83%)
   - Bagging, AdaBoost (84–86%)
   - ✅ **Random Forest: 97% accuracy**

5. 💾 **Model Saving**
   - Trained model saved as `my_model.pkl`

6. 🌐 **Web App UI**
   - Built using Flask + HTML/CSS
   - Responsive UI with input form and live prediction
   - Styled with glassmorphism and modern design

---

## 🚀 Run Locally

### Step 1: Clone the Repo
```bash
git clone https://github.com/yourusername/energy-anomaly-detector.git
cd energy-anomaly-detector

### Step 2:
pip install -r requirements.txt

### Step 3:
python app.py

### Step 4:
docker build -t smartcity-energy-app .

### Step 5:
docker run -p 5000:5000 smartcity-energy-app


✍️ Author
Arsalan Azhar
BS Computer Science (2021–2025)
Final Year Project – University of Haripur


📃 License
This project is licensed for academic and educational use.