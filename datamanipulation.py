import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

st.set_page_config(page_title='data visualization for top rated movies',layout='wide')
st.title('data visualization')
data=pd.read_csv('C:/Users/elkha/OneDrive/Desktop/DSM_project/CleanData.csv')


t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,t11,t12,t13=st.tabs(['barblot for production_companies and it\'s count'
                                                ,'barblot for actors and it\'s count'
                                                ,'barplot for production companies and it\'s budget'
                                                ,'barblot for cast and revenue'
                                                ,'barblot for cast and thier vote_average'
                                                ,'barblot for production_countries and budget'
                                                ,'barblot for genre and revenue'
                                                ,'barblot for directors and revenue most director earned the most'
                                                ,'scatterplot for vote_count and vote_average'
                                                ,'scatterplot for runtime and vote_average'
                                                ,'histplot for genres'
                                                ,'histplot for year and count of films'
                                                ,'scatterplot for budget and revenue'])

# barblot for production_companies till us about how many it appears at the best 1000 movie

# e=data[['production_companies','title']]
# e['production_companies']=e['production_companies'].str.split(', ')
# d=e.explode('production_companies')
# ds=d.groupby('production_companies')['title'].count()
# ds=ds.to_frame().reset_index()
# ds.columns=['production_companies','title']
# ds=ds.sort_values('title',ascending=False).head(10)
# sns.barplot(data=ds,x='production_companies',y='title')


with t1:
    st.header('till us about how many it appears at the best 1000 movie')
    e=data[['production_companies','title']]
    e['production_companies']=e['production_companies'].str.split(', ')
    d=e.explode('production_companies')
    ds=d.groupby('production_companies')['title'].count()
    ds=ds.to_frame().reset_index()
    ds.columns=['production_companies','title']
    ds=ds.sort_values('title',ascending=False).head(10)
    
    fig1,ax1=plt.subplots(figsize=(10,5))
    sns.barplot(data=ds,x='production_companies',y='title',ax=ax1,palette='viridis')
    ax1.set_xticklabels(ax1.get_xticklabels(), rotation=45, ha='right')
    st.pyplot(fig1)
# barblot for actors till us about how many they appears at the best 1000 movie

# e=data[['cast','title']]
# e['cast']=e['cast'].str.split(', ')
# d=e.explode('cast')
# ds=d.groupby('cast')['title'].count()
# ds=ds.to_frame().reset_index()
# ds.columns=['cast','title']
# ds=ds.sort_values('title',ascending=False).head(10)
# sns.barplot(data=ds,x='cast',y='title')

with t2:
    st.header('till us about how many they appears at the best 1000 movie')
    e=data[['cast','title']]
    e['cast']=e['cast'].str.split(', ')
    d=e.explode('cast')
    ds=d.groupby('cast')['title'].count()
    ds=ds.to_frame().reset_index()
    ds.columns=['cast','title']
    ds=ds.sort_values('title',ascending=False).head(10)
    
    fig2,ax2=plt.subplots(figsize=(10,5))
    sns.barplot(data=ds,x='cast',y='title',ax=ax2,palette='mako')
    ax2.set_xticklabels(ax2.get_xticklabels(), rotation=45, ha='right')
    st.pyplot(fig2)

# barplot for production companies and it's budget tell us about how much companies pay for produce a good movies

    # e=data
    # e['production_companies']=e['production_companies'].str.split(', ')
    # d=e.explode('production_companies')
    # ds=d.groupby('production_companies')['budget'].mean()
    # ds=ds.to_frame().reset_index()
    # ds.columns=['production_companies','budget']
    # sns.barplot(data=ds,x='production_companies',y='budget')


with t3:
    st.header('tell us about how much companies pay for produce a good movies')
    e=data
    e['production_companies']=e['production_companies'].str.split(', ')
    d=e.explode('production_companies')
    ds=d.groupby('production_companies')['budget'].mean()
    ds=ds.to_frame().reset_index()
    ds.columns=['production_companies','budget']
    ds=ds.sort_values('budget',ascending=False).head(10)
    fig3,ax3=plt.subplots(figsize=(10,5))
    sns.barplot(data=ds,x='production_companies',y='budget',ax=ax3,palette='rocket')
    ax3.set_xticklabels(ax3.get_xticklabels(), rotation=45, ha='right')
    st.pyplot(fig3)

