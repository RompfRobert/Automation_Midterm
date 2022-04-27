import pandas as pd
from datetime import date, timedelta

today = date.today()
last_month = date.today()-timedelta(21)

def get_top_artists():
    df = pd.read_csv(f'artists({today})-({last_month}).csv')
    artists = df.loc[df['rank'] < 6].set_index('name')
    unsorted_artists = set(artists.index)
    sorted_artists = list(unsorted_artists)
    sorted_artists.sort()
    df2 = pd.DataFrame(index=sorted_artists)
    df2.index.name='Artists'
    df2['Average Ratings'] = ''
    df2.to_csv(f'top-artists({today})-({last_month}).csv')