import streamlit as st

from streamlit_extras.metric_cards import style_metric_cards

from utils import general_data
from utils import restaurant_data


def main():
    st.set_page_config(page_title='Restaurants', layout='wide', page_icon='🍴')

    df = general_data.read_data()

    general_data.sidebar()
    countries = general_data.country_filter(df, '003')
    general_data.footer()

    st.markdown("<h1 style='color: #ff5252; text-align: center'>Restaurants Metrics</h1>", unsafe_allow_html=True)
    st.markdown('---')

    with st.container():
        st.markdown("<h3 style='text-align: center'>Best Restaurants By Type of Cuisines</h3>",unsafe_allow_html=True)
        
        italian, american, arabian, japanese, brazilian = st.columns(5)
        
        with italian:
            
            cuisine, name, metric, country, city, avg_cost = restaurant_data.cuisines_rating(df, 'Italian')
            
            st.metric(
                label=f'{cuisine}: {name}', 
                value=f'{metric}/5.0', 
                help=f'''
                        Country: {country}\n
                        City: {city}\n
                        Average Cost For Two: {avg_cost}\n
                        ''')
            
        with american:

            cuisine, name, metric, country, city, avg_cost = restaurant_data.cuisines_rating(df, 'American')
            
            st.metric(
                label=f'{cuisine}: {name}', 
                value=f'{metric}/5.0', 
                help=f'''
                        Country: {country}\n
                        City: {city}\n
                        Average Cost For Two: {avg_cost}\n
                        ''')
            
        with arabian:
            
            cuisine, name, metric, country, city, avg_cost = restaurant_data.cuisines_rating(df, 'Arabian')
            
            st.metric(
                label=f'{cuisine}: {name}', 
                value=f'{metric}/5.0', 
                help=f'''
                        Country: {country}\n
                        City: {city}\n
                        Average Cost For Two: {avg_cost}\n
                        ''')
            
        with japanese:
            
            cuisine, name, metric, country, city, avg_cost = restaurant_data.cuisines_rating(df, 'Japanese')
            
            st.metric(
                label=f'{cuisine}: {name}', 
                value=f'{metric}/5.0', 
                help=f'''
                        Country: {country}\n
                        City: {city}\n
                        Average Cost For Two: {avg_cost}\n
                        ''')
            
        with brazilian:
            
            cuisine, name, metric, country, city, avg_cost = restaurant_data.cuisines_rating(df, 'Brazilian')
            
            st.metric(
                label=f'{cuisine}: {name}', 
                value=f'{metric}/5.0', 
                help=f'''
                        Country: {country}\n
                        City: {city}\n
                        Average Cost For Two: {avg_cost}\n
                        ''')
    
        st.markdown('---')
        
    style_metric_cards(background_color = '#1a1c24',  border_color='white', border_left_color='white')

    with st.container():
        st.markdown("<h3 style='text-align: center'>Top 10 Restaurants</h3>",unsafe_allow_html=True)
        
        dataframe = restaurant_data.top_restaurants(df, countries)
        
        st.dataframe(dataframe, use_container_width=True)
            
        st.markdown('---')
            
    with st.container():
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("<h3 style='text-align: center'>Type Price By Online Delivery</h3>",unsafe_allow_html=True)
            
            fig = restaurant_data.price_heatmap(df)
            
            st.plotly_chart(fig, use_container_width=True)
            
        with col2:
            st.markdown("<h3 style='text-align: center'>Restaurants By Price Type</h3>",unsafe_allow_html=True)
            
            fig = restaurant_data.price_pie(df, countries)
            
            st.plotly_chart(fig, use_container_width=True) 
        
        st.markdown('---')

    with st.container():
        st.markdown("<h3 style='text-align: center'>Top 10 Cuisines By Rating</h3>",unsafe_allow_html=True)
        
        fig = restaurant_data.top_cuisines(df, countries)
        
        st.plotly_chart(fig, use_container_width=True)
    
    return None
        
if __name__ == '__main__':
    main()
