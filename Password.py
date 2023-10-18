import random
import string

class Password:
    def __init__(self, longitud=8):
        self.longitud = longitud
        self.contraseña = self.generarPassword()

    def generarPassword(self):
        caracteres = string.ascii_letters + string.digits
        contraseña = ''.join(random.choice(caracteres) for _ in range(self.longitud))
        return contraseña

    def esFuerte(self):
        mayusculas = 0
        minusculas = 0
        numeros = 0

        for caracter in self.contraseña:
            if caracter.isupper():
                mayusculas += 1
            elif caracter.islower():
                minusculas += 1
            elif caracter.isdigit():
                numeros += 1
        return mayusculas > 2 and minusculas > 1 and numeros > 5

    def getContraseña(self):
        return self.contraseña

    def getLongitud(self):
        return self.longitud

    def setLongitud(self, longitud):
        self.longitud = longitud
        self.contraseña = self.generarPassword()

if __name__ == "__main__":
    tamaño = int(input("Introduce la longitud de los passwords: "))
    cantidad = int(input("Introduce la cantidad de passwords: "))

    passwords = []
    es_fuerte = []

    for _ in range(cantidad):
        password = Password(tamaño)
        passwords.append(password)
        es_fuerte.append(password.esFuerte())

    for i in range(cantidad):
        print(f"Contraseña {i+1}: {passwords[i].getContraseña()} {es_fuerte[i]}")