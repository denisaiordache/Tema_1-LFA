def lambda_moves(stari_curente):
    ok=1
    global legaturi
    while ok==1:
        ok=0
        for stare in stari_curente:
            for leg in legaturi:
                if int(leg[0])==stare and leg[1]=='$'and int(leg[2])not in stari_curente:
                    stari_curente.append(int(leg[2]))
                    ok=1
    return stari_curente

def eval(cuvant):
    global stare_initiala,stari_finale,legaturi
    stari_curente=[stare_initiala] #pornesc din starea initiala
    stari_curente=lambda_moves(stari_curente) #adaug starile in care ma pot duce cu lambda din starea initiala
    for litera in cuvant:

        stari_noi=[] #toate nodurile in care ma pot duce cu litera respectiva
        for stare in stari_curente:
            stari_litera = []  # nodurile in care ma pot duce cu litera respectiva din stare
            for leg in legaturi:
                if int(leg[0])==stare and leg[1]==litera and int(leg[2]) not in stari_litera:
                    stari_litera.append(int(leg[2]))
            stari_noi.extend(stari_litera)
        stari_curente=stari_noi
        new_list=[] #lista cu noduri din care elimin duplicatele
        for stare in stari_curente:
            if stare not in new_list:
                new_list.append(stare)
        new_list=lambda_moves(new_list) #nodurile in care ma pot duce cu lambda
        stari_curente = new_list #updatez lista cu noduri din care continui verificarea
        if len(new_list)==0: return False
    for stare in new_list:
        if stare in stari_finale:
            return True
    return False





f = open("date.in")
nr_stari = int(f.readline())
nr_caractere = int(f.readline())
alfabet = [x for x in f.readline().split()]
stare_initiala = int(f.readline())
nr_stari_finale = int(f.readline())
stari_finale = [int(x) for x in f.readline().split()]
nr_translatari = int(f.readline())
legaturi = []
for i in range(nr_translatari):
    legaturi.append(f.readline())
for i in range(len(legaturi) - 1):
    legaturi[i] = legaturi[i][:len(legaturi[i]) - 1]
if(eval("abyyxz")==True):
    print("cuvant acceptat")
else:
    print("cuvantul nu este acceptat")