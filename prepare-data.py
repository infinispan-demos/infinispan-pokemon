import csv
import json
import os
import zipfile

zip_ref = zipfile.ZipFile("pokemon.zip", 'r')
zip_ref.extractall()
zip_ref.close()

csv_file = 'pokemon.csv'
json_file = 'pokemon.json'


def to_number(item):
    try:
        return float(item)
    except:
        return item


with open(csv_file) as f:
    reader = csv.DictReader(f)
    fields = reader.fieldnames

    for row in reader:
        for k, v in row.items():
            row[k] = to_number(v)
            if row[k] == "":
                row[k] = 0

        row["_type"] = "Pokemon"
        row.move_to_end("_type", last=False)

        json_doc = json.dumps(row, indent=4, separators=(',', ': '))
        file_name = row['name'].replace(' ', '') + ".json"
        with open(os.path.join("data/", file_name), "w") as j:
            j.write(json_doc)
