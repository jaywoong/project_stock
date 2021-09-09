class User:
    def __init__(self, user_id, member_password, member_name, member_email):
        self.user_id = user_id;
        self.pwd = member_password;
        self.name = member_name;
        self.email = member_email;
    def __str__(self):
        return self.user_id+' '+self.member_password+' '+self.member_name+' '+self.member_email+' ';

