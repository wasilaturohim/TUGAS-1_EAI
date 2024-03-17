from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def root():
    return "Welcome to Premier League and Primeira Liga Standings!"

@app.route('/liga')
def get_standings():
    premier_url = "https://premier-league-standings1.p.rapidapi.com/"
    primeira_url = "https://primeira-liga-standings.p.rapidapi.com/"
    
    premier_headers = {
        "X-RapidAPI-Key": "ad19e9c691msh38e569ff9db4f62p16dce4jsna60233ddcddf",
        "X-RapidAPI-Host": "premier-league-standings1.p.rapidapi.com"
    }
    
    primeira_headers = {
        "X-RapidAPI-Key": "1bfc62e407mshf854dedd3d74057p13aac9jsn020d982c8772",
        "X-RapidAPI-Host": "primeira-liga-standings.p.rapidapi.com"
    }
    
    premier_response = requests.get(premier_url, headers=premier_headers)
    primeira_response = requests.get(primeira_url, headers=primeira_headers)
    
    premier_data = premier_response.json()
    primeira_data = primeira_response.json()
    
    return render_template('premier.html', premier_data=premier_data, primeira_data=primeira_data)

if __name__ == '__main__':
    app.run(debug=True)
