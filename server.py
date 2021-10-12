"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']

DISS_TRACKS = [
  "stupid", "dogwater", "disrespectful", "mean", "annoying", "dense",
  "not cool", "rude", "spiteful", "hurtful", "nasty", "cruel"]


@app.route('/')
def start_here():
    """Home page."""

    return """
    <!doctype html>
    <html>
      <body>
        <h1> Hi! This is the home page. </h1>
        <a href="/hello"> say hello </a>
      </body>
    </html>
    """


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          What's your name? <input type="text" name="person"> <br>
          Pick a word out of these options. <br>
          <input type="radio" name="compliment" value ="awesome"> <label> awesome </label>
          <input type="radio" name="compliment" value ="terrific"> <label> terrific </label>
          <input type="radio" name="compliment" value ="fantastic"> <label> fantastic </label>
          <input type="radio" name="compliment" value ="neato"> <label> neato </label> 
          <input type="radio" name="compliment" value ="fantabulous"> <label> fantabulous </label>
          <input type="radio" name="compliment" value ="wowza"> <label> wowza </label>
          <input type="radio" name="compliment" value ="oh-so-not-meh"> <label> oh-so-not-meh </label>
          <br>
          <input type="radio" name="compliment" value ="brillant"> <label> brilliant </label>
          <input type="radio" name="compliment" value ="ducky"> <label> ducky </label>
          <input type="radio" name="compliment" value ="collio"> <label> collio </label>
          <input type="radio" name="compliment" value ="incredible"> <label> incredible </label>
          <input type="radio" name="compliment" value ="wonderful"> <label> wonderful </label>
          <input type="radio" name="compliment" value ="smashing"> <label> smashing </label>
          <input type="radio" name="compliment" value ="lovely"> <label> lovely </label>
          <br> 
          <input type="submit" value="Submit">
        </form>

        <form action="/diss">
          What's your name? <input type="text" name="person"> <br>
          <input type="submit" value="If you're not feeling up for a compliment">
        </form>
      </body>
    </html>
    """


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    compliment = request.args.get("compliment")

    return f"""
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {player}! I think you're {compliment}!
      </body>
    </html>
    """

@app.route('/diss')
def diss_person():
  """Get user by name."""

  player = request.args.get("person")
  diss = choice(DISS_TRACKS)

  return f"""
  <!doctype html>
  <html>
    <head>
      <title> A Diss</title>
    </head>
    <body>
      Hi, {player}, I think you're {diss}.
    </body>
  </html>
  """


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
