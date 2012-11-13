def question_list(questions):
    """ returns list of questions ready for JSON serialization """
    response = []
    
    for q in questions:        
        question = {}
        question['id'] = q.id
        question['title'] = q.title
        question['answer_count'] = q.answer_count
        question['accepted_count'] = q.accepted_count
        question['author_real_name'] = q.author.real_name
        question['author_user_name'] = q.author.username        
        response.append(question)
        
    return response
    
def user_list(users):
    """ returns list of users ready for JSON serialization """
    
    response = []
    
    for u in users:
        user = {}
        user['id'] = u.id 
        user['username'] = u.username 
        user['real_name'] = u.real_name    
        user['date_joined'] = str(u.date_joined)
        user['email'] = u.email
        user['email_isvalid'] = u.email_isvalid
        user['first_name'] = u.first_name
        user['last_name'] = u.last_name
        user['is_active'] = convert_numeric(u.is_active)
        user['is_approved'] = convert_numeric(u.is_approved)
        user['is_staff'] = convert_numeric(u.is_staff)
        user['is_superuser'] = convert_numeric(u.is_superuser)
        user['last_activity'] = str(u.last_activity)
        response.append(user)
    
    return response
    
def convert_numeric(bool_value):
    """ converts boolean to numeric value (0/1) """    
    
    if bool_value:
        return 1
    else:
        return 0