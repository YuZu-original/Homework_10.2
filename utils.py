import json

STYLES = """
<style>
    body {background-color: #282a36;}
    pre  {width: fit-content; padding: 20px 25px; background-color: #44475a;
          color: #f8f8f2; border-radius: 5px;}
    .user_avatar {border-radius: 10px;}
</style>"""

def load_candidates(path="candidates.json"):
    """Загрузка информации о кандидатах из json файла"""
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def make_nice_cand_content(data:dict, make_img=False):
    """Создание приятного пользовательского вида для контента"""
    content = ""

    # Если ничего нет в date
    if data is None or data == []:
        return STYLES+'''<pre>Ничего нет :(</pre>'''
    # Если дата это инфа об одном кандидате, тоесть это словарь, а не список словарей как должно быть
    if type(data) == dict:
        data = [data]
    
    for cand in data:
        content +=  '<img class="user_avatar" src="'+cand["picture"]+'">' if make_img else "" # Если нужны картинки
        content +=  "<pre>"+\
                    "Имя кандидата - "+cand["name"]+"\n"+\
                    "Позиция кандидата: "+cand["position"]+"\n"+\
                    "Навыки: "+cand["skills"]+"\n"+\
                    "</pre>"
    return STYLES+content

def get_cand_by_id(cands_info:dict, cand_id):
    """Поиск информации о студенте по его id"""
    for cand in cands_info:
        if cand["id"] == cand_id:
            return cand

def get_cands_by_skill(cands_info:dict, cand_skill:str):
    """Поиск всех студентов с таким умением"""
    cands = []
    for cand in cands_info:
        if cand_skill.strip().lower() in [skill.strip().lower() for skill in cand["skills"].split(",")]:
            cands.append(cand)
    return cands
