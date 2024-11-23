import os

data_folder = 'data'
raw_folder = 'raw'
result_folder = 'result'

if not os.path.exists(data_folder):
    raise FileNotFoundError(f"Folder {data_folder} tidak ditemukan.")
if not os.path.exists(os.path.join(data_folder, 'nama.txt')):
    raise FileNotFoundError("File 'nama.txt' tidak ditemukan di folder 'data'.")
if not os.path.exists(os.path.join(data_folder, 'nim.txt')):
    raise FileNotFoundError("File 'nim.txt' tidak ditemukan di folder 'data'.")
if not os.path.exists(os.path.join(data_folder, 'username.txt')):
    raise FileNotFoundError("File 'username.txt' tidak ditemukan di folder 'data'.")

if not os.path.exists(raw_folder):
    raise FileNotFoundError(f"Folder {raw_folder} tidak ditemukan.")
if not os.path.exists(os.path.join(raw_folder, 'plain.txt')):
    raise FileNotFoundError("File 'plain.txt' tidak ditemukan di folder 'raw'.")

if not os.path.exists(result_folder):
    os.makedirs(result_folder) 

with open(os.path.join(data_folder, 'nama.txt'), 'r') as f:
    nama_list = f.read().lower().splitlines()

with open(os.path.join(data_folder, 'nim.txt'), 'r') as f:
    nim_list = f.read().splitlines()

with open(os.path.join(raw_folder, 'plain.txt'), 'r') as f:
    plain_text = f.read().lower().split("\nindonesia\n")

with open(os.path.join(data_folder, 'username.txt'), 'r') as f:
    username_list = f.read().lower().splitlines()

data_list = [{'nama': nama, 'username': username, 'nim': nim, 'nilai': '0'} for nama, username, nim in zip(nama_list, username_list, nim_list)]

for index, data in enumerate(plain_text):
    lines = data.split("\n")
    
    username = lines[2].strip()
    nilai = lines[5].strip().replace('.', ',')

    if username in username_list:
        nim = nim_list[username_list.index(username)]
        
        for entry in data_list:
            if entry['nim'] == nim:
                entry['nilai'] = nilai

with open(os.path.join(result_folder, 'grade.txt'), 'w') as f:
    for item in data_list:
        f.write(f"{item['nilai']}\n")

with open(os.path.join(result_folder, 'desc.txt'), 'w') as f:
    for item in data_list:
        f.write(f"{item['nim']}\t{item['nama']}\t{item['username']}\t{item['nilai']}\n")

print("Proses selesai!")
