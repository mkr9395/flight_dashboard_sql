import streamlit as st 

# left hand sidebar
st.sidebar.title('Flights Analytics')

# adding drop-down

user_option = st.sidebar.selectbox('Menu',['Select One','Check Flights','Analytics'])

if user_option == 'Check Flights':
    st.title('Check Flights')
elif user_option == 'Analytics':
    st.title('Analytics')
else:
    st.title('tell about the project')