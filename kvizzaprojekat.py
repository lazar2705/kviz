import pygame
import random


pygame.init()

SIRINA, VISINA = 800, 600
ekran = pygame.display.set_mode((SIRINA, VISINA))
pygame.display.set_caption("Kviz")
font = pygame.font.Font(None, 40)

BIJELA = (245, 245, 245)
CRNA = (0, 0, 0)
PLAVA = (0, 0, 255)
CRVENA = (255, 0, 0)
ZELENA = (0, 255, 0)

pitanja = [
    {"pitanje": "Koji je glavni grad Francuske?", "odgovori": ["Pariz", "London", "Berlin", "Madrid"], "tacan": 0},
    {"pitanje": "Koliko iznosi (2*3)*4/2?", "odgovori": ["10", "12", "15", "11"], "tacan": 1},
    {"pitanje": "Koja je hemijska oznaka za vodu?", "odgovori": ["H2O", "CO2", "O2", "NaCl"], "tacan": 0},
    {"pitanje": "Koja je najveća planeta u Sunčevom sistemu?", "odgovori": ["Zemlja", "Mars", "Jupiter", "Saturn"], "tacan": 2},
    {"pitanje": "Ko je napisao 'Na Drini Ćuprija'?", "odgovori": ["Ivo Andrić", "Mesa Selimović", "Petar Petrović Njegoš", "Branko Ćopić"], "tacan": 0},
    {"pitanje": "Koja je formula brzine?", "odgovori": ["v = s/t", "a = v/t", "f = m*a", "E = mc^2"], "tacan": 0},
    {"pitanje": "Ko je otkrio gravitaciju?", "odgovori": ["Albert Ajnštajn", "Nikola Tesla", "Isaac Newton", "Galileo Galilej"], "tacan": 2},
    {"pitanje": "Koliko kontinenata ima na Zemlji?", "odgovori": ["5", "6", "7", "8"], "tacan": 2},
    {"pitanje": "Koja država ima najviše stanovnika?", "odgovori": ["SAD", "Indija", "Kina", "Rusija"], "tacan": 2},
    {"pitanje": "Koliko sati ima jedan dan?", "odgovori": ["12", "24", "36", "48"], "tacan": 1}
]
#dodatna pitanja za kviz:
''' {"pitanje": "Koja je najbrža životinja na svijetu?", "odgovori": ["Zec", "Gepard", "Orao", "Slon"], "tacan": 1},
    {"pitanje": "Koji je najduži riječni sistem na svijetu?", "odgovori": ["Amazon", "Nil", "Bistrica", "Misisipi"], "tacan": 0},
    {"pitanje": "Koji je simbol hemijskog elementa zlata?", "odgovori": ["Au", "Ag", "Fe", "Pb"], "tacan": 0},
    {"pitanje": "Koja je najviša planina na svijetu?", "odgovori": ["Kilimandžaro", "Everest", "Aconcagua", "Elbrus"], "tacan": 1},
    {"pitanje": "Koja država je domaćin najviše Olimpijskih igara?", "odgovori": ["SAD", "Francuska", "Crna Gora", "Japan"], "tacan": 0},
    {"pitanje": "Koji je glavni grad Italije?", "odgovori": ["Venecija", "Rim", "Milano", "Podgorica"], "tacan": 1},
    {"pitanje": "Koliko je duginih boja?", "odgovori": ["5", "6", "7", "8"], "tacan": 2},
    {"pitanje": "Koji je najpoznatiji egipatski faraon?", "odgovori": ["Ramzes II", "Tutanhamon", "Kleopatra", "Aleksandar Veliki"], "tacan": 1},
    {"pitanje": "Koja je osnovna jedinica za masu u SI sistemu?", "odgovori": ["gram", "kilogram", "ton", "dekagram"], "tacan": 1},
    {"pitanje": "Koja je osnovna jedinica za temperaturu u SI sistemu?", "odgovori": ["Celzijus", "Kelvin", "Fahrenheit", "Rankine"], "tacan": 1},
    {"pitanje": "Ko je bio prvi predsjednik SAD?", "odgovori": ["Abraham Lincoln", "George Washington", "Thomas Jefferson", "Donald Trump"], "tacan": 1},
    {"pitanje": "Koja je najpoznatija životinja u Australiji?", "odgovori": ["Koala", "Kengur", "Emu", "Dingo"], "tacan": 1},
    {"pitanje": "Koji je najpoznatiji roman Marka Tvena?", "odgovori": ["Otpisani", "Tom Sojer", "Veliki Gatsby", "Oliver Twist"], "tacan": 1},
    {"pitanje": "Koji je glavni grad Japana?", "odgovori": ["Seul", "Peking", "Tokyo", "Hong Kong"], "tacan": 2},
    {"pitanje": "Koja životinja je poznata po tome što nosi oklop?", "odgovori": ["Zmija", "Kornjača", "Delfin", "Pas"], "tacan": 1},
    {"pitanje": "Koje je najpoznatije djel Vilijama Šekspira?", "odgovori": ["Hamlet", "Romeo i Julija", "Macbeth", "Svi kraljevi"], "tacan": 1},
    {"pitanje": "Koja je najljepša životinja na svijetu?", "odgovori": ["Tigar", "Jelen", "Lav", "Jednorog"], "tacan": 0},
    {"pitanje": "Koja je najveća država na svijetu?", "odgovori": ["Kanada", "SAD", "Rusija", "Kina"], "tacan": 2},
    {"pitanje": "Koliko planeta ima u Sunčevom sistemu?", "odgovori": ["8", "9", "10", "7"], "tacan": 0},
    {"pitanje": "Koji je osnovni simbol za hemijsku supstancu vodonik?", "odgovori": ["O", "H", "He", "N"], "tacan": 1},
    {"pitanje": "Koja je najjača gravitacija u Sunčevom sistemu?", "odgovori": ["Jupiter", "Zemlja", "Saturn", "Mars"], "tacan": 0},
    {"pitanje": "Koji je simbol za element gvožđe?", "odgovori": ["Fe", "Ag", "Cu", "Pb"], "tacan": 0},
    {"pitanje": "Ko je izumio telefon?", "odgovori": ["Nikola Tesla", "Alexander Graham Bell", "Thomas Edison", "James Watt"], "tacan": 1},
    {"pitanje": "Koja je najvažnija supstanca u krvi?", "odgovori": ["Plazma", "Eritrociti", "Hemoglobin", "Leukociti"], "tacan": 2},
    {"pitanje": "Koji je glavni grad Australije?", "odgovori": ["Sidnej", "Melburn", "Kanbera", "Brisban"], "tacan": 2}
    
'''
def promijesaj_pitanja(pitanja):
    random.shuffle(pitanja)
    for p in pitanja:
        odgovori = p["odgovori"]
        tacan_odgovor = odgovori[p["tacan"]]
        random.shuffle(odgovori)
        p["tacan"] = odgovori.index(tacan_odgovor)
    return pitanja

