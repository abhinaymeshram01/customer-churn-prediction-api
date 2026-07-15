# 🚀 Customer Churn Prediction API

An end-to-end Machine Learning project that predicts whether a telecom customer is likely to churn. The project demonstrates a complete ML deployment pipeline using **Scikit-learn**, **FastAPI**, **Docker**, and **AWS EC2**.

---

## 📌 Project Overview

Customer churn is one of the biggest challenges for telecom companies. Predicting customers who are likely to leave helps businesses take proactive measures to improve customer retention.

This project builds a Machine Learning model to predict customer churn and deploys it as a REST API using FastAPI. The application is containerized with Docker and deployed on AWS EC2, following a production-style workflow.

---

## ✨ Features

- Data preprocessing and feature engineering
- Scikit-learn Pipeline
- ColumnTransformer for preprocessing
- Random Forest Classifier
- FastAPI REST API
- Interactive Swagger UI
- Docker containerization
- AWS EC2 deployment
- Modular project structure
- Easy deployment using GitHub

---

## 🛠 Tech Stack

| Category | Technology |
|----------|------------|
| Language | Python |
| Data Analysis | Pandas, NumPy |
| Machine Learning | Scikit-learn |
| API | FastAPI |
| API Server | Uvicorn |
| Model Serialization | Joblib |
| Containerization | Docker |
| Cloud Platform | AWS EC2 |
| Version Control | Git & GitHub |

---

## 📂 Project Structure

```text
customer-churn-prediction-api/
│
├── app/
│   ├── main.py
│   ├── schema.py
│   └── utils.py
│
├── model/
│   └── customer_churn_pipeline.pkl
│
├── Dockerfile
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🔄 Machine Learning Workflow

- Data Collection
- Data Cleaning
- Feature Engineering
- Exploratory Data Analysis
- Train-Test Split
- Data Preprocessing
- ColumnTransformer
- Scikit-learn Pipeline
- Model Training
- Model Evaluation
- Model Serialization using Joblib
- FastAPI Deployment
- Docker Containerization
- AWS EC2 Deployment

---

## 📊 Dataset Features

### Numerical Features

- tenure
- MonthlyCharges
- TotalCharges
- ChargePerMonth
- service_count
- HasPremiumServices
- IsHighValue

### Categorical Features

- gender
- SeniorCitizen
- Partner
- Dependents
- PhoneService
- MultipleLines
- InternetService
- OnlineSecurity
- OnlineBackup
- DeviceProtection
- TechSupport
- StreamingTV
- StreamingMovies
- Contract
- PaperlessBilling
- PaymentMethod
- tenure_group

---

## 🤖 Machine Learning Models

The following models were evaluated during experimentation:

- Logistic Regression
- Decision Tree
- K-Nearest Neighbors (KNN)
- Random Forest
- Gradient Boosting
- AdaBoost
- XGBoost

The final deployed model is **Random Forest Classifier**.

---

## 📈 Model Performance

Replace the values below with your final evaluation metrics.

| Metric | Score |
|---------|------:|
| Accuracy | XX.XX |
| Precision | XX.XX |
| Recall | XX.XX |
| F1 Score | XX.XX |
| ROC-AUC | XX.XX |

---

## ⚙ Installation

Clone the repository.

```bash
git clone https://github.com/your-username/customer-churn-prediction-api.git
```

Move to the project directory.

```bash
cd customer-churn-prediction-api
```

---

## 🐳 Run Using Docker

Build the Docker image.

```bash
docker build -t customer-churn-api .
```

Run the Docker container.

```bash
docker run -d -p 8000:8000 customer-churn-api
```

Verify that the container is running.

```bash
docker ps
```

---

## ▶ Run Without Docker

Install dependencies.

```bash
pip install -r requirements.txt
```

Run the FastAPI application.

```bash
uvicorn app.main:app --reload
```

---

## 🌐 API Documentation

After starting the application locally:

```text
http://localhost:8000/docs
```

If deployed on AWS EC2:

```text
http://<EC2-PUBLIC-IP>:8000/docs
```

Swagger UI provides an interactive interface to test the API.

---

## 📥 Sample Request

```json
{
  "gender": "Male",
  "SeniorCitizen": 0,
  "Partner": "Yes",
  "Dependents": "No",
  "tenure": 24,
  "PhoneService": "Yes",
  "MultipleLines": "No",
  "InternetService": "Fiber optic",
  "OnlineSecurity": "No",
  "OnlineBackup": "Yes",
  "DeviceProtection": "No",
  "TechSupport": "No",
  "StreamingTV": "Yes",
  "StreamingMovies": "Yes",
  "Contract": "Month-to-month",
  "PaperlessBilling": "Yes",
  "PaymentMethod": "Electronic check",
  "MonthlyCharges": 89.5,
  "TotalCharges": 2148.0,
  "ChargePerMonth": 89.5,
  "service_count": 5,
  "HasPremiumServices": 1,
  "IsHighValue": 1,
  "tenure_group": "2-3 Years"
}
```

---

## 📤 Sample Response

```json
{
  "prediction": "Yes",
  "probability": 0.91
}
```

---

## 🐳 Docker Commands

Build Docker image.

```bash
docker build -t customer-churn-api .
```

Run Docker container.

```bash
docker run -d -p 8000:8000 customer-churn-api
```

List running containers.

```bash
docker ps
```

Stop container.

```bash
docker stop <container-id>
```

Remove container.

```bash
docker rm <container-id>
```

Remove Docker image.

```bash
docker rmi customer-churn-api
```

---

## ☁ AWS EC2 Deployment

1. Launch an Ubuntu EC2 instance.
2. Connect to the instance using SSH.
3. Install Docker.
4. Clone this GitHub repository.
5. Build the Docker image.
6. Run the Docker container.
7. Allow inbound traffic on port **8000** in the EC2 Security Group.
8. Open the API using:

```text
http://<EC2-PUBLIC-IP>:8000/docs
```

---

## 🚀 Future Improvements

- CI/CD using GitHub Actions
- Kubernetes Deployment
- AWS ECS Deployment
- Model Monitoring
- API Authentication
- Logging and Monitoring
- Automated Model Retraining
- Unit and Integration Testing

---

## 👨‍💻 Author

**Abhinay Meshram**

Machine Learning Engineer

- GitHub: https://github.com/your-abhinaymeshram01
- LinkedIn: https://www.linkedin.com/in/abhinaymeshram01/

---

## 📄 License

This project is licensed under the MIT License.

---

⭐ If you found this project useful, consider giving it a star on GitHub.
````
