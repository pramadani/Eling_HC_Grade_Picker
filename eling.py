# Read the input files
with open('input/nama.txt', 'r') as f:
    nama_list = f.read().lower().splitlines()

with open('input/nim.txt', 'r') as f:
    nim_list = f.read().splitlines()

with open('input/plain.txt', 'r') as f:
    plain_text = f.read().lower().split("\n \n")

data_list = [{'nama': nama.lower(), 'nim': nim, 'nilai': '0'} for nama, nim in zip(nama_list, nim_list)]

for index, data in enumerate(plain_text):
    lines = data.split("\n")
    
    nama = lines[0].strip().split('\t')[2]
    nilai = lines[1].strip().split(' / ')[0].replace('.', ',')
    
    nim = nim_list[nama_list.index(nama)]
    
    for entry in data_list:
        if entry['nim'] == nim:
            entry['nilai'] = nilai

with open('output/grade.txt', 'w') as f:
    for item in data_list:
        f.write(f"{item['nilai']}\n")

with open('output/desc.txt', 'w') as f:
    for item in data_list:
        f.write(f"{item['nim']}\t{item['nama']}\t{item['nilai']}\n")