def get_only_names(json_response):
    names = []
    for user in json_response:
        names.append(user['login'])
    return names
