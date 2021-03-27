while True:
    key=input("Ingrese el codigo para la sustitución: ")
    lista1=[]
    for i in key:
        lista1.append(i.lower())
    lista1=sorted(lista1)
    abecedario="abcdefghijklmnopqrstuvwxyz"
    lista2=[]
    for i in abecedario:
        lista2.append(i)
    if lista1!=lista2:
        print("1")
        break
    pl=input("plaintext: ")
    ci=""
    for i in pl:
        if i.isalpha():
            if i.islower():
                index=lista2.index(i)
                c=""
                c+=key[index]
                ci+=c.lower()
            else:
                index=lista2.index(i.lower())
                c=""
                c+=key[index]
                ci+=c.upper()
        else:
            ci+=i
    print("ciphertext: ",ci)
    print("0")