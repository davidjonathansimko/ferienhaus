class PresentationLayer:
    def __init__(self, bll_objekt):
        # Die Anzeige bekommt Zugriff auf die Logik (BLL)
        self.bll = bll_objekt

    def start(self):
        while True:
            print("\n--- FERIENHAUS MANAGER ---")
            print("1. Haus hinzufügen")
            print("2. Haus suchen")
            print("3. Haus aus Liste wählen & buchen")
            print("4. Stornieren")
            print("5. Beenden")

            wahl = input("Ihre Wahl: ")

            if wahl == "1":
                hid = input("ID: ")
                n = input("Name: ")
                o = input("Ort: ")
                p = float(input("Preis: "))
                k = int(input("Kapazität: "))
                ok, msg = self.bll.haus_erstellen(hid, n, o, p, k)
                print(msg)

            elif wahl == "2":
                hid = input("ID suchen: ")
                haus = self.bll.dal.abrufen(hid)
                print(haus if haus else "Nicht gefunden.")

            elif wahl == "3":
                # Wir holen die Liste der freien Häuser
                freie = self.bll.hole_freie_haeuser()
                if not freie:
                    print("Keine Häuser verfügbar.")
                    continue

                # Wir zeigen sie nummeriert an
                for i, h in enumerate(freie, 1):
                    print(f"{i}. {h['name']} ({h['ort']}) - {h['preis_pro_nacht']}€")

                auswahl = input("Nummer wählen (oder Enter): ")
                if auswahl.isdigit():
                    idx = int(auswahl) - 1
                    if 0 <= idx < len(freie):
                        # Wir buchen über die ID des gewählten Hauses
                        ok, msg = self.bll.buchen(freie[idx]["id"])
                        print(msg)

            elif wahl == "4":
                hid = input("ID zum Stornieren: ")
                ok, msg = self.bll.stornieren(hid)
                print(msg)

            elif wahl == "5":
                print("Programm beendet.");
                break
