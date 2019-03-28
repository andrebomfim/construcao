import re, random
from pprint import pprint

letra_original = '''Amou daquela vez como se fosse a última
Beijou sua mulher como se fosse a última
E cada filho seu como se fosse o único
E atravessou a rua com seu passo tímido
Subiu a construção como se fosse máquina
Ergueu no patamar quatro paredes sólidas
Tijolo com tijolo num desenho mágico
Seus olhos embotados de cimento e lágrima
Sentou pra descansar como se fosse sábado
Comeu feijão com arroz como se fosse um príncipe
Bebeu e soluçou como se fosse um náufrago
Dançou e gargalhou como se ouvisse música
E tropeçou no céu como se fosse um bêbado
E flutuou no ar como se fosse um pássaro
E se acabou no chão feito um pacote flácido
Agonizou no meio do passeio público
Morreu na contramão atrapalhando o tráfego
Amou daquela vez como se fosse o último
Beijou sua mulher como se fosse a única
E cada filho seu como se fosse o pródigo
E atravessou a rua com seu passo bêbado
Subiu a construção como se fosse sólido
Ergueu no patamar quatro paredes mágicas
Tijolo com tijolo num desenho lógico
Seus olhos embotados de cimento e tráfego
Sentou pra descansar como se fosse um príncipe
Comeu feijão com arroz como se fosse o máximo
Bebeu e soluçou como se fosse máquina
Dançou e gargalhou como se fosse o próximo
E tropeçou no céu como se ouvisse música
E flutuou no ar como se fosse sábado
E se acabou no chão feito um pacote tímido
Agonizou no meio do passeio náufrago
Morreu na contramão atrapalhando o público
Amou daquela vez como se fosse máquina
Beijou sua mulher como se fosse lógico
Ergueu no patamar quatro paredes flácidas
Sentou pra descansar como se fosse um pássaro
E flutuou no ar como se fosse um príncipe
E se acabou no chão feito um pacote bêbado
Morreu na contramão atrapalhando o sábado
'''

letra_original_complemento = '''Por esse pão pra comer, por esse chão pra dormir
A certidão pra nascer e a concessão pra sorrir
Por me deixar respirar, por me deixar existir, Deus lhe pague
Pela cachaça de graça que a gente tem que engolir
Pela fumaça e a desgraça, que a gente tem que tossir
Pelos andaimes pingentes que a gente tem que cair,
Deus lhe pague
Pela mulher carpideira pra nos louvar e cuspir
E pelas moscas bicheiras a nos beijar e cobrir
E pela paz derradeira que enfim vai nos redimir, Deus lhe pague'''

lista_letra_original = letra_original.split('\n')


def coleta_proparoxitonas():
        padrao_proparoxitona = re.compile('\s[\so|a|um\s]*?\w+\n')
        global proparoxitonas
        proparoxitonas = re.findall(padrao_proparoxitona, letra_original)
        proparoxitonas = [str(p).replace('\n','') for p in proparoxitonas]


def limpa_proparoxitonas():
    global letra_sem_proparoxitonas
    letra_sem_proparoxitonas = list()
    for n in range(len(lista_letra_original) - 1):
        letra_sem_proparoxitonas.append(lista_letra_original[n].replace(proparoxitonas[n], ''))


def recompoe_letra():
    global letra_nova
    letra_nova = list()
    for verso in letra_sem_proparoxitonas:
        casa_verso(verso)
    letra_nova = '\n'.join(letra_nova) + '\n' + letra_original_complemento


def casa_verso(verso):
    proparoxitona = random.choice(proparoxitonas)
    if verso.endswith('s') and proparoxitona.endswith('s'):
        proparoxitonas.remove(proparoxitona)
        letra_nova.append(str(verso) + proparoxitona)
    elif not verso.endswith('s') and not proparoxitona.endswith('s'):
        proparoxitonas.remove(proparoxitona)
        letra_nova.append(str(verso) + proparoxitona)
    else:
        casa_verso(verso)


def reconstrucao():
    coleta_proparoxitonas()
    limpa_proparoxitonas()
    recompoe_letra()
    pprint(letra_nova)


if __name__ == '__main__':
    reconstrucao()
