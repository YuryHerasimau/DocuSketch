from flask import Flask, request
from flask_pymongo import PyMongo
from dotenv import load_dotenv
import os


load_dotenv()
MONGO_URI = os.getenv("MONGO_URI")

app = Flask(__name__)
app.config["MONGO_URI"] = MONGO_URI
db = PyMongo(app).db


@app.route("/api/key/<string:key>", methods=["GET"])
def get_value_by_key(key):
    """Читаем значение ключа"""

    result = db.keys.find_one({key: {"$exists": True}})
    if result:
        return {"key": key, "value": result[key]}, 200
    else:
        return {"message": "Ключ не найден"}, 404


@app.route("/api/key", methods=["POST"])
def create_key_and_value():
    """API эндпоинт для создания значения ключ=значение"""

    key = request.json.get("key")
    value = request.json.get("value")
    if key and value:
        db.keys.insert_one({key: value})
        new_key = db.keys.find_one({key: value})
        return {
            "message": f'Ключ=значение успешно создано. ObjectID={new_key.get("_id")}'
        }, 201
    else:
        return {"message": "Не указаны ключ или значение"}, 400


@app.route("/api/key/<string:key>", methods=["PUT"])
def update_value_by_key(key):
    """API эндпоинт для изменения ключ=новое_значение"""

    new_value = request.json.get("value")
    if new_value:
        result = db.keys.update_one(
            {key: {"$exists": True}}, {"$set": {key: new_value}}
        )
        if result.modified_count > 0:
            return {"message": "Значение ключа успешно изменено"}, 200
        else:
            return {"message": "Ключ не найден"}, 404
    else:
        return {"message": "Не указано новое значение ключа"}, 400


if __name__ == "__main__":
    app.run(port=8080, debug=True)
