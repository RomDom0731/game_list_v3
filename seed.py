import os
from app import app, db, Game

initial_data = [
    {"title": "Fortnite", "genre": "Third-Person Shooter", "rating": 9.0, "image_url": "https://placehold.co/300x400?text=Fortnite"},
    {"title": "Legend of Heroes: Trails to Azure", "genre": "JRPG", "rating": 9.0, "image_url": "https://placehold.co/300x400?text=Trails+to+Azure"},
    {"title": "The Legend of Zelda: Breath of the Wild", "genre": "Action-Adventure", "rating": 10.0, "image_url": "https://placehold.co/300x400?text=Zelda+BOTW"},
    {"title": "Elden Ring", "genre": "Action RPG", "rating": 10.0, "image_url": "https://placehold.co/300x400?text=Elden+Ring"},
    {"title": "Minecraft", "genre": "Sandbox", "rating": 9.5, "image_url": "https://placehold.co/300x400?text=Minecraft"},
    {"title": "Cyberpunk 2077", "genre": "Action RPG", "rating": 8.5, "image_url": "https://placehold.co/300x400?text=Cyberpunk+2077"},
    {"title": "The Witcher 3: Wild Hunt", "genre": "RPG", "rating": 10.0, "image_url": "https://placehold.co/300x400?text=Witcher+3"},
    {"title": "Red Dead Redemption 2", "genre": "Action-Adventure", "rating": 10.0, "image_url": "https://placehold.co/300x400?text=RDR2"},
    {"title": "Hades", "genre": "Roguelike", "rating": 9.0, "image_url": "https://placehold.co/300x400?text=Hades"},
    {"title": "Stardew Valley", "genre": "Simulation", "rating": 9.5, "image_url": "https://placehold.co/300x400?text=Stardew+Valley"},
    {"title": "Overwatch 2", "genre": "Hero Shooter", "rating": 7.5, "image_url": "https://placehold.co/300x400?text=Overwatch+2"},
    {"title": "Baldur's Gate 3", "genre": "RPG", "rating": 10.0, "image_url": "https://placehold.co/300x400?text=Baldurs+Gate+3"},
    {"title": "Valorant", "genre": "Tactical Shooter", "rating": 8.0, "image_url": "https://placehold.co/300x400?text=Valorant"},
    {"title": "Apex Legends", "genre": "Battle Royale", "rating": 8.5, "image_url": "https://placehold.co/300x400?text=Apex+Legends"},
    {"title": "God of War Ragnarök", "genre": "Action-Adventure", "rating": 9.5, "image_url": "https://placehold.co/300x400?text=God+of+War"},
    {"title": "Final Fantasy VII Rebirth", "genre": "RPG", "rating": 9.5, "image_url": "https://placehold.co/300x400?text=FFVII+Rebirth"},
    {"title": "Doom Eternal", "genre": "First-Person Shooter", "rating": 9.0, "image_url": "https://placehold.co/300x400?text=Doom+Eternal"},
    {"title": "Hollow Knight", "genre": "Metroidvania", "rating": 10.0, "image_url": "https://placehold.co/300x400?text=Hollow+Knight"},
    {"title": "Celeste", "genre": "Platformer", "rating": 9.0, "image_url": "https://placehold.co/300x400?text=Celeste"},
    {"title": "Sea of Thieves", "genre": "Adventure", "rating": 8.0, "image_url": "https://placehold.co/300x400?text=Sea+of+Thieves"},
    {"title": "Rocket League", "genre": "Sports", "rating": 8.5, "image_url": "https://placehold.co/300x400?text=Rocket+League"},
    {"title": "Grand Theft Auto V", "genre": "Action-Adventure", "rating": 9.5, "image_url": "https://placehold.co/300x400?text=GTA+V"},
    {"title": "Mass Effect Legendary Edition", "genre": "RPG", "rating": 10.0, "image_url": "https://placehold.co/300x400?text=Mass+Effect"},
    {"title": "Ghost of Tsushima", "genre": "Action-Adventure", "rating": 9.0, "image_url": "https://placehold.co/300x400?text=Ghost+of+Tsushima"},
    {"title": "Persona 5 Royal", "genre": "JRPG", "rating": 10.0, "image_url": "https://placehold.co/300x400?text=Persona+5"},
    {"title": "Animal Crossing: New Horizons", "genre": "Simulation", "rating": 8.5, "image_url": "https://placehold.co/300x400?text=Animal+Crossing"},
    {"title": "Disco Elysium", "genre": "RPG", "rating": 9.5, "image_url": "https://placehold.co/300x400?text=Disco+Elysium"},
    {"title": "Portal 2", "genre": "Puzzle", "rating": 10.0, "image_url": "https://placehold.co/300x400?text=Portal+2"},
    {"title": "Outer Wilds", "genre": "Exploration", "rating": 9.5, "image_url": "https://placehold.co/300x400?text=Outer+Wilds"},
    {"title": "Street Fighter 6", "genre": "Fighting", "rating": 8.5, "image_url": "https://placehold.co/300x400?text=Street+Fighter+6"},
    {"title": "Rhythm Heaven", "genre": "Music", "rating": 8.0, "image_url": "https://placehold.co/300x400?text=Rhythm+Heaven"}
]

def seed_database():
    with app.app_context():
        if Game.query.count() == 0:
            for item in initial_data:
                game = Game(**item)
                db.session.add(game)
            db.session.commit()
            print("Database seeded with 30 records.")
        else:
            print("Database already contains data.")

if __name__ == '__main__':
    seed_database()