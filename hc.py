# Read the input files
with open('input/nama.txt', 'r') as f:
    nama_list = f.read().lower().splitlines()

with open('input/nim.txt', 'r') as f:
    nim_list = f.read().splitlines()

with open('input/plain.txt', 'r') as f:
    plain_text = f.read().lower().split("\nindonesia\n")

with open('input/username.txt', 'r') as f:
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

with open('output/grade.txt', 'w') as f:
    for item in data_list:
        f.write(f"{item['nilai']}\n")

with open('output/desc.txt', 'w') as f:
    for item in data_list:
        f.write(f"{item['nim']}\t{item['nama']}\t{item['username']}\t{item['nilai']}\n")