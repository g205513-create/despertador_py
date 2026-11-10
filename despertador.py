import tkinter as ctk
import time
import winsound


alarme_ativo = True
codigo_alarme = "1234" 

while alarme_ativo:
    codigo_digitado = input("Digite o codigo para desativar o alarme: ")

    if codigo_digitado == codigo_alarme:
        print("Alarme desligado.")
        winsound.PlaySound(None, 0)
        alarme_ativo = False

        print("Codigo incorreto. O alarme continua tocando.")
        winsound.PlaySound(
            "alarme.wav",
            winsound.SND_FILENAME | winsound.SND_LOOP | winsound.SND_ASYNC,
        )
