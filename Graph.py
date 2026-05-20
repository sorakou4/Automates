from graphviz import Digraph
GREEN = "\033[32m"
YELLOW = "\033[38;5;226m"
BLUE = "\033[38;5;153m"
RESET = "\033[0m"

def pref(u):
    """
    Étant donné un mot u passé en paramètre renvoie la liste des préfixes de u
    """
    result = ['']
    for i in range(len(u)):
        result.append(result[-1] + u[i])
    return result

print(f"\n{GREEN}Partie 1 Mots, langages et automates..."f"{RESET}\n")
print(f"{BLUE}Partie 1.1 Mots")
print(f"{YELLOW}Partie 1.1.1 : préfixes"f"{RESET}\n",pref('coucou'))

def suf(u):
    """
    Étant donné un mot u passé en paramètre renvoie la liste des suffixes de u"""
    result = ['']
    for i in range(len(u)-1, -1, -1):
        result.append(u[i] + result[-1])
    return result[::-1]

print(f"{YELLOW}Partie 1.1.2 : suffixes"f"{RESET}\n",suf('coucou'))

def fact(u):
    """
    Étant donné un mot u passé en paramètre renvoie la liste sans doublons des facteurs de u"""
    result = ['']
    for i in range(len(u)):
        for j in range(i+1, len(u)+1):
            result.append(u[i:j])
    return result

print(f"{YELLOW}Partie 1.1.3 : facteurs"f"{RESET}\n",fact('coucou'))

def miroir(u):
    """
    Étant donné un mot u passé en paramètre renvoie le mot miroir de u
    """
    result = ''
    for i in range(len(u)-1, -1, -1):
        result = result + u[i]
    return result

print(f"{YELLOW}Partie 1.1.4 : miroir"f"{RESET}\n",miroir('coucou'))

def concatene(L1, L2):
    """
    Étant donnés deux langages L1 et L2 renvoie le produit de concaténation (sans doublons) de L1 et L2
    """
    result = []
    for i in range(len(L1)):
        for j in range(len(L2)):
            result.append(L1[i] + L2[j])
    return result

L1 =['aa', 'ab', 'ba', 'bb']
L2 =['a','b','']

print(f"{BLUE}\nPartie 1.2 Mots")
print(f"{YELLOW}Partie 1.2.1 : concatene"f"{RESET}\n",concatene(L1, L2))

def puis(L, n):
    """
    Étant donnés un langage L et un entier n renvoie le langage L
n (sans doublons)
    """
    result = ['']
    for i in range(n):
        result = concatene(result, L)
    return result

print(f"{YELLOW}Partie 1.2.2 : puissance"f"{RESET}\n",puis(L1,2))

"""
On ne peut pas faire une fonction calculant l'étoile d'un langage 
car l'étoile d'un langage est infini
"""

def tousmots(L,n):
    """
    Étant donné un alphabet A passé en paramètre renvoie la liste de tous les mots de A∗ de longueur inférieure à n
    """
    result = []
    for i in range(1, n+1):
        result = result + puis(L, i)
        result.append('')
    return result

print(f"{YELLOW}Partie 1.2.4 : tout les mots"f"{RESET}\n",tousmots(['a', 'b'],3))


