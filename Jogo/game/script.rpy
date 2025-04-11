define k = Character("Kingfire")
image Kingfire normal = "King_normal.png"
image Kingfire happy = "King_happy.png"
image Kingfire angry = "King_angry.png"
transform zoom_centro:
    zoom 1.5
    xalign 0.5
    yalign 1.0
label start:
    image fundo1 = 'fundo1.png'
    scene fundo1
    'Que manhã linda na cidade de Takukunavara, tão bela que você até esqueceu seu nome...'
    $ jogador = ''
    while jogador.strip() == '':
        $ jogador = renpy.input('Qual seu nome?')
    
    $ jogador = jogador.strip()

    'Beleza, então seu nome é [jogador], né?'

    menu:
        'Tá correto isso?'

        'Sim':
            'Ok, que mal gosto.'
            'Mas vamos lá então!'

        'Não':
            'Ok, então escolha novamente!'
            $ jogador = ''
            while jogador.strip() == '':
                $ jogador = renpy.input('Qual seu nome?')
            'Agora sim! ainda tá ruim mas serve, bora começar.'
    
    $ jogador = jogador.strip()

jump p1

label p1:
    scene fundo1
    'Caraca, aquele não é o aluno novo que está vindo ali?'
    show Kingfire normal at zoom_centro
    k 'Eai grande, como cê tá? sou o aluno novo mano, vim diretamente do brasil, tudo bem com você?'

    menu:
        "Como você está?"

        'Bem':
            show Kingfire happy at zoom_centro
            k "Ai sim mano, dale!"

        'Mal':
            show Kingfire angry at zoom_centro
            k "Oloco cara, o que que rolou?!"

            menu:
                "O que houve?"

                "Minha mãe me bateu":
                     k "Caraca véi ai é foda kk, ser filho de japonês não é fácil."

                "Nada":
                    show Kingfire normal at zoom_centro
                    k "Ah então tá bom mas qualquer coisa pode falar comigo."
    show Kingfire normal at zoom_centro
    k "E qual é seu nome em, você ainda não me disse."
    k "Ah é [jogador]? legal, combina com você."

return
