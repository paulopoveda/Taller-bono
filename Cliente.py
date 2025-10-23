from Node import Node
class Cliente(Node):
    def __init__(self, name, lastname, id, phone, active = True):
        self.lastname = lastname
        self.name = name
        self.id = id
        self.phone = phone
        self.active = active

    def __str__(self):
        return f"Cliente({self.name}, {self.lastname}, {self.id}, {self.id}, {self.phone}, {self.active})"

