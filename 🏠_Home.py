import streamlit as st
import folium
from streamlit_folium import folium_static
from folium.plugins import MarkerCluster

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
        m = folium.Map()
        marker_cluster = MarkerCluster().add_to(m)
    
        for _, line in df.iterrows():
    
            name = line['restaurant_name']
            price_for_two = line['average_cost_for_two']
            cuisine = line['cuisines']
            rating = line['aggregate_rating']
            color = f"{line['color_name']}"
    
            html = '<p><strong>{}</strong></p>'
            html += '<p>Price: {:.} ($) for two'.replace(".", ",")
            html += '<br/>Type: {}'
            html += '<br/>Rating: {}/5.0'
            html = html.format(name, price_for_two, cuisine, rating)
    
            popup = folium.Popup(
                folium.Html(html, script=True),
                max_width=500,
            )
    
            folium.Marker(
                [line['latitude'], line['longitude']],
                popup=popup,
                icon=folium.Icon(color=color, icon='home', prefix='fa'),
            ).add_to(marker_cluster)
    
        folium_static(m, width=1024, height=600)
    return None

if __name__ == '__main__':
    main()
