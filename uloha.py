ovocie = ["jablko", "banán", "hruška", "pomaranč", "hrozno"]
zelenina = ["mrkva", "brokolica", "špenát", "cibuľa", "paprika"]
saldkosti = ["čokoláda", "cukríky", "koláč", "zmrzlina", "med"]

nakupny_kosik = [jablko, mrkva, čokoláda]
ceny = {"jablko": 1, "banán": 0.5, "hruška":2, "pomaranč": 1, "hrozno":3, "mrkva": 0.8, "brokolica": 1.2, "špenát": 2, "cibuľa": 0.6, "paprika": 1.5, "čokoláda": 2, "cukríky": 1, "koláč": 3, "zmrzlina": 4, "med": 5}

while True:
    print("co chcete pridat do kosika?")
    vstup = input()
    if vstup == "uz nic":
        break
    else:
        if vstup in ovocie or vstup in zelenina or vstup in saldkosti:
            nakupny_kosik.append(vstup)
            print(f"{vstup} bol pridany do kosika.")
        else:
            print(f"{vstup} nie je v ponuke.")