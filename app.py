from flask import Flask, request, render_template, jsonify, session
from uuid import uuid4
from flask_debugtoolbar import DebugToolbarExtension
from boggle import BoggleGame

app = Flask(__name__)
app.config["SECRET_KEY"] = "this-is-secret"
debug = DebugToolbarExtension(app)
# The boggle games created, keyed by game id
games = {
    1 : BoggleGame() # NOTE: used for testing
}

@app.route("/")
def homepage():
    """Show board."""
    
    return render_template("index.html")


@app.route("/api/new-game")
def new_game():
    """Start a new game and return JSON: {game_id, board}."""
    # get a unique id for the board we're creating
    game_id = str(uuid4())
    game = BoggleGame()
    games[game_id] = game
    return jsonify( {"gameId":game_id, "board":game.board} )


@app.route('/api/score-word', methods=["POST"])
def score_word():
    """Scores word submitted in form"""    
    #It should be in the word list
    #It sound be findable on the board

    new_word = request.form('word')

    curr_game_id = 1  # NOTE: used for testing 

    current_game = games[curr_game_id]   # NOTE: used for testing 
    
    if current_game.is_word_in_word_list(new_word):
        pass
    elif current_game.is_word_not_a_dup(new_word):
        pass
    elif current_game.check_word_on_board(new_word):
        current_game.play_and_score_word(new_word)
    
    #update game in games

    games[curr_game_id] = current_game

    

    
    