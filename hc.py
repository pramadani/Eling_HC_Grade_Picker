# Read the data files
with open('data/nama.txt', 'r') as f:
    nama_list = f.read().lower().splitlines()

with open('data/nim.txt', 'r') as f:
    nim_list = f.read().splitlines()

with open('raw/plain.txt', 'r') as f:
    plain_text = f.read().lower().split("\nindonesia\n")

with open('data/username.txt', 'r') as f:
    username_list = f.read().lower().splitlines()

data_list = [{'nama': nama.lower(), 'username': username, 'nim': nim, 'nilai': '0'} for nama, username, nim in zip(nama_list, username_list, nim_list)]

for index, data in enumerate(plain_text):
    lines = data.split("\n")
    
    username = lines[2].strip()
    nilai = lines[5].strip().replace('.', ',')
    
    if username in username_list:
        nim = nim_list[username_list.index(username)]
        
        for entry in data_list:
            if entry['nim'] == nim:
                entry['nilai'] = nilai

with open('result/grade.txt', 'w') as f:
    for item in data_list:
        f.write(f"{item['nilai']}\n")

with open('result/desc.txt', 'w') as f:
    for item in data_list:
        f.write(f"{item['nim']}\t{item['nama']}\t{item['username']}\t{item['nilai']}\n")