print(f"{BLUE}\nPartie 1.3 Automates")
def defauto():
    """
    Permet de faire la saisie d’un automate (sans doublon)
    Forme d'un automate : auto ={"alphabet":['a','b'],"etats": [1,2,3,4],
                                "transitions":[[1,'a',2],[2,'a',2],[2,'b',3],
                                [3,'a',4]], "I":[1],"F":[4]}
    Accepte le langage a+ba
    """
    auto = {"alphabet": [], "etats": [], "transitions": [], "I": [], "F": []}

    auto["alphabet"] = input("Entrez l'alphabet de l'automate (séparé par des virgules) : ").split(',')
    etats_input = input("Entrez les états de l'automate (séparés par des virgules) : ")
    auto["etats"] = []
    for e in etats_input.split(','):
        val = int(e)
        auto["etats"].append(val)

    n_transitions = int(input("Entrez le nombre de transitions : "))

    for _ in range(n_transitions):
        transition = input("Entrez une transition (état_source, symbole, état_destination) : ").split(',')
        auto["transitions"].append([int(transition[0]), transition[1], int(transition[2])])

    I_input = input("Entrez les états initiaux de l'automate (séparés par des virgules) : ")
    F_input = input("Entrez les états finaux de l'automate (séparés par des virgules) : ")

    auto["I"] = []
    for e in I_input.split(','):
        val = int(e)
        auto["I"].append(val)

    auto["F"] = []
    for e in F_input.split(','):
        val = int(e)
        auto["F"].append(val)
    return auto

#print(f"{YELLOW}Partie 1.3.1 : saisie d'un automate"f"{RESET}\n",defauto())

auto ={"alphabet":['a','b'],"etats": [1,2,3,4],"transitions":[[1,'a',2],[2,'a',2],[2,'b',3],[3,'a',4]], "I":[1],"F":[4]}

def lirelettre(T,E,a):
    """
    Renvoie la liste des états dans lesquels on peut arriver en partant 
    d’un état de E et en lisant la lettre a
    """
    result = []
    for e in E:
        for t in T:
            if t[0] == e and t[1] == a:
                if t[2] not in result:
                    result.append(t[2])
    return result

print(f"{YELLOW}Partie 1.3.2 : lecture d'états"f"{RESET}\n",lirelettre(auto["transitions"], auto["etats"], 'a'))

def liremot(T,E,m):
    """
    Renvoie la liste des états dans lesquels on peut arriver en partant 
    d’un état de E et en lisant le mot m
    """
    result = E
    for lettre in m:
        result = lirelettre(T, result, lettre)
    return result

print(f"{YELLOW}Partie 1.3.3 : lecture de mot"f"{RESET}\n",liremot(auto["transitions"], auto["etats"], 'aba'))

def accepte(auto, m):
    """
    Renvoie True si le mot m est accepté par l’automate
    """
    etats_atteints = liremot(auto["transitions"], auto["I"], m)
    for e in etats_atteints:
        if e in auto["F"]:
            return True
    return False

print(f"{YELLOW}Partie 1.3.4 : acceptation d'un mot dans un automate (true or false)"f"{RESET}\n",accepte(auto, 'aba'))

def langage_accept(auto, n):
    """
    Renvoie la liste des mots de longueur inférieure à n acceptés par l’automate
    """
    result = []
    mots = tousmots(auto["alphabet"], n-1)
    for i in range(n):
        for m in mots:
            if accepte(auto, m) and m not in result:
                result.append(m)
    return result

print(f"{YELLOW}Partie 1.3.5 : liste des mots de longueur inférieure à n acceptés par l’automate"f"{RESET}\n",langage_accept(auto, 6))

"""
On ne peut pas faire une fonction qui renvoie le langage accepté par un automate 
car ce langage peut parfois être infini
"""

print(f"{GREEN}\n\nPartie 2 Déterminisation"f"{RESET}\n")

def deterministe(auto):
    """
    Renvoie True si l'automate est déterministe
    """
    if len(auto["I"]) > 1:
        return False
    
    for t1 in auto["transitions"]:
        for t2 in auto["transitions"]:
            if t1 != t2 and t1[0] == t2[0] and t1[1] == t2[1]:
                return False
    return True

auto0 ={"alphabet":['a','b'],"etats": [0,1,2,3],"transitions":[[0,'a',1],[1,'a',1],[1,'b',2],[2,'a',3]], "I":[0],"F":[3]}
auto1 ={"alphabet":['a','b'],"etats": [0,1],"transitions":[[0,'a',0],[0,'b',1],[1,'b',1],[1,'a',1]], "I":[0],"F":[1]}
auto2={"alphabet":['a','b'],"etats": [0,1],"transitions":[[0,'a',0],[0,'a',1],[1,'b',1],[1,'a',1]], "I":[0],"F":[1]}

