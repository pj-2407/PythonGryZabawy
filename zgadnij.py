# --- Gra: Zgadnij Liczbę ---

# Aby komputer mógł wylosować liczbę, musimy zaimportować (dodać) specjalny moduł o nazwie 'random'.
# Moduł to taki zestaw gotowych narzędzi, których możemy używać w naszym kodzie.
import random

# Komputer losuje jedną liczbę całkowitą z przedziału od 1 do 100.
# Funkcja randint() oznacza "losuj liczbę całkowitą" (z ang. random integer).
# Wynik losowania zapisujemy w zmiennej o nazwie 'sekretna_liczba'.
sekretna_liczba = random.randint(1, 100)

# Tworzymy zmienną, która będzie liczyć, ile prób podjął gracz.
# Na początku ustawiamy ją na 0, bo gracz jeszcze nie zgadywał.
liczba_prob = 0

# Dajemy graczowi znać, co ma zrobić.
print("Cześć! Pomyślałem sobie liczbę od 1 do 100.")
print("Spróbuj ją odgadnąć w jak najmniejszej liczbie prób.")

# Zaczynamy pętlę 'while True'. To oznacza, że kod wewnątrz pętli
# będzie się powtarzał w nieskończoność, dopóki jej nie przerwiemy.
# Przerwiemy ją, gdy gracz odgadnie liczbę.
while True:
    # Prosimy gracza o podanie liczby. Funkcja input() zawsze zwraca tekst (string).
    # Zapisujemy odpowiedź gracza w zmiennej 'odpowiedz_gracza'.
    odpowiedz_gracza = input("Jaka to liczba? ")

    # Musimy sprawdzić, czy gracz na pewno wpisał liczbę.
    # Metoda isdigit() sprawdza, czy tekst składa się tylko z cyfr.
    if odpowiedz_gracza.isdigit():
        # Jeśli tak, zamieniamy tekst na prawdziwą liczbę całkowitą (integer).
        # Robimy to za pomocą funkcji int(). Bez tego nie moglibyśmy porównywać liczb.
        zgadywana_liczba = int(odpowiedz_gracza)

        # Zwiększamy licznik prób o 1 przy każdej próbie odgadnięcia.
        # 'liczba_prob += 1' to skrót od 'liczba_prob = liczba_prob + 1'.
        liczba_prob += 1

        # Teraz używamy instrukcji warunkowych (if, elif, else), żeby porównać liczbę gracza z sekretną liczbą.
        if zgadywana_liczba < sekretna_liczba:
            # Jeśli liczba gracza jest za mała, podpowiadamy mu.
            print("Za mało! Spróbuj podać większą liczbę.")
        elif zgadywana_liczba > sekretna_liczba:
            # 'elif' to skrót od 'else if' (w przeciwnym razie, jeśli).
            # Jeśli liczba gracza jest za duża, też mu podpowiadamy.
            print("Za dużo! Spróbuj podać mniejszą liczbę.")
        else:
            # 'else' wykonuje się, gdy żaden z powyższych warunków (if, elif) nie jest prawdziwy.
            # Oznacza to, że gracz odgadł liczbę!
            print(f"Brawo! Zgadłeś! Ta liczba to {sekretna_liczba}.")
            print(f"Udało Ci się to w {liczba_prob} próbach.")

            # Używamy instrukcji 'break', aby wyjść z pętli 'while'.
            # To kończy grę.
            break
    else:
        # Jeśli gracz nie wpisał liczby (np. wpisał "hej" albo "pięć"),
        # informujemy go o błędzie i pętla zaczyna się od nowa, prosząc o podanie liczby.
        print("To nie jest liczba! Proszę, wpisz liczbę.")

