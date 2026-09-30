import random

def guardado():
    with open ("passwd.txt", "a", encoding="utf-8") as archivo:
        archivo.write(passwd+ "\n")
        print("Contraseña guardada")

passwd=""
char=""
letras = (
    "a","b","c","d","e","f","g","h","i","j",
    "k","l","m","n","o","p","q","r","s","t",
    "u","v","w","x","y","z")
numeros = ("0","1","2","3","4","5","6","7","8","9")
mix=letras+numeros
print("##########################")
print(" generardor de contraseña")
print("##########################")
print("")
print("")
print("")
print("")
lenght = int(input("De que longitud va a ser la constraseña: "))


#tipo de contraseña
print("Que va a contener la contraseña")
typepasswd = int(input("1: solo letras. 2: letras y numeros.: "))

#generacion de la contraseña
if typepasswd == 1:
    i=0
    while i<lenght:
        char = letras[random.randint(0, len(letras) - 1)]
        passwd=passwd+char
        i+=1
    print(f"La contraseña generada es: {passwd}")
else:
    i=0
    while i<lenght:
        char = mix[random.randint(0, len(mix) - 1)]
        passwd=passwd+char
        i+=1
    print(f"La contraseña generada es: {passwd}")

#guardar contraseña en un fichero
print("Desea guardar la contraseña en un fichero de texto: Y/N")
save = input("")

while save.upper() == "Y" or save.upper() == "N":
    if save == "Y":
        guardado()
    else:
         break
    break