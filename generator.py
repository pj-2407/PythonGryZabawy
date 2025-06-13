import string
import secrets

def generuj_bezpieczne_haslo(dlugosc=16, include_special=True):
    # Tworzymy zbiór znaków: małe/duże litery + cyfry
    alphabet = string.ascii_letters + string.digits
    if include_special:
        alphabet += string.punctuation

    # W pętli generujemy hasło aż spełni podstawowe warunki:
    while True:
        haslo = ''.join(secrets.choice(alphabet) for _ in range(dlugosc))
        # Sprawdzamy obecność minimum: mała, duża, cyfra
        if (any(c.islower() for c in haslo) and
            any(c.isupper() for c in haslo) and
            any(c.isdigit() for c in haslo)):
            return haslo

if __name__ == "__main__":
    for _ in range(5):
        print(generuj_bezpieczne_haslo(16))