print(f"{BLUE}\nPartie 2.1 auto0 deterministe? (true or false)"f"{RESET}\n",deterministe(auto0))
print(f"{BLUE}Partie 2.1 auto2 deterministe? (true or false)"f"{RESET}\n",deterministe(auto2))

def determinise(auto):
    """
    Déterminise l’automate passé en paramètre
    """
    etat_initial = sorted(auto["I"])
    
    etats_a_traiter = [etat_initial]
    etats_deja_vus = []
    transitions_finales = []
    final_finales = []

    while etats_a_traiter:
        courant = etats_a_traiter.pop(0)
        etats_deja_vus.append(courant)

        for e in courant:
            if e in auto["F"]:
                final_finales.append(courant)
                break

        for lettre in auto["alphabet"]:
            suivant = sorted(lirelettre(auto["transitions"], courant, lettre))
            
            if suivant:
                transitions_finales.append([courant, lettre, suivant])

                if suivant not in etats_deja_vus and suivant not in etats_a_traiter:
                    etats_a_traiter.append(suivant)
    
    return {
        "alphabet": auto["alphabet"],
        "etats": etats_deja_vus,
        "transitions": transitions_finales,
        "I": [etat_initial],
        "F": final_finales
    }

print(f"{BLUE}\nPartie 2.2 determinise"f"{RESET}\n",determinise(auto2))

def renommage(auto):
    """
    Étant donné un automate passé en paramètre renomme ses états avec les premiers entiers
    """
    dico = {}

    for i in range(len(auto["etats"])):
        dico[str(auto["etats"][i])] = i
    
    nouveaux_etats = list(range(len(auto["etats"])))
    nouvelles_transitions = []
    nouveaux_I = []
    nouveaux_F = []

    for t in auto["transitions"]:
        nouvelles_transitions.append([dico[str(t[0])], t[1], dico[str(t[2])]])

    for i in auto["I"]:
        nouveaux_I.append(dico[str(i)])

    for f in auto["F"]:
        nouveaux_F.append(dico[str(f)])

    return {
        "alphabet": auto["alphabet"],
        "etats": nouveaux_etats,
        "transitions": nouvelles_transitions,
        "I": nouveaux_I,
        "F": nouveaux_F
    }

print(f"{BLUE}\nPartie 2.3 renommage + determinise"f"{RESET}\n",renommage(determinise(auto2)))

auto3 ={"alphabet":['a','b'],"etats": [0,1,2,],"transitions":[[0,'a',1],[0,'a',0],[1,'b',2],[1,'b',1]], "I":[0],"F":[2]}

def complet(auto):
    """
    Étant donné un automate passé en paramètre renvoie True s’il est complet et False sinon
    """
    for e in auto["etats"]:
        for a in auto["alphabet"]:
            # On vérifie si on peut lire la lettre 'a' depuis l'état 'e'
            if lirelettre(auto["transitions"], [e], a) == []:
                return False
    return True


print(f"{GREEN}\n\nPartie 3  Complémentation"f"{RESET}\n")

print(f"{BLUE}\nPartie 3.1 complet ? (true or false)"f"{RESET}\n",complet(auto0))
print(f"{BLUE}Partie 3.1 complet ? (true or false)"f"{RESET}\n",complet(auto1))

def complete(auto):
    """
    Complète l’automate passé en paramètre en ajoutant un état puits
    """
    if complet(auto):
        return auto

    nouveau_auto = {
        "alphabet": list(auto["alphabet"]),
        "etats": list(auto["etats"]),
        "transitions": list(auto["transitions"]),
        "I": list(auto["I"]),
        "F": list(auto["F"])
    }

    puits = max(nouveau_auto["etats"]) + 1
    nouveau_auto["etats"].append(puits)

    for e in auto["etats"]:
        for a in auto["alphabet"]:
            if lirelettre(auto["transitions"], [e], a) == []:
                nouveau_auto["transitions"].append([e,a,puits])

    for a in auto["alphabet"]:
        nouveau_auto["transitions"].append([puits,a,puits])
        
    return nouveau_auto

