# --- Gra: Kamień, Papier, Nożyce ---

# Tak jak w grze "Zgadnij Liczbę", potrzebujemy modułu 'random' do losowania.
# Tym razem będziemy losować wybór komputera.
import random

# Witamy gracza i tłumaczymy zasady.
print("--- Zagrajmy w Kamień, Papier, Nożyce! ---")
print("Wybierz jedno z trzech: kamień, papier lub nożyce.")
print("Pamiętaj: kamień tępi nożyce, nożyce tną papier, a papier owija kamień.")

# Prosimy gracza o jego wybór.
wybor_gracza = input("Twój wybór: ")

# Zamieniamy wybór gracza na małe litery, aby uniknąć problemów z wielkością liter.
wybor_gracza = wybor_gracza.lower()

# Tworzymy listę (taki pojemnik na dane) z możliwymi wyborami dla komputera.
mozliwe_wybory = ["kamień", "papier", "nożyce"]

# Komputer losuje jedną z opcji z naszej listy.
# Funkcja random.choice() losowo wybiera jeden element z podanej listy.
wybor_komputera = random.choice(mozliwe_wybory)

# Wyświetlamy wybory, aby gracz wiedział, co wybrał komputer.
# Używamy f-stringów (litera 'f' przed cudzysłowem), aby łatwo wstawiać zmienne do tekstu.
print(f"\nTy wybrałeś: {wybor_gracza}")
print(f"Komputer wybrał: {wybor_komputera}\n")

# Teraz sprawdzamy wszystkie możliwości za pomocą instrukcji warunkowych.

# Najpierw sprawdzamy, czy jest remis.
# Dzieje się tak, gdy gracz i komputer wybrali to samo.
if wybor_gracza == wybor_komputera:
    print("Remis!")

# Teraz sprawdzamy warunki, w których wygrywa gracz.
# 'elif' to skrót od 'else if', czyli "w przeciwnym razie, jeśli...".
elif (wybor_gracza == "kamień" and wybor_komputera == "nożyce") or \
     (wybor_gracza == "nożyce" and wybor_komputera == "papier") or \
     (wybor_gracza == "papier" and wybor_komputera == "kamień"):
    # Używamy 'and' (i) oraz 'or' (lub) do łączenia warunków.
    # Np. (gracz wybrał kamień I komputer wybrał nożyce) LUB (gracz wybrał nożyce I komputer wybrał papier) ...
    print("Wygrałeś! Brawo!")

# Jeśli nie ma remisu i gracz nie wygrał, to znaczy, że musiał przegrać.
# 'else' obejmuje wszystkie pozostałe przypadki.
else:
    # Dodajemy małą "sztuczkę": sprawdzamy, czy gracz wpisał poprawną opcję.
    # Jeśli nie, dajemy mu znać.
    if wybor_gracza not in mozliwe_wybory:
        print("Hmm, chyba wpisałeś coś źle. Następnym razem wybierz kamień, papier lub nożyce.")
    else:
        # Jeśli wybór gracza był poprawny, ale przegrał, wyświetlamy standardową wiadomość.
        print("Niestety, tym razem przegrałeś. Spróbuj jeszcze raz!")
