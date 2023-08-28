'''Programa que toca uma música animada ou tranquila dependendo do sentimento descrito, a decisão de qual música será tocada é realizada através de um machine learning que identifica o sentimento digitado e descobre a qual animosidade ele se refere. 

Disclaimer: para que o programa funcione devidamente, é necessário que antes sejam instalados os módulos "requests" e "pygame" respectivamente através dos comandos "pip install requests" e "pip install pygame" através do terminal, um de cada vez e sem as aspas'''
import requests
import pygame

def classify(text):
    key = '67f12690-e86d-11ed-b347-b1685cefd6c738f30ac5-8c48-4fad-a1f4-1a7da04d3352'
    url = 'https://machinelearningforkids.co.uk/api/scratch/'+ key + '/classify'

    response = requests.get(url, params={ 'data' : text })

    if response.ok:
        responseData = response.json()
        topMatch = responseData[0]
        return topMatch
    else:
        response.raise_for_status()

pygame.init()
print()
repeat = True

while repeat:
    sentimento = input('Olá! Como você está se sentindo? ')
    demo = classify(sentimento)

    label = demo['class_name']

    if label == 'Sofrencia':
        pygame.mixer.music.load('triste.mp3')
    elif label == 'Festa':
        pygame.mixer.music.load('feliz.mp3')
    else:
        print('Não consegui identificar seu sentimento :(')

    pygame.mixer.music.play()
    
    quest = input('\nDeseja testar novamente? (Caso escolha uma opção válida, a música atual será interrompida)\nDigite "s" para "sim" ou "n" para "não":')
    print()

    while quest != 's' and quest != 'n':
        quest = input('Opção inválida! Digite "s" caso queira testar novamente ou "n" encerrar: ')
        print()

    
    if quest == 's':
        repeat = True
    else:
        repeat = False
    
pygame.event.wait()