meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "ROLF": "Una respuesta a una broma",
            "SHEESH": "Ligera desaprobacion",
            "AGGRO" : "Ponerse agresivo/enojado",
            "CREEPY": "Aterrador, siniestro",
            "XD" : "Expresion de gracia o una cara volteada"
            }

word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

if word in meme_dict.keys():
    print("El significado es:",meme_dict[word])
else:
    print("Esta palabra no esta")
