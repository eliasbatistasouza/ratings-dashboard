import streamlit as st

from utils import general_data
from utils import home_data

def main():
    
    st.set_page_config(page_title='Home', layout='wide', page_icon='🏠')

    general_data.clean_dataframe()
    df = general_data.read_data()

    general_data.sidebar()
    general_data.download()
    general_data.footer()

    st.markdown("<h1 style='color: #ff5252; text-align: center'>Zomato Dashboard</h1>", unsafe_allow_html=True)
    st.markdown("<h6 style='text-align: justify'>This dashboard presents important business metrics from the Zomato App, this metrics will help you with decision making and are separated by, Overall Metrics, Countries Metrics, Cities Metrics and Restaurant Metrics. Here you can have a broad view of all the goals reached by the company.<h6>", unsafe_allow_html=True)
    st.markdown('---')

    with st.container():
        st.markdown("<h3 style='text-align: center'>Overall Metrics</h3>", unsafe_allow_html=True)
        col1, col2, col3, col4, col5 = st.columns(5)
        
        with col1:
            metric = home_data.unique_numbers(df, 'restaurant_id')
            st.metric(label='Number of Restaurants', value=f"{metric:,}".replace(",", "."))
        
        with col2:
            metric = home_data.unique_numbers(df, 'country')
            st.metric(label='Number of Countries', value=metric)
            
        with col3:
            metric = home_data.unique_numbers(df, 'city')
            st.metric(label='Number of Cities', value=metric)
            
        with col4:
            metric = df['votes'].sum()
            st.metric(label='Number of Ratings', value=f"{metric:,}".replace(",", "."))
            
        with col5:
            metric = home_data.unique_numbers(df, 'cuisines')
            st.metric(label='Number of Cuisines', value=metric)
        
    st.markdown('---')
    
    with st.container():
        home_data.create_map(df)
    return None

if __name__ == '__main__':
    main()
