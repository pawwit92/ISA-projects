import pandas as pd
import streamlit as st
from scipy.stats import norm


#Ładowanie danych
df = pd.read_csv('covid_curr.csv')

#Nagłówek
st.header("COVID-19 - Kalkulator prawdopodobieństwa")
st.header("Czy pacjent wyzdrowieje?")
#st.image("https://upload.wikimedia.org/wikipedia/commons/8/82/SARS-CoV-2_without_background.png", width=200)
st.image("https://media.tenor.com/jDu5DVTyQLcAAAAM/pepe-peppo.gif", width=200)
st.header(" ")

container = st.container()

#Kontenery z wyborem informacji
container.subheader('Charakterystyka pacjenta')
sex_type = container.selectbox('Płeć', df['SEX_TYPE'].unique())
age_range = container.selectbox('Przedział wiekowy', sorted(df['AGE_RANGE'].unique()))
container.subheader('Choroby współistniejące')
pneumonia = container.selectbox('Zapalenie płuc', sorted(df['PNEUMONIA'].unique()))
diabetes = container.selectbox('Cukrzyca', sorted(df['DIABETES'].unique()))
hipertension = container.selectbox('Nadciśnienie', sorted(df['HIPERTENSION'].unique()))
container.subheader('Pozostałe')
intubed = container.selectbox('Pacjent intubowany', sorted(df['INTUBED'].unique()))

#Ustawienie przycisku
form = st.form(key='my_form')
submit_button = form.form_submit_button(label='Oblicz')

#Filtrowanie danych na podstawie wyboru użytkownika
filtered_df = df.query("SEX_TYPE == @sex_type and AGE_RANGE == @age_range and PNEUMONIA == @pneumonia and DIABETES == @diabetes and HIPERTENSION == @hipertension and INTUBED == @intubed")

#Obliczanie prawdopodobieństwa
num_deaths = filtered_df['DEATH'].sum()
num_patients = len(filtered_df)
prob_death = num_deaths / num_patients
prob_survive = (1-prob_death)*100

#Wyświetlanie wyników
st.write(" ")
st.write(" ")
# st.write(f"Number of patients: {num_patients}")
# st.write(f"Number of deaths: {num_deaths}")
#st.write(f"Pacjet ma {prob_survive:.2f}% na wyzdrowienie")

if submit_button:
    st.success(f"Prawdopodobieństwo że pacjent wyzdrowieje wynosi {prob_survive:.2f}%")