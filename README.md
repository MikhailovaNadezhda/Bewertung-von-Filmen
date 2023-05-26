## Eine Bewertung von Filmen mit Empfehlung von Ansichten

Es gab eine Tabelle mit der Geschichte des Ansehens von Filmen in einem Online-Kino.
Zwei Felder: Benutzer, Film

Ich habe ein Python-Skript erstellt,
die die Logik des Algorithmus implementieren würden, um Filme zum Ansehen zu empfehlen, die Benutzer noch nicht gesehen haben.

Die Logik ist folgende:
<br>•Nehmen wir an, der Benutzer hat sich Film A angesehen
<br>•Stellen Sie fest, welche anderen Benutzer Film A gesehen haben
<br>• Bestimmen Sie, welche anderen Filme alle diese Benutzer gesehen haben
<br>•Wir gruppieren die gefundenen Filme nach Namen und ermitteln für jeden die Anzahl der Nutzer, die ihn angesehen haben
<br>•Je mehr Benutzer es angesehen haben, desto höher ist ihre Bewertung in der Empfehlungsliste.
<br>•Die abschließende Abfrage sollte alle Filme, die alle Nutzer angesehen haben, im Empfehlungsmodell berücksichtigen.
<br>•Ausgabetabelle: Benutzer, Empfehlungsfilm, Bewertung der Empfehlung

Die Datei im CSV-Format sieht folgendermaßen aus:

![image](https://github.com/MikhailovaNadezhda/Bewertung-von-Filmen/blob/main/2023-05-26_09h26_26.png)

Erstellen wir mithilfe dieses Python-Skripts eine neue Tabelle mit Empfehlung von Filmen 

```python

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
   ```
   
Wir erhalten eine Tabelle mit Empfehlungen für jeden Benutzer, in der die prozentuale Bewertung für jeden empfohlenen Film angegeben ist:

![image](https://github.com/MikhailovaNadezhda/Bewertung-von-Filmen/blob/main/2023-05-26_09h49_59.png)
  
