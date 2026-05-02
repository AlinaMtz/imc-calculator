while True:
 peso = float(input("introduce tu peso en kg:"))
 if peso <= 0:
    print ("peso invalido")
    continue
 altura = float(input("introduce tu altura en m:"))
 if altura <= 0:
    print ("altura invalida")
    continue


 imc = peso/altura**2
 print ("tu imc es :", round(imc, 2))

 if imc < 18.5:
    print("bajo peso")
 elif 18.5 <= imc <= 24.9:
    print("peso normal")
 elif 25 <= imc <= 29.9:
    print("sobrepeso")
 elif imc >= 30:
    print("obesidad")
 else:
    print ("no se pudo calcular el imc, intente de nuevo")


 respuesta = input("¿quires calcular otro imc: (si/no)").lower (). strip ()
 if respuesta == "no": 
    print ("gracias por usar el programa") 
    exit()
 elif respuesta == "si":
        print("vamos a calcular otro IMC...")
        continue
 else:
        print("respuesta no válida, se repetirá el cálculo")



