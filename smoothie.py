# Smoothie Maker 3000 - Tryb nauczyciela
# Rozbuduj kod!

import time

# 1️⃣ LISTA OWOCÓW — dodaj tu więcej owoców
owoce = ["Banan", "Truskawka", "Jabłko"]

# 2️⃣ Funkcja pokazująca menu wyboru owoców
def pokaz_menu():
    print("\n--- WITAJ W SMOOTHIE MAKER 3000 ---")
    print("Wybierz owoce do swojego koktajlu:")
    for i, owoc in enumerate(owoce, 1):
        print(f"{i}. {owoc}")
    print("0. Zakończ wybieranie i miksuj!")

# 3️⃣ FUNKCJE MASZYNY — mozesz tu dodać efekty dźwiękowe (printy), zabawne teksty itp.

def obierz(owoc):
    print(f"Obieram {owoc.lower()}...")
    time.sleep(1)

def pokroj(owoc):
    print(f"Kroję {owoc.lower()} na kawałki...")
    time.sleep(1)

def miksuj(wybrane_owoce):
    print("Miksuję składniki...")
    for owoc in wybrane_owoce:
        time.sleep(0.5)
        print(f"Dodaję {owoc.lower()}...")
    time.sleep(1)
    print("Smoothie gotowe!")
    time.sleep(1)

def podaj():
    print("Przelewam do szklanki...")
    time.sleep(1)
    print("Smacznego! 🍹\n")

# 4️⃣ Główna funkcja maszyny
def maszyna_smoothie():
    wybrane_owoce = []

    while True:
        pokaz_menu()
        wybor = input("Wybierz numer owocu (lub 0 by zakończyć wybór): ")

        if not wybor.isdigit():
            print("⚠ Podaj numer!")
            continue

        wybor = int(wybor)

        if wybor == 0:
            break
        elif 1 <= wybor <= len(owoce):
            owoc = owoce[wybor - 1]
            wybrane_owoce.append(owoc)
            print(f"{owoc} dodany!")
        else:
            print("⚠ Nie ma takiego numeru.")

    if not wybrane_owoce:
        print("Nie wybrano owoców. Koniec.")
        return

    for owoc in wybrane_owoce:
        obierz(owoc)
        pokroj(owoc)
    
    miksuj(wybrane_owoce)
    podaj()

# START MASZYNY
maszyna_smoothie()