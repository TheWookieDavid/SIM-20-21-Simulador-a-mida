

class Resources:

    def __init__(self):
        self.cadiresTallar = 3
        self.cadiresRentar = 2

    def AgafarCadiraRentar(self):
        if self.cadiresRentar > 0:
            self.cadiresRentar -= 1
            return self.cadiresRentar
        return self.cadiresRentar -1

    def DeixarCadiraRentar(self):
        if self.cadiresRentar <= 2:
            self.cadiresRentar += 1

    def AgafarCadiraTallar(self):
        if self.cadiresTallar > 0:
            self.cadiresTallar -= 1
            return self.cadiresTallar
        return self.cadiresTallar -1

    def DeixarCadiraTallar(self):
        if self.cadiresRentar <= 3:
            self.cadiresTallar += 1