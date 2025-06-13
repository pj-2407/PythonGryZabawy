# --- Gra: Przygoda Tekstowa "Zaginiony Klucz" ---

# Zaczynamy od przywitania gracza i wprowadzenia go w historię.
print("--- Zaginiony Klucz ---")
print("Budzisz się w dziwnym, kamiennym pokoju. Nie pamiętasz, jak tu trafiłeś.")
print("Na przeciwległej ścianie widzisz dwoje drzwi: jedne czerwone, a drugie niebieskie.")
print("Obok Ciebie na podłodze leży mała, metalowa skrzynka.")

# Prosimy gracza o podjęcie pierwszej decyzji.
# Odpowiedź zapisujemy w zmiennej 'wybor1'.
wybor1 = input("Co robisz? (wpisz 'drzwi' lub 'skrzynka') ")

# Używamy metody .lower(), aby zamienić wszystkie litery w odpowiedzi gracza na małe.
# Dzięki temu nie ma znaczenia, czy gracz wpisze "Drzwi", "DRZWI" czy "drzwi" - program zawsze to zrozumie.
if wybor1.lower() == "skrzynka":
    # Ten blok kodu wykona się, jeśli gracz wybrał skrzynkę.
    print("\nPodchodzisz do skrzynki. Jest zamknięta na kłódkę.")
    print("Wygląda na to, że potrzebujesz klucza.")
    # Po zbadaniu skrzynki, gracz musi wrócić do poprzedniego wyboru.
    print("Wracasz na środek pokoju. Przed Tobą wciąż są czerwone i niebieskie drzwi.")
    wybor1 = "drzwi" # Ustawiamy wybór na "drzwi", aby gra mogła iść dalej.

# Ten blok kodu wykona się, jeśli gracz wybrał drzwi (od razu lub po sprawdzeniu skrzynki).
if wybor1.lower() == "drzwi":
    print("\nStoisz przed drzwiami.")
    wybor_drzwi = input("Które wybierasz? (wpisz 'czerwone' lub 'niebieskie') ")

    if wybor_drzwi.lower() == "czerwone":
        # Wybór czerwonych drzwi.
        print("\nOstrożnie otwierasz czerwone drzwi. Skrzypią głośno.")
        print("Za drzwiami jest mały, zakurzony pokój. Na stole leży lśniący, srebrny klucz.")
        print("Wygląda na to, że to jest klucz do skrzynki!")
        print("Zabierasz klucz i wracasz do pierwszego pokoju.")

        # Pytamy gracza, co chce zrobić z kluczem.
        wybor_klucz = input("Co teraz robisz? (wpisz 'otwórz skrzynkę') ")

        if wybor_klucz.lower() == "otwórz skrzynkę":
            print("\nUżywasz klucza, aby otworzyć skrzynkę. Pasuje idealnie!")
            print("W środku znajdujesz wielkie, złote drzwi, które materializują się na ścianie obok.")
            print("Otwierasz je i wychodzisz na zewnątrz, na słoneczną polanę.")
            print("Gratulacje! Uciekłeś z pokoju! KONIEC GRY.")
        else:
            print("\nPostanowiłeś nie otwierać skrzynki i zostałeś w pokoju na zawsze. KONIEC GRY.")

    elif wybor_drzwi.lower() == "niebieskie":
        # Wybór niebieskich drzwi - to zła ścieżka.
        print("\nOtwierasz niebieskie drzwi. Za nimi jest tylko ciemność.")
        print("Gdy robisz krok do przodu, podłoga się pod Tobą zapada!")
        print("Spadasz w nieskończoność... KONIEC GRY.")
    else:
        # Jeśli gracz wpisze coś innego niż 'czerwone' lub 'niebieskie'.
        print("\nStoisz w niezdecydowaniu tak długo, że zapadasz w sen i nigdy się nie budzisz. KONIEC GRY.")
else:
    # Jeśli gracz na samym początku wpisze coś innego niż 'drzwi' lub 'skrzynka'.
    print("\nNie wiesz, co zrobić, więc siadasz na podłodze. Zostajesz tam na zawsze. KONIEC GRY.")
