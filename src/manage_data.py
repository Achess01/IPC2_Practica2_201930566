import json
FILENAME = "podcasts.json"

def get_data():
    with open(FILENAME, encoding="utf-8") as file:
        data = json.load(file)
        return data

def add_data(data):
    with open(FILENAME, 'r+', encoding="utf-8") as file:
        json_data = json.load(file)
        data = json.loads(data)
        new_podcast = {
            "id": len(json_data)+1,
            "nombre": data['nombre'],
            "conductores": data['conductores'],
            "last_chapter": data['last_chapter']
        }
        json_data.append(new_podcast)
        file.seek(0)
        json.dump(json_data, file, ensure_ascii=False)
        file.truncate()
        return data