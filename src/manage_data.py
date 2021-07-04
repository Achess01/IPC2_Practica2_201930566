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
    
def edit_data(id, data):
    with open(FILENAME, 'r+', encoding="utf-8") as file:
        json_data = json.load(file)
        data = json.loads(data)               
        podcastFound = [podcast for podcast in json_data if podcast['id'] == id]
        if len(podcastFound) > 0:
            podcastFound[0]['last_chapter'] = data['url']
            file.seek(0)
            json.dump(json_data, file, ensure_ascii=False)
            file.truncate()
            return podcastFound[0]
        else:
            return None

def delete_data(id):
    with open(FILENAME, 'r+', encoding="utf-8") as file:
        json_data = json.load(file)                     
        podcastFound = [podcast for podcast in json_data if podcast['id'] == id]
        if len(podcastFound) > 0:
            json_data.remove(podcastFound[0])
            file.seek(0)
            json.dump(json_data, file, ensure_ascii=False)
            file.truncate()
            return podcastFound[0]
        else:
            return None
        
        
        
        