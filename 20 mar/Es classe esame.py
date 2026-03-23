class CEsame:
    def __init__(self, nome_esame, voto_primo_parziale, voto_secondo_parziale):
        self.nome_esame = nome_esame
        self.voto_primo_parziale = voto_primo_parziale
        self.voto_secondo_parziale = voto_secondo_parziale

    def _calcola_media(self):
        media=(self.voto_primo_parziale + self.voto_secondo_parziale)/2
        return media

    def stampa_voto_finale(self):
        voto_finale = self._calcola_media()
        print("Il voto finale per l'esame ", self.nome_esame, " è ", voto_finale)



Esame_matetica=CEsame("Matematica", 17, 25)
Esame_matetica.stampa_voto_finale()


