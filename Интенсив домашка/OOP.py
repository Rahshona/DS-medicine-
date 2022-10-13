class User:
    count = 0

    def __init__(self, name, login, password):
        self._name = name
        self._login = login
        self._password = password
        User.count += 1

    @property   #Позволяет читать
    def name(self):
        return self._name

    @name.setter #Позволяет изменять
    def name(self, value):
        self._name = value

    @property #Позволяет только читать
    def login(self):
        return self.login

    def set_password(self, value): #Позволяет только изменять с нижним проперти тоже
        self._password = value

    _password = property(fset=set_password)

    def show_info(self):
        return f'Name - {self._name}, login - {self.login}'


class SuperUser(User):
    count = 0

    def __init__(self, name, login, password, role):
        super().__init__(name, login, password)
        self._role = role
        SuperUser.count += 1

    @property  # Позволяет читать
    def role(self):
        return self._role

    @role.setter  # Позволяет изменять
    def role(self, value):
        self._role = value

    def show_info(self):
        return super().show_info(), 'role', self._role




u1 = User("Rose", 'RoseMs', '12345')
