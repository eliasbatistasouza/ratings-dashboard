import streamlit as st
import folium
from streamlit_folium import st_folium
from folium.plugins import MarkerCluster


def unique_numbers(dataframe, column) -> int:
    metric = dataframe.loc[:,column].nunique()
    
    return metric


def create_map(dataframe):
    
    f = folium.Figure(width=1920, height=1080)

    m = folium.Map(max_bounds=True).add_to(f)

    marker_cluster = MarkerCluster().add_to(m)

    for _, line in dataframe.iterrows():

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

    st_folium(m, width=1024, height=600, returned_objects=[])
    
    return None