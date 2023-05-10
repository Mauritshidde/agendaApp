def add_user(email, username, password):
    pass

def username_exists(username_to_search):
    result = User.query.filter_by(username=username_to_search).first()
    
    return result