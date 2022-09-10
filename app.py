from flask import Flask, render_template
from utils import *


app = Flask(__name__)

@app.route('/')
def index():
    candidates = load_candidates_from_json(path)
    return render_template('list.html', candidates=candidates)

@app.route('/candidate/<int:x>')
def card(x):
    candidate = get_candidate(x)
    return render_template('card.html', candidate=candidate) if candidate else '<h1>Такого кандидата нет.</h1>'

@app.route('/search/<candidate_name>')
def search(candidate_name):
    candidates = get_candidates_by_name(candidate_name)
    return render_template('search.html', candidates=candidates)

@app.route('/skill/<skill_name>')
def skill(skill_name):
    candidates = get_candidates_by_skill(skill_name)
    return render_template('skill.html', skill_name=skill_name, candidates=candidates)


app.run()