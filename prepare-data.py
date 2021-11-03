import csv
import json
import os
import zipfile
from collections import OrderedDict

zip_ref = zipfile.ZipFile("archive.zip", 'r')
zip_ref.extractall()
zip_ref.close()

csv_file = 'pokemon.csv'
json_file = 'pokemon.json'


def format(item):
    if item.startswith("["):
        return item
    try:
        return int(item)
    except ValueError:
        try:
            return float(item)
        except ValueError:
            return item

with open(csv_file) as f:
    reader = csv.DictReader(f)
    fields = reader.fieldnames

    for row in reader:
        orderedRow = OrderedDict(row)
        for k, v in orderedRow.items():
            orderedRow[k] = format(v)
            if orderedRow[k] == "":
                orderedRow[k] = 0

        orderedRow["_type"] = "Pokemon"
        orderedRow.move_to_end("_type", last=False)

        json_doc = json.dumps(orderedRow, indent=4, separators=(',', ': '))
        file_name = orderedRow['name'].replace(' ', '') + ".json"
        with open(os.path.join("data/", file_name), "w") as j:
            j.write(json_doc)