print(f"{BLUE}\nPartie 3.2 complete "f"{RESET}\n",complete(auto0))

def complement(auto):
    """
    Étant donné un automate passé en paramètre acceptant un langage L 
    renvoie un automate acceptant le complement L¯
    """
    a = determinise(auto)
    a = renommage(a)
    a = complete(a)

    nouveaux_F = []
    for e in a["etats"]:
        if e not in a["F"]:
            nouveaux_F.append(e)

    return {
        "alphabet": a["alphabet"],
        "etats": a["etats"],
        "transitions": a["transitions"],
        "I": a["I"],
        "F": nouveaux_F
    }

print(f"{BLUE}\nPartie 3.3 complement "f"{RESET}\n",complement(auto3))


auto4 ={"alphabet":['a','b'],"etats": [0,1,2,],"transitions":[[0,'a',1],[1,'b',2],[2,'b',2],[2,'a',2]], "I":[0],"F":[2]}

auto5 ={"alphabet":['a','b'],"etats": [0,1,2],"transitions":[[0,'a',0],[0,'b',1],[1,'a',1],[1,'b',2],[2,'a',2],[2,'b',0]],"I":[0],"F":[0,1]}


def inter(auto1, auto2):
    """
    Étant donnés deux automates déterministes auto1 et auto2
    renvoie l'automate produit acceptant l'intersection L1 ∩ L2
    """
    alphabet = auto1["alphabet"]

    I = [(auto1["I"][0], auto2["I"][0])]

    etats = []
    transitions = []
    F = []

    a_traiter = [I[0]]

    while a_traiter:
        courant = a_traiter.pop(0)

        if courant not in etats:
            etats.append(courant)

        # si les deux composantes sont finales donc état final
        if courant[0] in auto1["F"] and courant[1] in auto2["F"]:
            if courant not in F:
                F.append(courant)
                

        for a in alphabet:

            # trouver la destination dans auto1
            dest1 = []
            for t in auto1["transitions"]:
                if t[0] == courant[0] and t[1] == a:
                    dest1.append(t[2])

            # trouver la destination dans auto2
            dest2 = []
            for t in auto2["transitions"]:
                if t[0] == courant[1] and t[1] == a:
                    dest2.append(t[2])

            # les deux automates sont déterministes donc une seule destination
            if dest1 != [] and dest2 != []:
                nouveau = (dest1[0], dest2[0])

                transitions.append([courant, a, nouveau])

                if nouveau not in etats and nouveau not in a_traiter:
                    a_traiter.append(nouveau)

    return {
        "alphabet": alphabet,
        "etats": etats,
        "transitions": transitions,
        "I": I,
        "F": F
    }
    
print(f"{GREEN}\n\nPartie 4  Automate produit"f"{RESET}\n")
print(f"{BLUE}\nPartie 4.1 : intersection"f"{RESET}\n",inter(auto4, auto5,))
print(f"{BLUE}\nPartie 4.1 : renommage + intersection"f"{RESET}\n",renommage(inter(auto4,auto5)))

def difference(auto1, auto2):
    """
    Étant donnés deux automates déterministes auto1 et auto2
    renvoie l'automate produit acceptant L1\L2.
    Les automates sont complétés avant le produit.
    """
    A = complete(auto1)
    B = complete(auto2)

    alphabet = A["alphabet"]

    I = [(A["I"][0], B["I"][0])]

    etats = []
    transitions = []
    F = []

    a_traiter = [I[0]]

    while a_traiter:
        courant = a_traiter.pop(0)

        if courant not in etats:
            etats.append(courant)

        # état final si l'automate 1 accepte et que l'automate 2 n'accepte pas
        if courant[0] in A["F"] and courant[1] not in B["F"]:
            if courant not in F:
                F.append(courant)

        for a in alphabet:

            dest1 = []
            for t in A["transitions"]:
                if t[0] == courant[0] and t[1] == a:
                    dest1.append(t[2])

            dest2 = []
            for t in B["transitions"]:
                if t[0] == courant[1] and t[1] == a:
                    dest2.append(t[2])

            if dest1 != [] and dest2 != []:
                nouveau = (dest1[0], dest2[0])

                transitions.append([courant, a, nouveau])

                if nouveau not in etats and nouveau not in a_traiter:
                    a_traiter.append(nouveau)

    return {
        "alphabet": alphabet,
        "etats": etats,
        "transitions": transitions,
        "I": I,
        "F": F
    }