pitanja = promijesaj_pitanja(pitanja)


def unos_korisnika():
    ime = ""
    indeks = ""
    aktivno_polje = "ime"

    while True:
        ekran.fill(BIJELA)

        tekst_ime = font.render(f"Ime: {ime}", True, PLAVA)
        tekst_indeks = font.render(f"Broj indeksa: {indeks}", True, PLAVA)
        ekran.blit(tekst_ime, (100, 150))
        ekran.blit(tekst_indeks, (100, 200))

        podsjetnik = font.render("Unesite svoje podatke (ime pa TAB, indeks pa ENTER):", True, CRVENA)
        ekran.blit(podsjetnik, (40, 100))

        pygame.display.flip()

        for dogadjaj in pygame.event.get():
            if dogadjaj.type == pygame.QUIT:
                pygame.quit()
                exit()
            if dogadjaj.type == pygame.KEYDOWN:
                if dogadjaj.key == pygame.K_RETURN:
                    if ime and indeks:
                        return ime, indeks
                elif dogadjaj.key == pygame.K_BACKSPACE:
                    if aktivno_polje == "ime":
                        ime = ime[:-1]
                    else:
                        indeks = indeks[:-1]
                elif dogadjaj.key == pygame.K_TAB:
                    aktivno_polje = "indeks" if aktivno_polje == "ime" else "ime"
                else:
                    if aktivno_polje == "ime":
                        ime += dogadjaj.unicode
                    else:
                        indeks += dogadjaj.unicode

def prikazi_pitanje(pitanje, odgovori, trenutni_rezultat):
    ekran.fill(BIJELA)    
    tekst_pitanje = font.render(pitanje, True, CRNA)
    ekran.blit(tekst_pitanje, (50, 50))

    for i, odgovor in enumerate(odgovori):
        tekst_odgovor = font.render(f"{chr(65+i)}: {odgovor}", True, CRNA)
        ekran.blit(tekst_odgovor, (100, 150 + i * 50))

    tekst_rezultat = font.render(f"Rezultat: {trenutni_rezultat}", True, PLAVA)
    ekran.blit(tekst_rezultat, (600, 400))

    pygame.display.flip()

def kviz():
    ime, indeks = unos_korisnika()
    trenutni_rezultat = 0
    for p in pitanja:
        pitanje = p["pitanje"]
        odgovori = p["odgovori"]
        tacan = p["tacan"]

        while True:
            prikazi_pitanje(pitanje, odgovori, trenutni_rezultat)
            for dogadjaj in pygame.event.get():
                if dogadjaj.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if dogadjaj.type == pygame.KEYDOWN:
                    if dogadjaj.key in [pygame.K_a, pygame.K_b, pygame.K_c, pygame.K_d]:
                        izabrano = ord(dogadjaj.unicode) - 97
                        if izabrano == tacan:
                            trenutni_rezultat += 10
                        else:
                            trenutni_rezultat -= 5
                        break
            else:
                continue
            break

    ekran.fill(BIJELA)
    tekst_rezultat = font.render(f"Rezultat za {ime} ({indeks}): {trenutni_rezultat}", True, ZELENA)
    ekran.blit(tekst_rezultat, (100, 200))

    pygame.display.flip()
    pygame.time.wait(5000)

kviz()
pygame.quit()
