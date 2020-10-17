# Feladat 1
# Készíts egy PostIt osztályt, amelynek van 3 tagváltozója:

# hatterszin
# szoveg (ami rajta van)
# szovegszin Készíts pár példa objektumot:
# sárga postit kék szöveggel: "Első ötlet"
# rózsaszínű postit fekete szöveggel: "Hurrá!"
# zöld postit barna szöveggel: "Szuper!"

# Feladat 2
# Készíts egy Allat osztályt
# Minden állatnak van éhsége, ami egy szám
# Minden állatnak van szomja, ami egy szám
# Amikor egy állat létrejön, 50-es az éhsége és 50-es a szomja
# Minden állat tud csinálni bizonyos dolgokat:
# eszik(), ilyenkor az éhsége csökken eggyel
# iszik(), ilyenkor a szomja csökken eggyel
# jatszik(), ilyenkor az éhsége és szomja megnő eggyel
# Feladat 3
# Másold magadhoz az elkészített Pokemon osztályt:

# class Pokemon:
#     def __init__(self,  nev, tipus, ellenfel):
#         self.nev = nev
#         self.tipus = tipus
#         self.ellenfel = ellenfel

#     def hatasos_ellene(self, masik):
#         return self.ellenfel == masik.tipus
# Illetve használd ezen programot, benne kommentként láthatod a feladatot:

# def initialize_pokemons():
#     pokemon = [];
#     pokemon.append(Pokemon("Balbasaur", "fű", "víz"))
#     pokemon.append(Pokemon("Pikatchu", "elektromos", "víz"))
#     pokemon.append(Pokemon("Charizard", "tűz", "fű"))
#     pokemon.append(Pokemon("Balbasaur", "víz", "tűz"))
#     pokemon.append(Pokemon("Kingler", "víz", "tűz"))
#     return pokemon

# ash_pokemonjai = initialize_pokemons()

# # Minden pokémonnak van neve és típusa.
# # Bizonyos tipusok hatásosak más típusokkal szemben, pl. víz hatásos tűz ellen.

# # Ash-nek van néhány pokémonja.
# # Felbukkant egy vad pokémon!

# vad_pokemon = Pokemon("Oddish", "fű", "víz")

# # Melyik pokémonját válassza Ash a küzdelemhez?

# print("..., téged választalak!")
# A class és a program kódja két különböző file-ban legyen.

# Feladat 4
# Másold magadhoz az elkészített Thing és Fleet osztályt:

# class Thing:
#     def __init__(self, name):
#         self.name = name
#         self.completed = False

#     def complete(self):
#         self.completed = True

#     def __str__(self):
#         return ("[x] " if self.completed else "[ ] ") + self.name
# class Fleet(object):
#     def __init__(self):
#         self.things = []

#     def add(self, thing):
#         self.things.append(thing)

#     def __str__(self):
#         result = ""
#         for i in range(0, len(self.things)):
#             result += str(i+1) + ". " + self.things[i].__str__() + "\n"
#         return result
# Illetve használd ezen programot, benne kommentként láthatod a feladatot:

# from fleet import Fleet
# from thing import Thing

# fleet = Fleet()

# # Töltsd fel a fleet példányt olyan módon, hogy a következő legyen a kimenet:
# # 1. [ ] Get milk
# # 2. [ ] Remove the obstacles
# # 3. [x] Stand up
# # 4. [x] Eat lunch

# print(fleet)
# A class és a program kódja két különböző file-ban legyen.

# Feladat 5
# Hozz létre diák és tanár osztályokat: Student és Teacher néven

# Student (diák)
# learn(): Kiírja a képernyőre: "A diák tanul valamit"
# question(teacher): Meghívja a tanár (teach) metódusát
# Teacher (tanár)
# teach(student): Meghívja a diák learn() metódusát
# answer(): Kiírja a képernyőre: "A tanár válaszol a diáknak"
# Program
# Hozz létre egy Student és Teacher példányt
# Hívd meg a diák question() metódusát és a tanár teach() metódusát
# Feladat 6
# Hozz létre egy töltőállomás és autó osztályt Station és Car néven.

# Station
# Tagváltozók:

# gas_amount: A töltőállomás üzemanyag szintje
# Metódusok:

# refill(car): Csökkenti a gas_amount tagváltozót az átadott autó által befogadható üzemanyag mennyiségének értékével, és megnöveli az autó gas_amount tagváltozóját a maximális értékre (teletölti)
# Car
# Tagváltozók:

# gas_amount: Az autó aktuális üzemanyag szintje
# capacity: Az autó maximális üzemanyag szintje
# Metódusok:

# Hozz létre egy konstruktort, ami beállítja a következő értékeket:

# gas_amount: 0
# capacity: 100
# Feladat 7
# Hozz létre egy filctoll és tolltartó osztályt Sharpie és SharpieSet néven.

# Sharpie
# Az osztály tárolja a filc szinét, vastagságát és tinta mennyiségét.

# A létrehozott példány tinta mennyisége legyen 100.

# Legyen egy use() metódusa ami csökkenti a tinta mennyiségét.

# SharpieSet (tolltartó)
# Az osztály filceket tárol. Egy tolltartó rendelkezzen a következő metódusokkal:

# add(sharpie): Hozzáad egy filcet
# count_usable(): Visszaadja a számát azoknak a filceknek, amikben még van tinta
# remove_trash(): Törli az üres filceket
# Feladat 8
# Farm
# Használd újra az Allat osztályt.

# Hozz létre egy Farm osztályt.

# tároljon állatokat
# tárolja, hogy maximum hány állatot tud tárolni
# Metódusok:

# breed(): létrehoz egy új állatot, ha van neki hely
# sell(): kiveszi a legkevésbé éhes állatot
# Feladat 9
# BlogPost
# Hozz létre BlogPost osztályt aminek van:

# szerző neve
# címe
# szövege
# dátuma
# Blog
# Hozz létre Blog-ot, ami képes:

# BlogPost-okat tárolni
# Hozzáadni egy új blogpostot a blogpostok listájhoz
# Törölni egy postot (index alapján)
# Megváltoztatni egyet egy másik pédányra, index alapján