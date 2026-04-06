# 💳 Projeto: Chatbot de Análise de Crédito

Projeto de Machine Learning com deploy utilizando **FastAPI + Streamlit + Docker** para análise de risco de crédito.

---

## 🚀 Funcionalidades

- 📊 Modelo de Machine Learning para prever inadimplência
- ⚡ API REST com FastAPI
- 🖥️ Interface interativa com Streamlit
- 🐳 Deploy containerizado com Docker Compose

---

## 🧠 Como funciona

O usuário insere dados financeiros e pessoais, e o sistema retorna:

- ✅ Predição: risco de inadimplência (0 ou 1)
- 📈 Probabilidade de default

![ChatBot]([https://i.imgur.com/YV5kpa6.gif](https://i.imgur.com/YV5kpa6.gif))

---

## 🏗️ Estrutura do Projeto

```
chatbotcredito/
│
├── app/
│ ├── api/
│ │ └── app.py 				# FastAPI
│ ├── chatbot/
│ │ └── chatbot.py			# Streamlit
│
├── data/
| └── processed/
|   └── dados_tratados.csv		# Dataset tratado após o EDA.
| └── raw/
|   └── credit_risk_dataset.csv		# Dataset original.
|
├── models/
│ └── modelo_credito.pkl		# Modelo treinado
|
├── notebooks/
│ └── 01_eda.ipynb			# Notebook EDA
│ └── 02_modeling.ipynb			# Notebook treinamento e metricas
|
|── src/
│ └── load_data.py			# Arquivo python para carregar datasets
| └── save_model.py			# Arquivo python para salvar modelo treinado
│
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md
```

---

## ⚙️ Como rodar o projeto

### 🔹 1. Clonar o repositório

```bash
git clone https://github.com/Joao-gui/ChatbotCredito
cd ChatbotCredito
```

### 🔹 2. Rodar com Docker

`docker compose up --build`

## 🌐 Acessos

- API: http://localhost:8000
- Backend (FastAPI): http://localhost:8000/docs
- Frontend (Streamlit): http://localhost:8501

## 📡 Endpoint principal

POST `/predict`

```
{
  "person_age": 30,
  "person_income": 50000,
  "person_home_ownership": "RENT",
  "person_emp_length": 5,
  "loan_intent": "PERSONAL",
  "loan_grade": "A",
  "loan_amnt": 10000,
  "loan_int_rate": 12.5,
  "loan_percent_income": 0.2,
  "cb_person_default_on_file": "N",
  "cb_person_cred_hist_length": 5
}
```

Exemplo de saída:

```
{
  "prediction": 0,
  "probability_default": 0.22
}
```

## 🛠️ Tecnologias utilizadas

* Python
* FastAPI
* Streamlit
* Scikit-learn
* Pandas
* Docker

## 👨‍💻 Autor

**João Guilherme Pellacani** - Engenheiro Elétrico com foco em Inteligência Artificial.

[LinkedIn](https://www.linkedin.com/in/joao-guilherme-pellacani/) | [GitHub](https://github.com/Joao-gui)

“A inteligência é o resultado de milhões de anos de evolução, que não podem ser computados em código binário” – **Miguel Nicolelis**
