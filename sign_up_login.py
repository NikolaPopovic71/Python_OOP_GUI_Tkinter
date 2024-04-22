class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __str__(self):
        return "{}|{}".format(self.username, self.password)

class Users:
    def __init__(self):
        self.users_list = []

    def load_users(self):
        lines = [line.strip() for line in open('users.txt')]
        for line in lines:
            r = line.split('|')
            user = User(r[0], r[1])
            self.users_list.append(user)

    def login(self, username, password):
        for user in self.users_list:
            if user.username == username:
                if user.password == password:
                    return "Login successful"
                else:
                    return "Password incorrect"
        return "User doesn't exist!\nYou should create an account!\nPlease, sign up for an account"
    
    def sign_up(self, username, password):
        for user in self.users_list:
            if user.username == username:
                return "Username already exists! Please, try another one"
            
        user = User(username, password)
        self.users_list.append(user)
        self.update_the_users()
        return "Account successfully created"


    def update_the_users(self):
        with open('users.txt', 'w') as f:
            for user in self.users_list:
                f.write('{}|{}\n'.format(user.username, user.password))
    
        
U = Users()
U.load_users()
for user in U.users_list:
    print(user)
