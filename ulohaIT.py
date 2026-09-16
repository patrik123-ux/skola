def vytvor_kosik():
    # Slovník, ktorý už predbežne obsahuje nejaké počiatočné veci a ich ceny
    kosik = {
        "chlieb": 1.49,
        "mlieko": 0.99,
        "maslo": 2.20,
        "káva": 5.49
    }

    print("Vitajte v nákupnom košíku!")
    print("V košíku už nejaké položky máš. Môžeš pridávať ďalšie.")
    print("Ak chceš skončiť a vidieť súčet, napíš do názvu 'koniec'.\n")

    # Ukážeme, čo už v košíku aktuálne je
    print("Aktuálny obsah košíka:")
    for polozka, cena in kosik.items():
        print(f"- {polozka}: {cena:.2f} €")
    print("-" * 30)

    while True:
        # Získame názov položky od používateľa
        polozka = input("Zadaj názov novej položky (alebo 'koniec'): ").strip()

        # Ak používateľ napíše koniec, cyklus prerušíme
        if polozka.lower() == "koniec":
            break

        # Ochrana pred prázdnym vstupom
        if not polozka:
            print("Názov položky nemôže byť prázdny. Skúste znova.")
            continue

        try:
            # Získame cenu položky a pretypujeme ju na desatinné číslo (float)
            cena = float(input(f"Zadajte cenu pre '{polozka}' v €: "))
            
            if cena < 0:
                print("Cena nemôže byť záporná. Skúste znova.")
                continue

            # Pridanie alebo aktualizácia položky do slovníka (dictionary)
            kosik[polozka] = cena
            print(f"-> Do košíka bolo pridané: {polozka} ({cena:.2f} €)\n")

        except ValueError:
            print("Neplatná cena! Zadajte prosím číslo (napr. 1.50).\n")

    # --- VÝPIS KOŠÍKA A FINÁLNEJ CENY ---
    print("\n" + "=" * 30)
    print("       VÁŠ FINÁLNY KOŠÍK       ")
    print("=" * 30)

    if not kosik:
        print("Váš košík je prázdny.")
    else:
        # Prechádzame slovník pomocou metódy .items()
        for polozka, cena in kosik.items():
            print(f"- {polozka}: {cena:.2f} €")

        # Výpočet celkovej sumy pomocou funkcie sum() a hodnôt v slovníku
        celkova_cena = sum(kosik.values())
        print("-" * 30)
        print(f"CELKOVÁ CENA: {celkova_cena:.2f} €")
        print("=" * 30)

# Spustenie programu
if __name__ == "__main__":
    vytvor_kosik()