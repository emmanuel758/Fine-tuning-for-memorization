import json

input_files = ['dataset_matricule_2.json', 'dataset_nom_2.json' ]
dataset_file = 'dataset_final.json'
dataset_data = []

final_list = []
for file in input_files:
    with open(file, 'r') as f:
        data = json.load(f)
        for item in data:
            final_list.append(item)
with open(dataset_file, 'w',encoding="utf-8") as f:
        json.dump(final_list, f, ensure_ascii= False, indent=4)
