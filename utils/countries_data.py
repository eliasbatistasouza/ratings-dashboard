import plotly.express as px

from utils import general_data


def group_avg(dataframe, avg, group, top):
    dataframe = dataframe.loc[:, [avg, group]].groupby(group).mean().sort_values(by=avg, ascending=False).round(2).reset_index().head(top)
    fig = px.bar(dataframe,x=group, y=avg, labels=general_data.LABELS, text_auto=True)
    return fig


def treemap(dataframe, countries):
    dataframe = (dataframe.loc[dataframe['country'].isin(countries), ['country','city', 'restaurant_id', 'aggregate_rating']]
                .groupby(['country','city'])
                .agg(restaurants=('restaurant_id', 'count'), 
                    rating=('aggregate_rating', 'mean'))
                .reset_index())
    
    fig = px.treemap(data_frame=dataframe, 
                    path=[px.Constant('World'),'country', 'city'], 
                    values='restaurants', 
                    color='rating', 
                    color_continuous_scale=['pink', 'white', 'lightblue', 'blue']
                    )
    
    return fig