# barblot for cast and revenue tell us the mean amount of money the actor films got

    # e=data
    # e['cast']=e['cast'].str.split(', ')
    # d=e.explode('cast')
    # ds=d.groupby('cast')['revenue'].mean()
    # ds=ds.to_frame().reset_index()
    # ds.columns=['cast','revenue']
    # ds=ds.sort_values('revenue',ascending=False).head(10)
# sns.barplot(data=ds,x='cast',y='revenue')


with t4:
    st.header('tell us the mean amount of money the actor films got')
    e=data
    e['cast']=e['cast'].str.split(', ')
    d=e.explode('cast')
    ds=d.groupby('cast')['revenue'].mean()
    ds=ds.to_frame().reset_index()
    ds.columns=['cast','revenue']
    ds=ds.sort_values('revenue',ascending=False).head(10)
    
    fig4,ax4=plt.subplots(figsize=(10,5))
    sns.barplot(data=ds,x='cast',y='revenue',ax=ax4,palette='magma')
    ax4.set_xticklabels(ax4.get_xticklabels(), rotation=45, ha='right')
    st.pyplot(fig4)

# barblot for cast and thier vote_average tell us the mean of vote for each actor

# e=data
# e['cast']=e['cast'].str.split(', ')
# d=e.explode('cast')
# ds=d.groupby('cast')['vote_average'].mean()
# ds=ds.to_frame().reset_index()
# ds.columns=['cast','vote_average']
# ds=ds.sort_values('vote_average',ascending=False).head(10)
# sns.barplot(data=ds,x='cast',y='vote_average')

with t5:
    st.header('tell us the mean of votes for each actor')
    e=data
    d=e.explode('cast')
    ds=d.groupby('cast')['vote_average'].mean()
    ds=ds.to_frame().reset_index()
    ds.columns=['cast','vote_average']
    ds=ds.sort_values('vote_average',ascending=False).head(10)
    
    fig5,ax5=plt.subplots(figsize=(10,5))
    sns.lineplot(data=ds,x='cast',y='vote_average',ax=ax5,color='crimson',marker='o')
    ax5.set_xticklabels(ax5.get_xticklabels(), rotation=45, ha='right')
    st.pyplot(fig5)

# barblot for production_countries and budget tell us about the countries that heavily fund films

# e=data
# e['production_countries']=e['production_countries'].str.split(', ')
# d=e.explode('production_countries')
# ds=d.groupby('production_countries')['budget'].sum()
# ds=ds.to_frame().reset_index()
# ds.columns=['production_countries','budget']
# ds=ds.sort_values('budget',ascending=False).head(10)
# sns.barplot(data=ds,x='production_countries',y='budget')

with t6:
    st.header('tell us about the countries that heavily fund films')
    e=data
    e['production_countries']=e['production_countries'].str.split(', ')
    d=e.explode('production_countries')
    ds=d.groupby('production_countries')['budget'].sum()
    ds=ds.to_frame().reset_index()
    ds.columns=['production_countries','budget']
    ds=ds.sort_values('budget',ascending=False).head(10)
    
    fig6,ax6=plt.subplots(figsize=(10,5))
    sns.barplot(data=ds,x='production_countries',y='budget',ax=ax6,palette='Blues_d')
    ax6.set_xticklabels(ax6.get_xticklabels(), rotation=45, ha='right')
    st.pyplot(fig6)

# barblot for genre and revenue most genre earned the most

# e=data
# e['genres']=e['genres'].str.split(', ')
# d=e.explode('genres')
# ds=d.groupby('genres')['revenue'].mean()
# ds=ds.to_frame().reset_index()
# ds.columns=['genres','revenue']
# ds=ds.sort_values('revenue',ascending=False).head(10)
# sns.barplot(data=ds,x='genres',y='revenue')

with t7:
    st.header('tell us about genres earned the most')
    e=data
    e['genres']=e['genres'].str.split(', ')
    d=e.explode('genres')
    ds=d.groupby('genres')['revenue'].mean()
    ds=ds.to_frame().reset_index()
    ds.columns=['genres','revenue']
    ds=ds.sort_values('revenue',ascending=False).head(10)
    
    fig7,ax7=plt.subplots(figsize=(10,5))
    sns.barplot(data=ds,x='genres',y='revenue',ax=ax7,palette='Greens_d')
    ax7.set_xticklabels(ax7.get_xticklabels(), rotation=45, ha='right')
    st.pyplot(fig7)

# barblot for directors and revenue most director earned the most

