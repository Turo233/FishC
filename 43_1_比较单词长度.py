class Word(str):
    def __str__(self):
        try:
            return str(self.split(' ', 1)[0])
        except:
            return str(self)
    def __lt__(self, other):
        if len(str(self)) < len(str(other)):
            return True
        else:
            return False
    def __eq__(self, other):
        if len(str(self)) == len(str(other)):
            return True
        else:
            return False
    def __gt__(self, other):
        if len(str(self)) > len(str(other)):
            return True
        else:
            return False
    
a = Word('Hell')
b = Word('NO')
c = Word('ac d')
