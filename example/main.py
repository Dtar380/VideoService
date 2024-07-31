from VideoService import *
from flask import Flask
from os.path import join

current_folder = "./example/"
database_folder = join(current_folder, "Database/")

video_service = VideoService(
    DATABASE=join(database_folder, "database.json"),
    MINIATURES=join(database_folder, "Miniatures"),
    VIDEOS=join(database_folder, "Videos"),
    UPLOADS=join(current_folder, "Uploads"),
    LANGUAGES=join(database_folder, "Languages")
)

app = Flask(__name__)

@app.route("/")
def main():
    pass

@app.route("/search")
def search():
    pass

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)