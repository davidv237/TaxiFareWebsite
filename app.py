import streamlit as st
import requests
import datetime

'''
# TaxiFareModel front-end
'''

st.markdown('''
Ein Modell zum Vorhersagen, des Preises einer Taxifahrt in New York auf Basis des Datums, der Koordinaten und der Anzahl der Passagiere.
''')

'''
## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

1. Let's ask for:
- date and time
- pickup longitude
- pickup latitude
- dropoff longitude
- dropoff latitude
- passenger count
'''

start_time = st.slider("When do you start?",value=datetime(2021, 3, 2, 9, 30),format="MM/DD/YY - hh:mm:ss UTC")
st.write("Start time:", start_time)
pickup_longitude = st.text_input('longitude', '-73.950655')
st.write('Start Longitude ist:', pickup_longitude)
pickup_latitude = st.text_input('pickup_latitude', '40.783282')
st.write('Start Latitude:', pickup_latitude)
dropoff_longitude = st.text_input('dropoff_longitude', '-73.984365')
st.write('Dropoff Longitude :', dropoff_longitude)
dropoff_latitude = st.text_input('dropoff_latitude', '40.769802')
st.write('Dropoff Latitude:', dropoff_latitude)
passenger_count = st.text_input('Passagiere', '1')
st.write('Anzahl der Passagiere:', passenger_count)

'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''

'''

2. Let's build a dictionary containing the parameters for our API...

'''

params = {
            "key": '0',
            "pickup_datetime": str(start_time) + 'UTC',
            "pickup_longitude": float(pickup_longitude),
            "pickup_latitude": float(pickup_latitude),
            "dropoff_longitude": float(dropoff_longitude),
            "dropoff_latitude": float(dropoff_latitude),
            "passenger_count": float(passenger_count)
             }

params
'''
3. Let's call our API using the `requests` package...
'''

url = 'https://lewagondavidvenzke-vkbio62pmq-ew.a.run.app/predict_fare'
r = requests.get(url, params=params)

'''

4. Let's retrieve the prediction from the **JSON** returned by the API...


'''
r = r.json()
r
prediction = r['prediction']


'''
## Finally, we can display the prediction to the user
'''
f"Der Preis der Taxifahrt beträgt voraussichtlich: {round(prediction)} USD"