print(f"{BLUE}\nPartie 4.2 : Différence"f"{RESET}\n",difference(auto4,auto5))

print(f"{BLUE}\nPartie 4.2 : renommage + différence"f"{RESET}\n",renommage(difference(auto4,auto5)))


#TD4 exercice3
auto_exo3 ={"alphabet":['a','b'],"etats":[1,2,3,4,5],"transitions":[[1,'a',1],[1,'a',2],[2,'b',3],[2,'a',5],[3,'b',3],[3,'a',4],[5,'b',5]],"I":[1],"F":[4,5]}

def prefixe(auto):
    """
    Renvoie un automate acceptant l'ensemble des préfixes des mots de L
    """
    atteints = []
    a_traiter = list(auto["I"])

    while a_traiter:
        e = a_traiter.pop(0)
        if e not in atteints:
            atteints.append(e)
            for t in auto["transitions"]:
                if t[0] == e and t[2] not in atteints:
                    a_traiter.append(t[2])

    return {
        "alphabet": auto["alphabet"],
        "etats": auto["etats"],
        "transitions": auto["transitions"],
        "I": auto["I"],
        "F": atteints
    }

def suffixe(auto):
    """
    Renvoie un automate acceptant l'ensemble des suffixes des mots de L
    """
    inv = []
    for t in auto["transitions"]:
        inv.append([t[2], t[1], t[0]])

    initiaux = []
    a_traiter = list(auto["F"])

    while a_traiter:
        e = a_traiter.pop(0)
        if e not in initiaux:
            initiaux.append(e)
            for t in inv:
                if t[0] == e and t[2] not in initiaux:
                    a_traiter.append(t[2])

    return {
        "alphabet": auto["alphabet"],
        "etats": auto["etats"],
        "transitions": auto["transitions"],
        "I": initiaux,
        "F": auto["F"]
    }

def facteur(auto):
    """
    Renvoie un automate acceptant l'ensemble des facteurs des mots de L
    """

    # États atteignables depuis l'état initial
    atteignables = []
    a_traiter = list(auto["I"])

    while a_traiter:
        e = a_traiter.pop(0)
        if e not in atteignables:
            atteignables.append(e)
            for t in auto["transitions"]:
                if t[0] == e and t[2] not in atteignables:
                    a_traiter.append(t[2])

    # États pouvant atteindre un final
    auto_suf = suffixe(auto)
    vers_finaux = auto_suf["I"]

    # Intersection = nouveaux états initiaux
    nouveaux_I = []
    for e in auto["etats"]:
        if e in atteignables and e in vers_finaux:
            nouveaux_I.append(e)

    # États finaux = ceux qui peuvent atteindre un final
    return {
        "alphabet": auto["alphabet"],
        "etats": auto["etats"],
        "transitions": auto["transitions"],
        "I": nouveaux_I,
        "F": vers_finaux
    }

def miroir_a(auto):
    """
    Renvoie un automate acceptant l'ensemble des miroirs des mots de L
    """
    inv = []
    for t in auto["transitions"]:
        inv.append([t[2], t[1], t[0]])

    auto_inv = {
        "alphabet": auto["alphabet"],
        "etats": auto["etats"],
        "transitions": inv,
        "I": auto["F"],
        "F": auto["I"]
    }

    return determinise(auto_inv)

