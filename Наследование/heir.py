from parent import Parent


class Heir(Parent):

    def __init__(self, login, password, age):
        super().__init__(login, password)
        self.save()
        self.age = age

    def save(self):
        with open('users') as r:
            for i in r:
                if f'{self.login, self.password}'+'\n' == i:
                    raise ValueError('такой уже есть')
        super().save()

    def show(self):
        return self.login, self.password


x = Heir('Boby1', '123456789', 35)
