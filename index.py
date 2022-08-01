from re import S


palavras = []
count = []
teste = []
soma = 0

song = """yeah, breakfast at tiffany's and bottles of bubbles
girls with tattoos who like getting in trouble
lashes and diamonds, atm machines
buy myself all of my favorite things (yeah)
been through some bad shit, i should be a sad bitch
who woulda thought it'd turn me to a savage?
rather be tied up with cuffs and not strings
write my own checks like i write what i sing, yeah (yeah)
my wrist, stop watchin', my neck is flossin'
make big deposits, my gloss is poppin'
you like my hair? gee, thanks, just bought it
i see it, i like it, i want it, i got it (yeah)
i want it, i got it, i want it, i got it
i want it, i got it, i want it, i got it
you like my hair? gee, thanks, just bought it
i see it, i like it, i want it, i got it (yeah)
wearing a ring, but ain't gon' be no mrs
bought matching diamonds for six of my bitches
i'd rather spoil all my friends with my riches
think retail therapy my new addiction
whoever said money can't solve your problems
must not have had enough money to solve 'em
they say: which one? i say: nah, i want all of 'em
happiness is the same price as red-bottoms
my smile is beamin', my skin is gleamin'
the way it shine, i know you've seen it (you've seen it)
i bought a crib just for the closet (just for, closet)
both his and hers, i want it, i got it, yeah
i want it, i got it, i want it, i got it
i want it, i got it, i want it, i got it (baby)
you like my hair? gee, thanks, just bought it (oh yeah)
i see it, i like it, i want it, i got it (yeah)
i got my receipts, be lookin' like phone numbers
if it aint money, then wrong number
black card is my business card
the way it be settin' the tone for me
i don't mean to brag, but i be like: put it in the bag, yeah
when you see them racks, they stacked up like my ass, yeah
shoot, go from the store to the booth
make it all back in one loop, give me the loot
never mind, i got the juice
nothing but net when we shoot
look at my neck, look at my jet
ain't got enough money to pay me respect
ain't no budget when i'm on the set
if i like it, then that's what i get, yeah
i want it, i got it, i want it, i got it (yeah)
i want it, i got it, i want it, i got it (oh yeah, yeah)
you like my hair? gee, thanks, just bought it
i see it, i like it, i want it, i got it (i want it) (yeah)"""

# Limpar
replaces = {',': '',
            '?': '',
            ')': '',
            '(': '',
            ':': '',
            '\n': ' '}
for key, value in replaces.items():
    song = song.replace(key, value)


# Separar por espaços
splited = song.split(" ")


# Adiciona na array "Palavras, as palavras apenas uma única vez"

for i in range(len(splited)):
    if splited[i] not in palavras:
        palavras.append(splited[i])
        count.append(0)

for i in range(len(splited)):
    for n in range(len(palavras)):
        if splited[i] == palavras[n]:
            count[n] = count[n] + 1

for i in range(len(palavras)):
    print(palavras[i], count[i], "\n")
