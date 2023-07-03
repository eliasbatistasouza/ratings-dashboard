import pandas as pd
import plotly.express as px

from utils import general_data

def cuisines_rating(dataframe, cuisine):
    dataframe = (dataframe.loc[dataframe['cuisines'] == cuisine, 
                        ['restaurant_name', 'restaurant_id', 'aggregate_rating', 'average_cost_for_two', 'city', 'country']]
                .sort_values(by=['aggregate_rating', 'restaurant_id'], ascending=[False, True]))
    
    metric = dataframe['aggregate_rating'].iloc[0]
    name = dataframe['restaurant_name'].iloc[0]
    country = dataframe['country'].iloc[0]
    city = dataframe['city'].iloc[0]
    avg_cost = dataframe['average_cost_for_two'].iloc[0]
    
    return cuisine, name, metric, country, city, avg_cost


def top_restaurants(dataframe, countries):
    
    dataframe = (dataframe.loc[dataframe['country'].isin(countries),['restaurant_id', 'restaurant_name', 'country', 'city', 
                        'average_cost_for_two', 'price_type', 'aggregate_rating', 'votes']]
                .sort_values(by=['aggregate_rating', 'restaurant_id'], ascending=[False, True])
                .head(10))
    dataframe = dataframe.loc[:,['restaurant_name', 'country', 'city', 'average_cost_for_two', 
                                'price_type', 'aggregate_rating', 'votes']]
    
    return dataframe

def price_heatmap(dataframe):
    
    dataframe = (dataframe.loc[:,['price_type', 'has_online_delivery', 'restaurant_id']]
                .groupby(['price_type', 'has_online_delivery'])
                .count()
                .reset_index())
    dataframe = dataframe.pivot(index='price_type', columns='has_online_delivery')['restaurant_id']
    
    fig = px.imshow(dataframe, x=['No', 'Yes'], y=general_data.PRICES, text_auto=True, labels=dict(x='Has Online Delivery', y='Price Type', color='Number of Restaurants'), aspect='auto')

    return fig

def price_pie(dataframe, countries):
    dataframe = (dataframe.loc[dataframe['country'].isin(countries), ['restaurant_id', 'price_type']]
                    .groupby(['price_type'])
                    .count()
                    .reset_index())
        
    fig = px.pie(dataframe, values='restaurant_id', names='price_type', category_orders=general_data.PRICE_ORDER, labels=general_data.LABELS)
    
    return fig

def top_cuisines(dataframe, countries):
    
    dataframe = (dataframe.loc[dataframe['country'].isin(countries),['cuisines', 'aggregate_rating']]
                .groupby(['cuisines'])
                .mean()
                .sort_values(by='aggregate_rating', ascending=False)
                .reset_index()
                .round(2)
                .head(10))
    
    fig = px.bar(data_frame=dataframe, x='cuisines', y='aggregate_rating', text_auto=True, labels=general_data.LABELS)
    
    return fig