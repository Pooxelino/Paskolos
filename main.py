class Paskola:
    def __init__(self, suma, terminas, palukanos):
        self.suma = suma
        self.terminas = terminas
        self.palukanos = palukanos
        self.menesis = []
        self.grazintina = 0
        self.liko = []
        self.prisk_pal = []
        self.moketi = []

    def skaiciuokle(self):
        self.grazintina = self.suma / self.terminas  # kiek mokama kas menesi
        for i in range(self.terminas):
            self.menesis.append(i + 1)  # menesio indeksas
            pal = (self.suma * (self.palukanos / 100)) / 12
            self.prisk_pal.append(round(pal, 2))
            self.suma -= self.grazintina  # kiek liko grazinti
            self.liko.append(self.suma)
            mok = self.grazintina + pal
            self.moketi.append(round(mok, 2))

    def info(self):
        print("{:<8} {:<8} {:<12} {:<12} {:<8}".format("Suma", "Terminas", "Palūkanos", "Palukanu suma", "Bendra suma"))
        print(
            "{:<8} {:<8} {:<12} {:<12} {:<8}".format(len(self.menesis) * self.grazintina, self.terminas, self.palukanos,
                                                     sum(self.prisk_pal), sum(self.moketi)))

    def grafikas(self):
        print("{:<8} {:<8} {:<12} {:<12} {:<8}".format("Mėnuo", "Dalis", "Likutis", "Palūkanos", "Suma"))
        for i in range(self.terminas):
            print("{:<8} {:<8} {:<12} {:<12} {:<8}".format(self.menesis[i], self.grazintina, self.liko[i],
                                                           self.prisk_pal[i], self.moketi[i]))

        print("{:<8} {:<8} {:<12} {:<12} {:<8}".format("Bendra:", len(self.menesis) * self.grazintina, "",
                                                       round(sum(self.prisk_pal), 2), round(sum(self.moketi), 2)))


uzklausos = []


def visos_uzklausos():
    while True:
        print("Visos paskolos: ")
        for i in range(len(uzklausos)):
            print(
                f"{i + 1} paskola: suma: {uzklausos[i][0]}, terminas: {uzklausos[i][1]}, palukanos: {uzklausos[i][2]}")
        print("1 - pasirinkti paskola redagavimui")
        print("2 - pasirinkti paskola informacijai")
        print("3 - pasirinkti paskola grafikui")
        print("4 - uzdaryti paskolu uzklausas")
        veiksmas2 = input("Pasirinkite veiksma: ")
        if veiksmas2 == "1":
            redagavimas()
        elif veiksmas2 == "2":
            info_isvedimas()
        elif veiksmas2 == "3":
            grafiko_isvedimas()
        elif veiksmas2 == "4":
            break


def redagavimas():
    eilute = int(input("pasirinkite eilute: "))
    print(uzklausos[eilute - 1][0], uzklausos[eilute - 1][1], uzklausos[eilute - 1][2])
    pirm = float(input("pakeiskite suma: "))
    antr = int(input("pakeiskite termina: "))
    trec = float(input("pakeiskite palukanas: "))
    uzklausos[eilute - 1][0] = pirm
    uzklausos[eilute - 1][1] = antr
    uzklausos[eilute - 1][2] = trec


def grafiko_isvedimas():
    eilute = int(input("pasirinkite eilute: "))
    p1 = Paskola(uzklausos[eilute - 1][0], uzklausos[eilute - 1][1], uzklausos[eilute - 1][2])
    p1.skaiciuokle()
    p1.grafikas()


def info_isvedimas():
    eilute = int(input("pasirinkite eilute: "))
    print(type(uzklausos[eilute - 1][0]), type(uzklausos[eilute - 1][1]), type(uzklausos[eilute - 1][2]))
    p1 = Paskola(uzklausos[eilute - 1][0], uzklausos[eilute - 1][1], uzklausos[eilute - 1][2])
    p1.skaiciuokle()
    p1.info()


while True:
    print("1 - iveskite paskolos duomenis")
    print("2 - rodyti visas paskola")
    print("3 - baigti darba")
    veiksmas = input("Iveskite norima veiksma: ")
    if veiksmas == "1":
        suma = float(input("Iveskite paskolos suma: "))
        ter = int(input("Iveskite termina: "))
        pal = float(input("Iveskite metines palukanas: "))
        uzklausos.append([suma, ter, pal])
    elif veiksmas == "2":
        visos_uzklausos()
    elif veiksmas == "3":
        break
    else:
        print("Tokio veiksmo nera")
