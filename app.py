from flask import Flask, request, render_template, jsonify, session
from uuid import uuid4
from flask_debugtoolbar import DebugToolbarExtension
from boggle import BoggleGame
from wordlist import english_words


app = Flask(__name__)
app.config["SECRET_KEY"] = "this-is-secret"
debug = DebugToolbarExtension(app)
# The boggle games created, keyed by game id
# games = {
#     1 : BoggleGame() # NOTE: used for testing
# }


games = {}
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
    session["game_id"] = game_id
    games[game_id] = game
    return jsonify( {"gameId":game_id, "board":game.board} )


@app.route('/api/score-word', methods=["POST"])
def score_word():
    """Scores word submitted in form"""    
    #It should be in the word list
    #It sound be findable on the board

    game_id = session["game_id"]
    new_word = request.form['word'].strip().upper()
    game = games[game_id]
    response = None
    

    if new_word not in english_words.words:
        return {"result": "not-word"}

    elif game.check_word_on_board(new_word):
        response = {"result": "not-on-board"}

    elif game.is_word_in_word_list(new_word):
        # Word is in word list, score word
        response = {"result": "ok"}
    # game.play_and_score_word(new_word)
    
    return  jsonify(response)



    
    


    

    

    
    