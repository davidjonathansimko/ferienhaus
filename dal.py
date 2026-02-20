import json
import os

class DataAccessLayer:
    def __init__(self, datei="daten.json"):
        self.datei = datei
        self.ferienhaeuser = self._laden()

    def _laden(self):
        if os.path.exists(self.datei):
            with open(self.datei, "r") as f:
                return json.load(f)
        return {}

    def _speichern(self):
        with open(self.datei, "w") as f:
            json.dump(self.ferienhaeuser, f, indent=4)

    def hinzufuegen(self, haus_daten):
        self.ferienhaeuser[haus_daten["id"]] = haus_daten
        self._speichern()

    def abrufen(self, haus_id):
        return self.ferienhaeuser.get(haus_id)

    def aktualisieren(self, haus_id, neue_daten):
        if haus_id in self.ferienhaeuser:
            self.ferienhaeuser[haus_id] = neue_daten
            self._speichern()

    def alle_auflisten(self):
        return list(self.ferienhaeuser.values())
