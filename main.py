from flask import Flask
from utils import *

app = Flask(__name__)

@app.route('/')
def index_page():
    return make_nice_cand_content(load_candidates(), make_img=False)


@app.route('/candidates/<int:cand_id>/')
def candidate_page(cand_id):
    cand = get_cand_by_id(load_candidates(), cand_id)
    return make_nice_cand_content(cand, make_img=True)


@app.route('/skills/<skill>/')
def skills_search_page(skill):
    cands = get_cands_by_skill(load_candidates(), skill)
    return make_nice_cand_content(cands, make_img=True)

if __name__ == "__main__":
    app.run(debug=True)