print(f"{GREEN}\n\nPartie 5  Propriétés de fermeture"f"{RESET}\n")
print(f"{BLUE}\nPartie 5.1 : suffixe"f"{RESET}\n",suffixe(auto_exo3))
print(f"{BLUE}\nPartie 5.2 : prefixe"f"{RESET}\n",prefixe(auto_exo3))
print(f"{BLUE}\nPartie 5.3 : facteur"f"{RESET}\n",facteur(auto_exo3))
print(f"{BLUE}\nPartie 5.4 : miroir"f"{RESET}\n",miroir_a(auto_exo3),"\n")


auto6 ={"alphabet":['a','b'],"etats": [0,1,2,3,4,5],"transitions":[[0,'a',4],[0,'b',3],[1,'a',5],[1,'b',5],[2,'a',5],[2,'b',2],[3,'a',1],[3,'b',0],[4,'a',1],[4,'b',2],[5,'a',2],[5,'b',5]],"I":[0],"F":[0,1,2,5]}


def dessine(auto, nom="automate"):
    """
    Dessine un automate sous forme de graphe avec Graphviz.
    https://graphviz.org/download/
    """

    g = Digraph(name=nom, format="png")
    g.attr(rankdir="LR")

    # style des états (avec couleurs cuz why not(✿◡‿◡) )
    for e in auto["etats"]:
        est_initial = e in auto["I"]
        est_final = e in auto["F"]

        if est_initial and est_final:
            g.node(str(e), shape="doublecircle", style="filled", fillcolor="#d28eff") # initial + final  
        elif est_initial:
            g.node(str(e), shape="circle", style="filled", fillcolor="#8e92ff") # initial
        elif est_final:
            g.node(str(e), shape="doublecircle", style="filled", fillcolor="#ff8e8e") # final
        else:
            g.node(str(e), shape="circle", style="filled", fillcolor="#7A7A7A") # autre état

    # état initial
    for i in auto["I"]:
        g.node("start_"+str(i), shape="point")
        g.edge("start_"+str(i), str(i))

    # transitions
    for t in auto["transitions"]:
        src, a, dst = t
        g.edge(str(src), str(dst), label=a)

    # export au format png
    g.render(filename=nom, cleanup=True)
    print(f"Automate dessiné sous le nom '{nom}.png'")


#dessine(auto_exo3, "auto_exo3")
#dessine(prefixe(auto_exo3), "prefixe_auto_exo3")
#dessine(suffixe(auto_exo3), "suffixe_auto_exo3")
#dessine(facteur(auto_exo3), "facteur_auto_exo3")
#dessine(miroir_a(auto_exo3), "miroir_auto_exo3")

print(f"{GREEN}\n\nPartie 6  Minimisation"f"{RESET}\n")



auto6 ={"alphabet":['a','b'],"etats": [0,1,2,3,4,5],"transitions":[[0,'a',4],[0,'b',3],[1,'a',5],[1,'b',5],[2,'a',5],[2,'b',2],[3,'a',1],[3,'b',0],[4,'a',1],[4,'b',2],[5,'a',2],[5,'b',5]],"I":[0],"F":[0,1,2,5]}

def sep(auto):
    """ Crée la classe de départ de niveau 0 sous 
    forme de liste de liste (séparer les états finaux 
    des non finaux) """
    finaux = []
    non_finaux = []
    niv0 = []
    
    # On parcours chaque états de l'automate
    for e in auto["etats"]:
        
        # Si l'état est final
        if e in auto["F"]:
            finaux.append(e)
            
        # Si l'état n'est pas final
        else:
            non_finaux.append(e)
            
    niv0.append(finaux)
    niv0.append(non_finaux)
    
    return niv0

print(f"{YELLOW}\ntest 1 : séparation"f"{RESET}\n",sep(auto6))

def indice_classe(etat,niv):
    """ Renvoie l'indice de classe de niveau 'niv' de l'état """
    
    for i in range(len(niv)):
        if etat in niv[i]:
            return i

    return None


