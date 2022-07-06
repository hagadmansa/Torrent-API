.eval 
import requests 
query = "doctor strange"
k = requests.get(f"https://api.safone.tech/torrent?query={query}")

name1 = k.json()['results'][1]['name']
size1 = k.json()['results'][1]['size']
seeders1 = k.json()['results'][1]['seeders']
leechers1 = k.json()['results'][1]['leechers']
magnetLink1 = k.json()['results'][1]['magnetLink']

name2 = k.json()['results'][2]['name']
size2 = k.json()['results'][2]['size']
seeders2 = k.json()['results'][2]['seeders']
leechers2 = k.json()['results'][2]['leechers']
magnetLink2 = k.json()['results'][2]['magnetLink']

name3 = k.json()['results'][3]['name']
size3 = k.json()['results'][3]['size']
seeders3 = k.json()['results'][3]['seeders']
leechers3 = k.json()['results'][3]['leechers']
magnetLink3 = k.json()['results'][3]['magnetLink']

name4 = k.json()['results'][4]['name']
size4 = k.json()['results'][4]['size']
seeders4 = k.json()['results'][4]['seeders']
leechers4 = k.json()['results'][4]['leechers']
magnetLink4 = k.json()['results'][4]['magnetLink']

name5 = k.json()['results'][5]['name']
size5  = k.json()['results'][5]['size']
seeders5 = k.json()['results'][5]['seeders']
leechers5 = k.json()['results'][5]['leechers']
magnetLink5 = k.json()['results'][5]['magnetLink']

name6 = k.json()['results'][6]['name']
size6 = k.json()['results'][6]['size']
seeders6 = k.json()['results'][6]['seeders']
leechers6 = k.json()['results'][6]['leechers']
magnetLink6 = k.json()['results'][6]['magnetLink']

name7 = k.json()['results'][7]['name']
size7 = k.json()['results'][7]['size']
seeders7 = k.json()['results'][7]['seeders']
leechers7 = k.json()['results'][7]['leechers']
magnetLink7 = k.json()['results'][7]['magnetLink']

name8 = k.json()['results'][8]['name']
size8 = k.json()['results'][8]['size']
seeders8 = k.json()['results'][8]['seeders']
leechers8 = k.json()['results'][8]['leechers']
magnetLink8 = k.json()['results'][8]['magnetLink']

name9 = k.json()['results'][9]['name']
size9 = k.json()['results'][9]['size']
seeders9 = k.json()['results'][9]['seeders']
leechers9 = k.json()['results'][9]['leechers']
magnetLink9 = k.json()['results'][9]['magnetLink']

name10 = k.json()['results'][10]['name']
size10 = k.json()['results'][10]['size']
seeders10 = k.json()['results'][10]['seeders']
leechers10 = k.json()['results'][10]['leechers']
magnetLink10 = k.json()['results'][10]['magnetLink']

data = f"""Torrent information for {query}

1. {name1}

📦 {size1}, 🟢 {seeders1}, 🔴 {leechers1}

📥 Magnet Link: {magnetLink1}

2. {name2}

📦 {size2}, 🟢 {seeders2}, 🔴 {leechers2}

📥 Magnet Link: {magnetLink2}

3. {name3}

📦 {size3}, 🟢 {seeders3}, 🔴 {leechers3}

📥 Magnet Link: {magnetLink3}

4. {name4}

📦 {size4}, 🟢 {seeders4}, 🔴 {leechers4}

📥 Magnet Link: {magnetLink4}

5. {name5}

📦 {size5}, 🟢 {seeders5}, 🔴 {leechers5}

📥 Magnet Link: {magnetLink5}

6. {name6}

📦 {size6}, 🟢 {seeders6}, 🔴 {leechers6}

📥 Magnet Link: {magnetLink6}

7. {name7}

📦 {size7}, 🟢 {seeders7}, 🔴 {leechers7}

📥 Magnet Link: {magnetLink7}

8. {name8}

📦 {size8}, 🟢 {seeders8}, 🔴 {leechers8}

📥 Magnet Link: {magnetLink8}

9. {name9}

📦 {size9}, 🟢 {seeders9}, 🔴 {leechers9}

📥 Magnet Link: {magnetLink9}

10. {name10}

📦 {size10}, 🟢 {seeders10}, 🔴 {leechers10}

📥 Magnet Link: {magnetLink10}

Powered by @hagadmansa"""

print(data)
