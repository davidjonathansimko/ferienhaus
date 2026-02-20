class BusinessLogicLayer:
    def __init__(self, dal_objekt):
        self.dal = dal_objekt

    def haus_erstellen(self, h_id, name, ort, preis, kapazitaet):
        if self.dal.abrufen(h_id):
            return False, "Fehler: ID existiert bereits!"
        neues_haus = {
            "id": h_id, "name": name, "ort": ort,
            "preis_pro_nacht": preis, "kapazitaet": kapazitaet,
            "verfuegbarkeit": True
        }
        self.dal.hinzufuegen(neues_haus)
        return True, "Haus erfolgreich angelegt."

    def buchen(self, h_id):
        haus = self.dal.abrufen(h_id)
        if haus and haus["verfuegbarkeit"]:
            haus["verfuegbarkeit"] = False
            self.dal.aktualisieren(h_id, haus)
            return True, "Buchung erfolgreich!"
        return False, "Buchung fehlgeschlagen."

    def stornieren(self, h_id):
        haus = self.dal.abrufen(h_id)
        if haus and not haus["verfuegbarkeit"]:
            haus["verfuegbarkeit"] = True
            self.dal.aktualisieren(h_id, haus)
            return True, "Stornierung erfolgreich!"
        return False, "Stornierung nicht möglich."

    def hole_freie_haeuser(self):
        return [h for h in self.dal.alle_auflisten() if h["verfuegbarkeit"]]
