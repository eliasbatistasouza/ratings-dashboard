import streamlit as st

from utils import general_data
from utils import cities_data


def main():
    st.set_page_config(page_title='Cities', layout='wide', page_icon='🏙️')

    df = general_data.read_data()
    
    general_data.sidebar()
    countries = general_data.country_filter(df, '002')
    low, high = general_data.rating_filter()
    range = general_data.cost_range(df)
    general_data.footer()

    st.markdown("<h1 style='color: #ff5252; text-align: center'>Cities Metrics</h1>", unsafe_allow_html=True)
    st.markdown('---')

    with st.container():
        col1, col2 = st.columns(2)

        with col1:
            st.markdown(f"<h3 style='text-align: center'>Top 5 Cities By Rating</h3>", unsafe_allow_html=True)
            fig = cities_data.cities_mean(df, countries)
            st.plotly_chart(fig, use_container_width=True, text_auto=True)

        with col2:
            st.markdown(f"<h3 style='text-align: center'>Top 5 Cities By Cuisines</h3>", unsafe_allow_html=True)
            fig = cities_data.cities_nunique(df, countries)
            st.plotly_chart(fig, use_container_width=True, text_auto=True)

        st.markdown('---')

    with st.container():
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown(f"<h3 style='text-align: center'>Top 5 Cities by {low}- Restaurants</h3>", unsafe_allow_html=True)
            fig = cities_data.btm_rating(df, countries, low)
            st.plotly_chart(fig, use_container_width=True, text_auto=True)

        with col2:
            st.markdown(f"<h3 style='text-align: center'>Top 5 Cities by {high}+ Restaurants</h3>", unsafe_allow_html=True)
            fig = cities_data.top_rating(df, countries, high)
            st.plotly_chart(fig, use_container_width=True, text_auto=True)

        st.markdown('---')

    with st.container():
            st.markdown("<h3 style='text-align: center'>Distribution of Cities</h3>", unsafe_allow_html=True)
            
            fig = cities_data.cities_dist(df, countries, range)
            
            st.plotly_chart(fig, use_container_width=True, text_auto=True)
            
    return None

if __name__ == '__main__':
    main()