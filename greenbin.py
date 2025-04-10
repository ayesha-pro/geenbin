import pandas as pd
import folium

df = pd.read_csv('C:/Users/Ayesha/Desktop/locations.csv')
map_ = folium.Map(location=[24.8607, 67.0011], zoom_start=12)

for i, row in df.iterrows():
    folium.Marker(
        location=[row['Latitude'], row['Longitude']],
        popup=f"{row['Name']} - {row['Address']}"
    ).add_to(map_)

map_.save('greenbin_map.html')

import webbrowser
webbrowser.open("greenbin_map.html")