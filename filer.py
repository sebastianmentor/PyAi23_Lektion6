import json
import os

konstig_datastruktur = [1,2,[{1:2,2:3,3:4}, (1,2,3,4)]]

with open('konstig_json.json', 'w') as f:
    json.dump(konstig_datastruktur, f)

if os.path.exists('konstig_json.json'):
    with open('konstig_json.json') as f:
        new_data = json.load(f)

print(new_data)
print(new_data[1])
print(new_data[2][0]['2'])
print(new_data[2][1])

