import pandas as pd
import pickle
import streamlit as st

#Załadowanie modelu picklem
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

#Załadowanie nazw kolumn
with open('columns.pkl', 'rb') as f:
    columns = pickle.load(f)

# Set up the app layout
st.set_page_config(page_title='Pogromcy danych - Projekt ML - Ciucholand', page_icon=':ludzik:')
st.title('CIUCHOLAND')
st.header('Pogromcy danych - Projekt ML ')
st.header('')

# Define the left and right columns
col1, col2 = st.columns([1, 2])

# Add the PNG picture on the left column
with col1:
    st.image('appka.png')

with col2:
    st.subheader('Zaznacz zmienne:')
    #Okno z checkboxami
    form = st.form(key='my_form')
    selected_features = []
    for col in columns:
        selected = form.checkbox(col)
        selected_features.append(selected)
    submit_button = form.form_submit_button(label='Predykcja')

    #Liczenie predykcji po kliknięciu w guzik
    if submit_button:
        #Tworzymy dataframe do predykcji
        selected_features_dict = {}
        for i, col in enumerate(columns):
            selected_features_dict[col] = [1 if selected_features[i] else 0]
        selected_features_df = pd.DataFrame.from_dict(selected_features_dict)

        #Upewniamy się czy zgadzają się ilości kolumn
        missing_cols = set(columns) - set(selected_features_df.columns)
        for col in missing_cols:
            selected_features_df[col] = 0
        selected_features_df = selected_features_df[columns]

        #Predykcja
        prediction = model.predict(selected_features_df)

        #Pokazanie predykcji
        if prediction == 1:
            st.write('Klient zrobi zakupy w naszym sklepie.')
        else:
            st.write('Klient nie zrobi zakupów w naszym sklepie.')