from Cliente import Cliente
from listasdoblementeenlazadas import listasdoblementeenlazadas
id = 0
list = listasdoblementeenlazadas()
def registrar_cliente(self, name, lastname, phone):
    nuevo_cliente = Cliente(name, lastname, phone, id)
    list.append(nuevo_cliente)
    print("cliente{name} {lastname} con telefono: {phone} e id: {id} fue registrado exitosamente")    
    id += 1
    
def eliminar_cliente(self, id):
    

while True:
    print("1. registrar un cliente")
    print("2. listar cliente")
    print("3. eliminar cliente")

    op = input()
    if op == "1":
        name = input("ingrese el nombre del cliente: ")
        lastname = input("ingrese el apellido del cliente: ")
        phone = input("ingrese el telefono del cliente: ")
        registrar_cliente(name, lastname, phone)
    elif op == "2":
    elif op == "3":

    
