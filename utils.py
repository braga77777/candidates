import json

path = 'candidates.json'

def load_candidates_from_json(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.loads(f.read())

def get_candidate(candidate_id):
    candidates = load_candidates_from_json(path)
    for c in candidates:
        if c['id'] == candidate_id:
            return c
    return False

def get_candidates_by_name(candidate_name):
    candidates = load_candidates_from_json(path)
    return [c for c in candidates if candidate_name.lower() in c['name'].lower()]


def get_candidates_by_skill(skill_name):
    candidates = load_candidates_from_json(path)
    return [c for c in candidates if skill_name.lower() in c['skills'].lower().split(', ')]
