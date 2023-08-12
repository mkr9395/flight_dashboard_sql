import streamlit as st 
from dbhelper import DB

import plotly.graph_objects as go
import plotly.express as px



db = DB()

# left hand sidebar
st.sidebar.title('Flights Analytics')

# adding drop-down

user_option = st.sidebar.selectbox('Menu',['Select One','Check Flights','Analytics'])

if user_option == 'Check Flights':
    st.title('Check Flights')
    
    # check boxes
    col1,col2 = st.columns(2)
    
    # fetching names of city
    city = db.fetch_city_names()
    
    # creating first dropdown for source
    with col1:
        source_city = st.selectbox('Source city',sorted(city))
    
     # creating second dropdown for destination   
    with col2:
        destination_city = st.selectbox('Destination city',sorted(city))
        
    # creating button to search
    if st.button('Search'):
        results = db.fetch_all_flights(source_city,destination_city)
        # displaying all results as dataframe
        st.dataframe(results)  
    
elif user_option == 'Analytics':
    st.title('Analytics')
    
    # fetching airline name and frequency
    airline,frequency = db.fetch_airline_frequency()
    
    #pie-chart for airline frquency
    fig = go.Figure(
        go.Pie(
            labels = airline,
            values = frequency,
            hoverinfo = 'label + percent',
            textinfo = 'value'
        ))
    
    st.header("Pie chart")
    st.plotly_chart(fig)
    
    # fetching city name and frequency of flights
    city_name,freq = db.busy_airport()
    
    # bar-graph for airline freq per city using plotly.express
    st.header("Bar chart")
    fig = px.bar(
        x = city_name,
        y = freq
        )
    
    # Customize the layout with titles and labels
    fig.update_layout(
        title="Frequency of Flights per City",
        xaxis_title="City",
        yaxis_title="Frequency")
    
    st.plotly_chart(fig, theme='streamlit',use_container_width=True)
   
    

else:
    st.title('tell about the project')