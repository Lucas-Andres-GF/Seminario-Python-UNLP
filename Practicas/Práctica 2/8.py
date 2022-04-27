frase = input("Ingrese una frase para verificar: ").upper().replace(" ","")
puntos =0
for c in frase : 
    match c :
        case "A"|"E"|"I"|"O"|"U"|"L"|"N"|"R"|"S"|"T": 
            puntos += 1
        case "D"|"G":
            puntos += 2
        case "B"|"C"|"M"|"P": 
            puntos += 3
        case "F"|"H"|"V"|"W"|"Y":
            puntos += 4
        case "K":
            puntos += 5
        case "J"|"X":
            puntos += 8
        case "Q"|"Z":
            puntos += 10
print(puntos)

