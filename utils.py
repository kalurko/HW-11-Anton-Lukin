import json

def load_candidates():
    with open('candidates.json', 'r', encoding='utf-8') as file:
        return json.load(file)


def get_all():
    '''возвращает список всех кандидатов'''
    return load_candidates()


def get_candidate_by_id(id):
    '''возвращает одного кандидата по его id'''
    for candidate in load_candidates():
        if candidate['id'] == id:
            return candidate
    return "Не найден"


def get_candidate_by_name(name):
    '''возвращает кандидатов по имени'''
    result = []
    for candidate in load_candidates():
        if name.lower() in candidate['name'].lower():
            result.append(candidate)
    return result


def get_by_skill(skill):
    '''возвращает кандидатов по навыку'''
    result = []
    for candidate in load_candidates():
        if skill.lower() in candidate['skills'].lower().split(', '):
            result.append(candidate)
    return result

