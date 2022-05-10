import json

STYLES = """
<style>
    body {background-color: #282a36;}
    pre  {width: fit-content; padding: 20px 25px; background-color: #44475a;
          color: #f8f8f2; border-radius: 5px;}
    .user_avatar {border-radius: 10px;}
</style>"""

def load_candidates(path="candidates.json"):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def make_nice_cand_content(data:dict, make_img=False):
    content = ""
    print(data)
    if data is None or data == []:
        return STYLES+'''<pre>Таких у нас нет! Но мы их купим  >:)</pre>'''
    if type(data) == dict:
        data = [data]
    
    for cand in data:
        content +=  '<img class="user_avatar" src="'+cand["picture"]+'">' if make_img else ""
        content +=  "<pre>"+\
                    "Имя кандидата - "+cand["name"]+"\n"+\
                    "Позиция кандидата: "+cand["position"]+"\n"+\
                    "Навыки: "+cand["skills"]+"\n"+\
                    "</pre>"
    return STYLES+content

def get_cand_by_id(cands_info:dict, cand_id):
    for cand in cands_info:
        if cand["id"] == cand_id:
            return cand

def get_cands_by_skill(cands_info:dict, cand_skill:str):
    cands = []
    for cand in cands_info:
        if cand_skill.strip().lower() in [skill.strip().lower() for skill in cand["skills"].split(",")]:
            cands.append(cand)
    return cands
