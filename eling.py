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
    plain_text = f.read().lower().split("\n \n")

data_list = [{'nama': nama, 'nim': nim, 'nilai': '0'} for nama, nim in zip(nama_list, nim_list)]

for index, data in enumerate(plain_text):
    lines = data.split("\n")
    
    nama = lines[0].strip().split('\t')[2]
    nilai = lines[1].strip().split(' / ')[0].replace('.', ',')
    
    nim = nim_list[nama_list.index(nama)]
    
    for entry in data_list:
        if entry['nim'] == nim:
            entry['nilai'] = nilai

with open(os.path.join(result_folder, 'grade.txt'), 'w') as f:
    for item in data_list:
        f.write(f"{item['nilai']}\n")

with open(os.path.join(result_folder, 'desc.txt'), 'w') as f:
    for item in data_list:
        f.write(f"{item['nim']}\t{item['nama']}\t{item['nilai']}\n")

print("Proses selesai!")
