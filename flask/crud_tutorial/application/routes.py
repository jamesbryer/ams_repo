from application import app, db
from application.models import Games

@app.route('/add/<name>')
def add(name):
    new_game = Games(name=name)
    db.session.add(new_game)
    db.session.commit()
    return (f"Added {name} to database")

@app.route('/read')
def read():
    all_games = Games.query.all()
    games_string = ""
    for game in all_games:
        games_string += "<br>" + str(game.id) + " " + game.name
    return games_string

@app.route('/update/<name>')
def update(name):
    first_game = Games.query.first()
    first_game.name = name
    db.session.commit()
    return first_game.name

@app.route('/delete/int:<id>')
def delete(id):
    game_to_delete = Games.query.filter_by(id=id).first()
    db.session.delete(game_to_delete)
    db.session.commit()
    return "Deleted first game from database"