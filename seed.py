import os
from app import app, db, Game

initial_data = [
    {"title": "Fortnite", "genre": "Third-Person Shooter", "rating": 9.0, "image_url": "https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/2170320/header.jpg"},
    {"title": "Legend of Heroes: Trails to Azure", "genre": "JRPG", "rating": 9.0, "image_url": "https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/1668520/header.jpg"},
    {"title": "The Legend of Zelda: Breath of the Wild", "genre": "Action-Adventure", "rating": 10.0, "image_url": "https://assets.nintendo.com/image/upload/ar_16:9,c_lpad,w_656/b_white/f_auto/q_auto/v1/ncom/en_US/games/switch/t/the-legend-of-zelda-breath-of-the-wild-switch/hero"},
    {"title": "Elden Ring", "genre": "Action RPG", "rating": 10.0, "image_url": "https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/1245620/header.jpg"},
    {"title": "Minecraft", "genre": "Sandbox", "rating": 9.5, "image_url": "https://assets-prd.ignimgs.com/2021/12/14/minecraft-1639513933156.jpg"},
    {"title": "Cyberpunk 2077", "genre": "Action RPG", "rating": 8.5, "image_url": "https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/1091500/header.jpg"},
    {"title": "The Witcher 3: Wild Hunt", "genre": "RPG", "rating": 10.0, "image_url": "https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/292030/header.jpg"},
    {"title": "Red Dead Redemption 2", "genre": "Action-Adventure", "rating": 10.0, "image_url": "https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/1174180/header.jpg"},
    {"title": "Hades", "genre": "Roguelike", "rating": 9.0, "image_url": "https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/1145360/header.jpg"},
    {"title": "Stardew Valley", "genre": "Simulation", "rating": 9.5, "image_url": "https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/413150/header.jpg"},
    {"title": "Overwatch 2", "genre": "Hero Shooter", "rating": 7.5, "image_url": "https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/2357570/header.jpg"},
    {"title": "Baldur's Gate 3", "genre": "RPG", "rating": 10.0, "image_url": "https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/1086940/header.jpg"},
    {"title": "Valorant", "genre": "Tactical Shooter", "rating": 8.0, "image_url": "https://upload.wikimedia.org/wikipedia/commons/f/fc/Valorant_logo_-_pink_color_version.svg"},
    {"title": "Apex Legends", "genre": "Battle Royale", "rating": 8.5, "image_url": "https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/1172470/header.jpg"},
    {"title": "God of War Ragnarök", "genre": "Action-Adventure", "rating": 9.5, "image_url": "https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/2322010/header.jpg"},
    {"title": "Final Fantasy VII Rebirth", "genre": "RPG", "rating": 9.5, "image_url": "https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/2909400/c4e617a13d511a72b2787c91e0e08fbe57c99191/capsule_616x353.jpg?t=1770723867"},
    {"title": "Doom Eternal", "genre": "First-Person Shooter", "rating": 9.0, "image_url": "https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/782330/header.jpg"},
    {"title": "Hollow Knight", "genre": "Metroidvania", "rating": 10.0, "image_url": "https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/367520/header.jpg"},
    {"title": "Celeste", "genre": "Platformer", "rating": 9.0, "image_url": "https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/504230/header.jpg"},
    {"title": "Sea of Thieves", "genre": "Adventure", "rating": 8.0, "image_url": "https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/1172620/header.jpg"},
    {"title": "Rocket League", "genre": "Sports", "rating": 8.5, "image_url": "https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/252950/header.jpg"},
    {"title": "Grand Theft Auto V", "genre": "Action-Adventure", "rating": 9.5, "image_url": "https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/271590/header.jpg"},
    {"title": "Mass Effect Legendary Edition", "genre": "RPG", "rating": 10.0, "image_url": "https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/1328670/header.jpg"},
    {"title": "Ghost of Tsushima", "genre": "Action-Adventure", "rating": 9.0, "image_url": "https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/2215430/header.jpg"},
    {"title": "Persona 5 Royal", "genre": "JRPG", "rating": 10.0, "image_url": "https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/1687950/header.jpg"},
    {"title": "Animal Crossing: New Horizons", "genre": "Simulation", "rating": 8.5, "image_url": "https://assets.nintendo.com/image/upload/ar_16:9,c_lpad,w_656/b_white/f_auto/q_auto/v1/ncom/en_US/games/switch/a/animal-crossing-new-horizons-switch/hero"},
    {"title": "Disco Elysium", "genre": "RPG", "rating": 9.5, "image_url": "https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/632470/header.jpg"},
    {"title": "Portal 2", "genre": "Puzzle", "rating": 10.0, "image_url": "https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/620/header.jpg"},
    {"title": "Outer Wilds", "genre": "Exploration", "rating": 9.5, "image_url": "https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/753640/header.jpg"},
    {"title": "Street Fighter 6", "genre": "Fighting", "rating": 8.5, "image_url": "https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/1364780/header.jpg"},
    {"title": "Rhythm Heaven", "genre": "Music", "rating": 8.0, "image_url": "https://upload.wikimedia.org/wikipedia/en/thumb/3/38/RhythmHeaven.PNG/250px-RhythmHeaven.PNG"}
]

def seed_database():
    with app.app_context():
        if Game.query.count() == 0:
            for item in initial_data:
                game = Game(**item)
                db.session.add(game)
            db.session.commit()
            print("Database seeded with 31 records.")
        else:
            print("Database already contains data.")

if __name__ == '__main__':
    seed_database()