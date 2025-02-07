class User:
    def __init__(self, user_name, email, password):
        self.user_name = user_name
        self._email = email
        self.user_password = password
    
    def get_email(self):
        return self._email
    
    def set_email(self,newemail):
        self.newemail = input("Enter a new Email:  ")
        return self.newemail



user1 = User("dantheman", "dan@gmail.com", "123")
print(user1.get_email())
#user1.set_email(n)
print(user1.set_email("new@gmail.com"))
