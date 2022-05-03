
import pickle
import copy



mapa = pickle.load(open("mapa.pickle", "rb"))
for element in mapa["values"]:
    print(element[1])