import random

def krec():
    symbole = ['🍋', '🍊', '⭐', '🍉', '🍒']
    return [random.choice(symbole) for _ in range(3)]

def wypisz(linia):
    print(" | ".join(linia))

def wyplata(linia, zaklad):
    if linia[0] == linia[1] == linia[2]:  
        if linia[0] == '🍒':
            return zaklad * 100
        
        elif linia[0] == '🍉':
            return zaklad * 50
        elif linia[0] == '⭐':
            return zaklad * 250
        elif linia[0] == '🍊':
            return zaklad * 30
        elif linia[0] == '🍋':
            return zaklad * 20
    return 0  

def main():
    balance = 100
    print("***************************")
    print("Witaj w maszynie!")
    print("Symbole: 🍋🍊⭐🍉🍒")
    print("***************************")
    
    while balance > 0:
        print(f"Obecny stan konta: ${balance}")

        zaklad = input("Postaw zakład: ")

        if not zaklad.isdigit():
            print("Wpisz tylko liczby!")
            continue

        zaklad = int(zaklad)

        if zaklad > balance:
            print("Nie masz wystarczająco pieniędzy!")
            continue

        if zaklad <= 0:
            print("Zakład musi być większy niż 0!")
            continue

        balance -= zaklad

        linia = krec()
        print("Generuje...")
        wypisz(linia)

        wygrana = wyplata(linia, zaklad)

        if wygrana > 0:
            balance += wygrana
            print(f"Wygrałeś ${wygrana}, twój balans to ${balance}!")
            
        else:
            print(f"Przegrałeś! twój balans to: ${balance}")

        if balance <= 0:
            print(f"Koniec gry! Nie masz już pieniędzy.")
            break

        zagraj_ponownie = input("Czy chcesz zagrać ponownie? (tak/nie): ")

        if zagraj_ponownie.lower() != 'tak':
            break

    print("***************************")
    print(f"Dziękujemy za grę! Twój końcowy balans to: ${balance}")
    print("***************************")

name = "name"
if name == "name":
    main()



