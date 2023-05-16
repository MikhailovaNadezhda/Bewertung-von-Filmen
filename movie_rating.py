# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 12:35:22 2021

@author: Mikhailova
"""
#
import pandas as pd
import numpy as np

#open file
data=pd.read_csv("1.csv")
#creating a new file to record the result
data_recomendation=pd.DataFrame(columns=['user','user_parent','film_recomend'])
#looping through all lines
for i,row in data.iterrows():
    film=row[0]
    user=row[1]
    #list of all watched movies by this user
    film_user=data[data['user']==user]['film']
    #a table that includes all users who have watched this movie
    users=data[(data['film']==film) & (data['user']!=user)]
    #viewing these users
    for j,row2 in users.iterrows():
        user2=row2[1]
        #select all films for user2, excluding film
        film2=data[(data['user']==user2)&(data['film']!=film)]
        for i2,row3 in film2.iterrows():
            #collect the recommended films in the date_recomendation. Check if the environment of these films, films that the user has watched
            if row3[0] not in film_user.values:
                data_recomendation=data_recomendation.append({'user':user,'user_parent':user2,'film_recomend':row3[0]},ignore_index=True)
#delete from the table the same movies that were received from one user
data_recomendation.drop_duplicates(inplace=True)
data_recomendation.sort_values(by=['user'],inplace=True)
#grouping by user and movie
data2=data_recomendation.groupby(['user','film_recomend']).count()
data2.rename(columns={'user_parent': 'rating_in_%'}, inplace=True)
data3=data_recomendation.groupby(['user']).count()
#count the rating as a percentage
data2['rating_in_%']=data2['rating_in_%']/data3['user_parent']*100
data2=data2.round(2)
#save to the final file
data2.to_csv('2.csv')

   


