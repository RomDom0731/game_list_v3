import os
import time
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from sqlalchemy import or_, func, desc

app = Flask(__name__)
CORS(app)




app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    genre = db.Column(db.String(100), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    image_url = db.Column(db.Text)

@app.route('/api', methods=['GET'])
def get_games():
    page = int(request.args.get('page', 1))
    limit = int(request.args.get('limit', 10))
    search = request.args.get('search', '')
    sort_by = request.args.get('sort', 'title')

    query = Game.query.filter(or_(
        Game.title.ilike(f'%{search}%'),
        Game.genre.ilike(f'%{search}%')
    ))

    global_avg_rating = db.session.query(func.avg(Game.rating)).scalar() or 0

    top_genre_row = db.session.query(
        Game.genre, func.count(Game.genre).label('cnt')
    ).group_by(Game.genre).order_by(desc('cnt')).first()

    global_top_genre = top_genre_row[0] if top_genre_row else "N/A"

    if sort_by == 'rating':
        query = query.order_by(Game.rating.desc())
    else:
        query = query.order_by(Game.title.asc())

    pagination = query.paginate(page=page, per_page=limit, error_out=False)

    unique_genres = db.session.query(Game.genre).distinct().all()
    genres_list = [g[0] for g in unique_genres]

    return jsonify({
        "data": [{"id": g.id, "title": g.title, "genre": g.genre, "rating": g.rating, "image_url": g.image_url} for g in pagination.items],
        "total": pagination.total,
        "page": page,
        "totalPages": pagination.pages,
        "allGenres": genres_list,
        "globalAvgRating": round(float(global_avg_rating), 1),
        "globalTopGenre": global_top_genre
    })

@app.route('/api', methods=['POST'])
def save_game():
    body = request.get_json()
    if not body.get('title') or not body.get('genre'):
        return jsonify({"error": "Missing fields"}), 400
    
    if 'id' in body:
        game = Game.query.get(body['id'])
        if game:
            game.title = body['title']
            game.genre = body['genre']
            game.rating = body['rating']
            game.image_url = body.get('image_url')
    else:
        new_game = Game(
            title=body['title'],
            genre=body['genre'],
            rating=body['rating'],
            image_url=body.get('image_url')
        )
        db.session.add(new_game)
    
    db.session.commit()
    return jsonify({"success": True})

@app.route('/api', methods=['DELETE'])
def delete_game():
    game_id = int(request.args.get('id'))
    game = Game.query.get(game_id)
    if game:
        db.session.delete(game)
        db.session.commit()
    return jsonify({"success": True})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    port = int(os.environ.get("PORT", 5001))
    app.run(host='0.0.0.0', port=port)