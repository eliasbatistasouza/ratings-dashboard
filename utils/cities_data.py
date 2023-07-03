import plotly.express as px


def cities_mean(dataframe, countries):
    dataframe = (dataframe.loc[dataframe['country'].isin(countries), ['country', 'city', 'aggregate_rating']]
                .groupby(['city', 'country'])
                .mean()
                .round(2)
                .sort_values(by='aggregate_rating', ascending=False)
                .reset_index()
                .head(5))
    
    fig = px.bar(dataframe,
                x='city',
                y='aggregate_rating',
                color='country',
                text_auto=True,
                labels={
                    'aggregate_rating': 'Average Rating',
                    'city': 'City',
                    'country': 'Country',
                    'cuisines': 'Cuisines',
                    'restaurant_id': 'Number of Restaurants'
                    })
    fig = fig.update_layout(xaxis={'categoryorder': 'total descending'})
    
    return fig


def cities_nunique(dataframe, countries):
    dataframe = (dataframe.loc[dataframe['country'].isin(countries), ['cuisines', 'country', 'city']]
                .groupby(['country', 'city'])
                .nunique()
                .round(2)
                .sort_values(by='cuisines', ascending=False)
                .reset_index()
                .head(5))
    fig = px.bar(dataframe,
                x='city',
                y='cuisines',
                color='country',
                text_auto=True,
                labels={
                    'aggregate_rating': 'Average Rating',
                    'city': 'City',
                    'country': 'Country',
                    'cuisines': 'Cuisines',
                    'restaurant_id': 'Number of Restaurants'
                    })
    fig = fig.update_layout(xaxis={'categoryorder': 'total descending'})
    
    
    return fig


def top_rating(dataframe, countries, high):
    
    dataframe = (dataframe.loc[(dataframe['aggregate_rating'] > high) & (dataframe['country'].isin(countries)), ['country', 'city', 'restaurant_id']]
                .groupby(['country', 'city'])
                .count()
                .round(2)
                .sort_values(by='restaurant_id', ascending=False)
                .reset_index()
                .head(5))
    fig = px.bar(dataframe,
                x='city',
                y='restaurant_id',
                color='country',
                text_auto=True,
                labels={
                    'aggregate_rating': 'Average Rating',
                    'city': 'City',
                    'country': 'Country',
                    'cuisines': 'Cuisines',
                    'restaurant_id': 'Number of Restaurants'
                    })
    fig = fig.update_layout(xaxis={'categoryorder': 'total descending'})
    
    return fig


def btm_rating(dataframe, countries, low):
    
    dataframe = (dataframe.loc[(dataframe['aggregate_rating'] < low) & (dataframe['country'].isin(countries)), ['country', 'city', 'restaurant_id']]
                    .groupby(['country', 'city'])
                    .count()
                    .round(2)
                    .sort_values(by='restaurant_id', ascending=False)
                    .reset_index()
                    .head(5))
        
    fig = px.bar(dataframe, 
                    x='city', 
                    y='restaurant_id', 
                    color='country', 
                    text_auto=True, 
                    labels={
                        'aggregate_rating': 'Average Rating', 
                        'city': 'City', 
                        'country': 'Country', 
                        'cuisines': 'Cuisines', 
                        'restaurant_id': 'Number of Restaurants'
                        })
    fig = fig.update_layout(xaxis={'categoryorder': 'total descending'})
    
    return fig


def cities_dist(dataframe, countries, range):
    
    dataframe = (dataframe.loc[dataframe['country'].isin(countries), ['restaurant_id', 'country', 'city', 'aggregate_rating', 'average_cost_for_two']]
                .groupby(['country', 'city'])
                .agg(restaurant_id=('restaurant_id', 'count'), 
                    aggregate_rating=('aggregate_rating', 'mean'), 
                    average_cost_for_two=('average_cost_for_two', 'mean'))
                .reset_index())
    fig = px.scatter(data_frame=dataframe, 
                    x='average_cost_for_two', 
                    y='aggregate_rating', 
                    size='restaurant_id',
                    color='country',
                    labels={
                        'average_cost_for_two': 'Average Cost For Two',
                        'aggregate_rating': 'Average Rating', 
                        'city': 'City', 
                        'country': 'Country', 
                        'cuisines': 'Cuisines', 
                        'restaurant_id': 'Number of Restaurants'
                        },
                    hover_data=['country', 'city', 'aggregate_rating', 'average_cost_for_two'],
                    range_x=[0,range])
    
    return fig