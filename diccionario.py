import time

meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "ROLF": "Una respuesta a una broma",
            "SHEESH": "Ligera desaprobacion",
            "AGGRO" : "Ponerse agresivo/enojado",
            "CREEPY": "Aterrador, siniestro",
            "XD" : "Expresion de gracia o una cara volteada"
            }

while True:
            word = input("Escribe una palabra que no entiendas ,"SALIR", para terminar el programa o "BUSCAR", para añadir nuevas palabras(¡con mayúsculas!): ").upper() #funcion para hacer que wordd sse haga en mayusculas

            if word == "SALIR":
                        print("Programa finalizado")
                        time.sleep(1)
                        break
            elif word == "AÑADIR":
                        new_word = input("Escribe la nueva palabra (¡con mayúsculas!): ").upper()
                        if new_word in meme_dict:
                                    print(new_word,"ya esta en el diccionario")
                        else:
                                    new_meaning = input(f"Escribe el significado de '{new_word}': ")
                                    meme_dict[new_word] = new_meaning
                                    print(new_word,"ha sido añadida con exito")
            elif word in meme_dict.keys():
                print("El significado es:",meme_dict[word])
            else:
                print("Esta palabra no esta")
