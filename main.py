# Wir importieren die Klassen aus den Dateien dal.py, bll.py und pl.py
from dal import DataAccessLayer
from bll import BusinessLogicLayer
from pl import PresentationLayer

def main():
    # 1. Wir erstellen die Objekte (Instanzen)
    lager = DataAccessLayer()
    logik = BusinessLogicLayer(lager)
    anzeige = PresentationLayer(logik)

    # 2. Wir rufen die Start-Methode der Anzeige auf
    anzeige.start()

if __name__ == "__main__":
    # Startet das Programm
    main()
