# Streamlit

import streamlit as st
import requests

st.title("Chatbot de Análise de Crédito")

st.write("Preencha os dados para avaliar risco de cŕedito")

# Inputs
person_age = st.number_input("Idade", 18, 100, 30)
person_income = st.number_input("Renda anual", 0, 1000000, 50000)

person_home_ownership = st.selectbox(
    "Tipo de moradia",
    ["RENT", "OWN", "MORTAGE", "OTHER"]
)

person_emp_lenght = st.number_input("Tempo de emprego (anos)", 0, 50, 5)

loan_intent = st.selectbox(
    "Motivo do empréstimo",
    ['PERSONAL', 'EDICATION', 'MEDICAL', 'VENTURE', 'HOMEIMPROVEMENT', 'DEBTCONSOLIDATION']
)

loan_grade = st.selectbox("Grade do empréstimo", list("ABCDEFG"))

loan_amnt = st.number_input('Valor do empréstimo', 500, 50000, 10000)
loan_int_rate = st.number_input('Valor de juros (%)', 5.0, 25.0, 12.5)
loan_percent_income = st.number_input('Percentual da renda', 0.0, 1.0, 0.2)

cb_person_default_on_file = st.selectbox('Já teve inadimplência?', ['Y', 'N'])
cb_person_cred_hist_length = st.number_input('Histórico de crédito (anos)', 1, 30, 5)

# Botão
if st.button('Analisar crédito'):

    data = {
        "person_age": person_age,
        "person_income": person_income,
        "person_home_ownership": person_home_ownership,
        "person_emp_length": person_emp_lenght,
        "loan_intent": loan_intent,
        "loan_grade": loan_grade,
        "loan_amnt": loan_amnt,
        "loan_int_rate": loan_int_rate,
        "loan_percent_income": loan_percent_income,
        "cb_person_default_on_file": cb_person_default_on_file,
        "cb_person_cred_hist_length": cb_person_cred_hist_length
    }

    response = requests.post("http:api:8000/predict", json=data)

    if response.status_code == 200:
        result = response.json()

        st.subheader("Resultado:")

        if result['prediction'] == 1:
            st.error(f"Alto risco de inadimplência ({result['probability_default']:.2f})")
        else:
            st.success(f"Baixo risco ({result['probability_default']:.2f})")

    else:
        st.error("Error ao conectar com a API")