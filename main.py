from flask import Flask, jsonify, render_template, request
import random

app = Flask(__name__)

# Kumpulan avatar berdasarkan jenis
avatars = {
    "anime": [
        "https://api.dicebear.com/7.x/adventurer/png?seed=Naruto",
        "https://api.dicebear.com/7.x/adventurer/png?seed=Sasuke",
        "https://api.dicebear.com/7.x/adventurer/png?seed=Luffy",
        "https://api.dicebear.com/7.x/adventurer/png?seed=Zoro"
    ],
    "robot": [
        "https://api.dicebear.com/7.x/bottts/png?seed=Mecha1",
        "https://api.dicebear.com/7.x/bottts/png?seed=RoboX",
        "https://api.dicebear.com/7.x/bottts/png?seed=Cybertron",
        "https://api.dicebear.com/7.x/bottts/png?seed=AI99"
    ],
    "pixel": [
        "https://api.dicebear.com/7.x/pixel-art/png?seed=Blocky",
        "https://api.dicebear.com/7.x/pixel-art/png?seed=PixelWarrior",
        "https://api.dicebear.com/7.x/pixel-art/png?seed=RetroGuy",
        "https://api.dicebear.com/7.x/pixel-art/png?seed=8BitHero"
    ]
}

@app.route('/api/avatar', methods=['GET'])
def get_avatar():
    avatar_type = request.args.get('type', 'anime')  # Default: anime
    if avatar_type not in avatars:
        return jsonify({"error": "Tipe avatar tidak tersedia"}), 400
    return jsonify({"avatar": random.choice(avatars[avatar_type])})

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
