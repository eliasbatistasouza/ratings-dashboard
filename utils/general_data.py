import pandas as pd
import streamlit as st

from streamlit_extras.app_logo import add_logo
from streamlit_extras.mention import mention

DATA_RAW_PATH = f'./data/raw/zomato.csv'
PROCESSED_DATA_PATH = f'./data/processed/data.csv'

COUNTRIES = {
    1: "India",
    14: "Australia",
    30: "Brazil",
    37: "Canada",
    94: "Indonesia",
    148: "New Zeland",
    162: "Philippines",
    166: "Qatar",
    184: "Singapure",
    189: "South Africa",
    191: "Sri Lanka",
    208: "Turkey",
    214: "United Arab Emirates",
    215: "England",
    216: "United States of America",
}

COLORS = {
    "3F7E00": "darkgreen",
    "5BA829": "green",
    "9ACD32": "lightgreen",
    "CDD614": "orange",
    "FFBA00": "red",
    "CBCBC8": "darkred",
    "FF7800": "darkred",
}

CURRENCY = {
    'Botswana Pula(P)': 0.076,
    'Brazilian Real(R$)': 0.19,
    'Dollar($)': 1,
    'Emirati Diram(AED)': 0.27,
    'Indian Rupees(Rs.)': 0.012,
    'Indonesian Rupiah(IDR)': 0.000065,
    'NewZealand($)': 0.61,
    'Pounds(£)': 1.20,
    'Qatari Rial(QR)': 0.27,
    'Rand(R)': 0.055,
    'Sri Lankan Rupee(LKR)': 0.0031,
    'Turkish Lira(TL)': 0.059
}

LABELS = {
    'average_cost_for_two': 'Average Cost For Two',
    'aggregate_rating': 'Average Rating', 
    'city': 'City', 
    'country': 'Country', 
    'cuisines': 'Cuisines',
    'has_online_delivery': 'Has Online Delivery',
    'price_type': 'Price Type', 
    'restaurant_id': 'Number of Restaurants',
}

PRICES = ['Cheap', 'Normal', 'Expensive', 'Gourmet']

PRICE_ORDER = {'price_type': ['cheap', 'normal', 'expensive', 'gourmet'] }


def clean_dataframe(path: str = DATA_RAW_PATH) -> pd.DataFrame:

    dataframe = pd.read_csv(path)
    dataframe = dataframe.dropna()
    
    dataframe = dataframe.drop_duplicates()
    dataframe = dataframe.drop(['Switch to order menu'], axis=1)
    
    cols = list(dataframe.columns)
    new_cols = []

    for col in cols:
        col = col.lower()
        col = col.replace(" ","_")
        new_cols.append(col)
        
    dataframe.columns = new_cols
    
    dataframe['color_name'] = dataframe['rating_color'].apply(lambda x: COLORS[x])
    dataframe['country'] = dataframe['country_code'].apply(lambda x: COUNTRIES[x])
    
    prices = list(dataframe['price_range'])
    new_prices = []

    for price in prices:
        if price == 1:
            new_prices.append('cheap')
        elif price == 2:
            new_prices.append('normal')
        elif price == 3:
            new_prices.append('expensive')
        else:
            new_prices.append('gourmet')

    dataframe['price_type'] = new_prices
    
    dataframe['cuisines'] = dataframe.loc[:,'cuisines'].apply(lambda x: x.split(',')[0])
    

    dataframe['average_cost_for_two'] = dataframe['average_cost_for_two']*dataframe['currency'].map(CURRENCY)
    dataframe.drop(columns='currency', inplace=True)
    
    lines = (dataframe['average_cost_for_two']>=2) & (dataframe['average_cost_for_two']<50000)
    dataframe = dataframe.loc[lines,:]
    
    dataframe.to_csv(PROCESSED_DATA_PATH, index=False)
    
    return None


def read_data(path = PROCESSED_DATA_PATH):
    dataframe = pd.read_csv(path)

    return dataframe


def sidebar() -> None:
    image_path = 'img/logo.png'
    add_logo(image_path, height=75)
    
    return None


def download():
    with st.sidebar:
        st.markdown("<h3>Database:</h3>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: justify'>This dashboard was developed using a public database from Zomato App.<p/><p> You can get the original database here:<p/>", unsafe_allow_html=True)
        with open(DATA_RAW_PATH, 'rb') as file:
        
            st.download_button(label='Download',data=file, file_name='zomato.csv', mime='text/csv' )
        st.markdown('---')
    
    return None


def country_filter(dataframe, key):
    countries = st.sidebar.multiselect(label='Which Countries?', options=dataframe.loc[:,'country'].unique().tolist(), default=dataframe.loc[:,'country'].unique().tolist(), key=key)
    st.sidebar.markdown('''---''')

    return list(countries)


def top_n(dataframe, default):
    max = int(dataframe['country'].nunique())
    top_n = st.sidebar.slider(label='Top?', min_value=1, max_value=max, value=default, step=1)
    st.sidebar.markdown('---')
    
    return top_n


def rating_filter():
    rating = st.sidebar.slider(label='Rating', min_value=0.0, max_value=5.0, value=(2.0,4.0))
    st.sidebar.markdown('---')
    
    return rating


def cost_range(dataframe):
    max = dataframe.loc[:,['city', 'average_cost_for_two']].groupby(['city']).mean().sort_values(by='average_cost_for_two', ascending=False).reset_index()
    max = int(max.iloc[0,1]) + 15
    range = st.sidebar.slider(label='Cost Range', min_value=0, max_value=max, value=100)
    st.sidebar.markdown('---')
        
    return range 


def footer():
    with st.sidebar:
        st.sidebar.markdown("<h3>Find Me:</h3>", unsafe_allow_html=True)
        mention(label='eliasbatista', icon='twitter', url='https://www.twitter.com/eliasbatista')
        mention(label='eliasbatistasouza', icon='github', url='https://github.com/eliasbatistasouza')
        mention(label='eliasbatista.com', icon='🌐', url='https://eliasbatista.com')

    return None