def decoupe(auto,niv):
    """ Pour chaque niveau, on découpe en classe """
    
    new_niv = []
    
    for classes in niv:
        groupe_classe = {}
        for e in classes:
            destination = []
            for a in auto["alphabet"]:
                etat_a = lirelettre(auto["transitions"], [e], a)
                
                # etat_a : un seul état car automate déterministe et complet
                i_classe = indice_classe(etat_a[0],niv)
                destination.append(i_classe)
            
            dest = tuple(destination)
            
            if dest not in groupe_classe:
                groupe_classe[dest] = []
                   
            groupe_classe[dest].append(e)
        
        for s_classe in groupe_classe.values():
            new_niv.append(s_classe)
            
    return new_niv

print(f"{YELLOW}\ntest 2 : découpe"f"{RESET}\n",decoupe(auto6,sep(auto6)))

def minimise(auto):
    """ Application de l'algorithme de moore sur l'automate auto """
    
    # Initialisation du niveau 0
    niveau = sep(auto)
    
    while True:
        niveau_suivant = decoupe(auto,niveau)
        if niveau == niveau_suivant:
            break
        niveau = niveau_suivant
    
    auto_m = {
        "alphabet": auto["alphabet"],
        "etats": niveau,
        "transitions": [],
        "I": [],
        "F": []
    }
    
    # Boucle pour vérifier les ajouts des états initaux et finaux à l'automate
    for classe in auto_m["etats"]:
        initial = False
        for e in classe:
            if e in auto["I"]:
                initial = True
        
        if initial :
            auto_m["I"].append(classe)
        
        final = False
        for e in classe:
            if e in auto["F"]:
                final = True
                
        if final :
            auto_m["F"].append(classe)
            
        # Création des transitions 
        etat = classe[0]
        for a in auto["alphabet"]:
            destination = lirelettre(auto["transitions"],[etat],a)[0]
            
            classe_destination = niveau[indice_classe(destination,niveau)]
            auto_m["transitions"].append([classe, a, classe_destination])

    return auto_m    

print(f"{BLUE}\nPartie 6 (test final) : minimise "f"{RESET}\n",renommage(minimise(auto6)))
print(f"{BLUE}\nPartie 6 (test final) : Renommage + minimise "f"{RESET}\n",renommage(minimise(auto6)))


auto_determinisation = {"alphabet":['a','b'],"etats": [1,2,3],"transitions":[[1,'b',2],[1,'b',3],[2,'a',2],[2,'b',2],[2,'a',3],[3,'a',1],[3,'a',3]],"I":[1,2],"F":[3]}

auto_produit_A1 = {"alphabet":['a','b'],"etats": [0,1,2,3],"transitions":[[0,'b',1],[0,'a',3],[1,'a',2],[1,'b',3],[2,'a',2],[2,'b',2],[3,'a',3],[3,'b',3]],"I":[0],"F":[2]}
auto_produit_A2 = {"alphabet":['a','b'],"etats": [0,1,2,3],"transitions":[[0,'b',0],[0,'a',1],[1,'a',1],[1,'b',2],[2,'b',0],[2,'a',1],[3,'a',1],[3,'b',2]],"I":[0],"F":[3]}

auto_minimisation = {"alphabet":['a','b'],"etats": [1,2,3,4,5,6,7],"transitions":[[1,'b',2],[1,'a',4],[2,'a',3],[2,'b',7],[3,'a',2],[3,'b',5],[4,'a',7],[4,'b',7],[5,'b',6],[5,'a',7],[6,'b',5],[6,'a',7],[7,'a',5],[7,'a',6],[7,'b',7]],"I":[1],"F":[1,2,4,7]}


print("________\n",determinise(auto_determinisation),"\n")

print(inter(auto_produit_A1,auto_produit_A2),"\n")

print(minimise(auto_minimisation),"\n")

dessine(determinise(auto_determinisation),"Auto_determinisation")

