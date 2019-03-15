from flask import Flask
from flask import render_template
from flask import request
from flask import send_from_directory
from random import randint, choice
from jokes_quotes_list import list_of_jokes,list_of_Albert_Einstein_quotes, list_of_Dalai_Lama_quotes

app = Flask(__name__)

# Serve static content
@app.route("/style.css")
def serve_style_css():
  return send_from_directory('templates', 'style.css')

@app.route("/")
def name():
  return render_template('welcome.html')

@app.route("/hello.html")
def hello():
    name = request.args.get("name")
    return render_template ('hello.html', name=name)

# generates random joke from the list_of_jokes imported from jokes_quotes_list
@app.route("/want_to_play_game_no.html")
def joke():
    joke = choice(list_of_jokes)
    return render_template ('/want_to_play_game_no.html', joke=joke)

@app.route("/want_to_play_game_yes.html")
def ask():
  return render_template("want_to_play_game_yes.html")

# generates random handsign from (rock, paper, scissors) list for computer and gets player choice from previous page
@app.route("/game_result.html")
def result():
  choices = ["rock", "paper", "scissors"]
  player_choice = request.args.get('player_choice', '')
  computer_choice = choice(choices)

  win = "undefined"
  if player_choice == computer_choice:
    win = "It's a tie..."
  elif player_choice == "rock" and computer_choice == "paper":
    win = "I win"
  elif player_choice == "rock" and computer_choice == "scissors":
    win = "You win" 
  elif player_choice == "paper" and computer_choice == "rock":
    win = "You win"
  elif player_choice == "paper" and computer_choice == "scissors":
    win = "I win" 
  elif player_choice == "scissors" and computer_choice == "paper":
    win = "You win"
  elif player_choice == "scissors" and computer_choice == "rock":
    win = "I win" 

# generates random quote from the list of quotes imported from jokes_quotes_list 
# (if computer wins - Albert Einstein's, if player wins - Dalai Lama's)
  quote = None
  if win == "I win":
      quote = choice(list_of_Albert_Einstein_quotes)
  elif win == "You win":
      quote = choice(list_of_Dalai_Lama_quotes)


  return render_template("game_result.html", player_choice = player_choice, computer_choice = computer_choice, win = win, quote = quote)