# e=data
# e['directors']=e['directors'].str.split(', ')
# d=e.explode('directors')
# ds=d.groupby('directors')['revenue'].mean()
# ds=ds.to_frame().reset_index()
# ds.columns=['directors','revenue']
# ds=ds.sort_values('revenue',ascending=False).head(10)
# sns.barplot(data=ds,x='directors',y='revenue')

with t8:
    st.header('tell us about directors earned the most')
    e=data
    e['directors']=e['directors'].str.split(', ')
    d=e.explode('directors')
    ds=d.groupby('directors')['revenue'].mean()
    ds=ds.to_frame().reset_index()
    ds.columns=['directors','revenue']
    ds=ds.sort_values('revenue',ascending=False).head(10)
    
    fig8,ax8=plt.subplots(figsize=(10,5))
    sns.barplot(data=ds,x='directors',y='revenue',ax=ax8,palette='icefire')
    ax8.set_xticklabels(ax8.get_xticklabels(), rotation=45, ha='right')
    st.pyplot(fig8)

# scatterplot for vote_count and vote_average to tell us about (is high amount of voters mean high vote)

# e=data[['vote_count','vote_average']]
# ds=e.sort_values('vote_count',ascending=False).head(100)
# sns.scatterplot(data=ds,x='vote_count',y='vote_average')

with t9:
    st.header('tell us about (is high amount of voters mean high vote?)')
    e=data[['vote_count','vote_average']]
    ds=e.sort_values('vote_count',ascending=False).head(100)
    
    fig9,ax9=plt.subplots(figsize=(10,5))
    sns.scatterplot(data=ds,x='vote_count',y='vote_average',ax=ax9)
    ax9.set_xticklabels(ax9.get_xticklabels(), rotation=45, ha='right')
    st.pyplot(fig9)

# scatterplot for runtime and vote_average to tell us(is there a relation between runtime and vote_average)

# e=data[['runtime','vote_average']]
# ds=data.sort_values('runtime',ascending=False).head(100)
# sns.scatterplot(data=ds,x='runtime',y='vote_average')

with t10:
    st.header('tell us(is there a relation between runtime and vote_average?)')
    e=data[['runtime','vote_average']]
    ds=data.sort_values('runtime',ascending=False).head(100)
    fig8,ax8=plt.subplots(figsize=(10,5))
    sns.scatterplot(data=ds,x='runtime',y='vote_average',ax=ax8)
    ax8.set_xticklabels(ax8.get_xticklabels(), rotation=45, ha='right')
    st.pyplot(fig8)

# histplot for genres tell us about most genres exist at top 1000 movie

# e=data
# e['genres']=e['genres'].str.split(', ')
# d=e.explode('genres')
# d=d.head(200)
# sns.histplot(data=d,x='genres')

with t11:
    st.header('tell us about most genres exist at top 200 movie')
    e1=data.copy()

    d=e1.explode('genres')
    d['genres'] = d['genres'].str.strip()
    d = d[d['genres'] != ''] 
    d=d.head(200)
    
    fig11,ax11=plt.subplots(figsize=(10,5))
    sns.histplot(data=d,x='genres',ax=ax11,kde=True,color='teal')
    ax11.set_xticklabels(ax11.get_xticklabels(), rotation=45, ha='right')
    st.pyplot(fig11)

# histplot for year and count of films tell us about (is the amount of goof movies increase by time)

# e=data
# e['release_date']=pd.to_datetime(e['release_date']).dt.year
# sns.histplot(data=e,x='release_date')

with t12:
    st.header('ttell us about (is the amount of goof movies increase by time)')
    e=data
    e['release_date']=pd.to_datetime(e['release_date']).dt.year
    
    fig12,ax12=plt.subplots(figsize=(10,5))
    sns.histplot(data=e,x='release_date',ax=ax12,kde=True,color='teal')
    ax12.set_xticklabels(ax12.get_xticklabels(), rotation=45, ha='right')
    st.pyplot(fig12)

# scatterplot for budget and revenue tell us is there a relation between budget and revenue

#  e=data[['budget','revenue']]
# ds=e.head(100)
# sns.scatterplot(data=ds,x='budget',y='revenue')

with t13:
    st.header('tell us is there a relation between budget and revenue')
    e=data[['budget','revenue']]
    ds=e.head(100)
    fig13,ax13=plt.subplots(figsize=(10,5))
    sns.scatterplot(data=ds,x='budget',y='revenue',ax=ax13)
    ax13.set_xticklabels(ax13.get_xticklabels(), rotation=45, ha='right')
    st.pyplot(fig13)