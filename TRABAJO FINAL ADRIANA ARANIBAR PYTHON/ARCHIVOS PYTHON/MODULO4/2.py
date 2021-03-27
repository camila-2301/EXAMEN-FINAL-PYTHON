import pandas as pd
airbnb = pd.read_csv("./data/pandas/airbnb.csv")

#CASO 1
alternativas = airbnb[(airbnb["reviews"] > 10) & (airbnb["overall_satisfaction"] > 4) & (airbnb["bedrooms"] == 2)].sort_values(by=['overall_satisfaction'], ascending=False)
print(alternativas.head(3))

#CASO 2
habitaciones = airbnb[(airbnb["room_id"]==97503) | (airbnb["room_id"]==90387)]
print(habitaciones.to_excel('roberto.xls', index = False))

#CASO 3
habita = airbnb[(airbnb["room_type"] == 'Shared room') & (airbnb["price"] <= 50/3)].sort_values(by=['overall_satisfaction'], ascending=False)
print(habita.head(10))
