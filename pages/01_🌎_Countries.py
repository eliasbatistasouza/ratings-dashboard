import streamlit as st

from utils import general_data
from utils import countries_data


def main():

    st.set_page_config(page_title='Countries', layout='wide', page_icon='🌎')

    df = general_data.read_data()

    general_data.sidebar()
    countries = general_data.country_filter(df, '001')
    general_data.footer()

    st.markdown("<h1 style='color: #ff5252; text-align: center'>Country Metrics</h1>", unsafe_allow_html=True)
    st.markdown('---')

    with st.container():
        st.markdown("<h3 style='text-align: center'>Number of Restaurants By City and Country</h3>",unsafe_allow_html=True)
        fig = countries_data.treemap(df, countries)
        st.plotly_chart(fig, use_container_width=True)
        
    st.markdown('---')

    with st.container():
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("<h3 style='text-align: center'>Top 5 Countries With Most Ratings</h3>",unsafe_allow_html=True)
            fig = countries_data.group_avg(df, 'votes', 'country', 5)
            st.plotly_chart(fig, use_container_width=True, text_auto=True)
        
        with col2:
            st.markdown("<h3 style='text-align: center'>Top 5 Countries by Average Rating</h3>",unsafe_allow_html=True)
            fig = countries_data.group_avg(df, 'aggregate_rating', 'country', 5)
            st.plotly_chart(fig, use_container_width=True)

    st.markdown('---')

    with st.container():
        st.markdown("<h3 style='text-align: center'>Top 10 Countries With Most Expensive Cost For Two</h3>",unsafe_allow_html=True)
        fig = countries_data.group_avg(df, 'average_cost_for_two', 'country', 10)
        st.plotly_chart(fig, use_container_width=True)
        
    return None

if __name__ == '__main__':
    main()