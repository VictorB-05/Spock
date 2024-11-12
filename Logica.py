class logica():
    puntosJ = 0
    puntoscpu = 0
    def ganaCpu(self):
        self.puntoscpu+=1

    def ganaJ(self):
        self.puntosJ+=1

    def fin(self):
        if self.puntosJ>=5 or self.puntoscpu>=5 :
            return True
        else:
            return False

    def ganar(self):
        if self.puntosJ>=5:
            return True
        else:
            return False

    def __str__(self):
        return f"{self.puntosJ} - {self.puntoscpu}"