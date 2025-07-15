class User:

    def __init__(self, first_name, last_name):
        self.userFN = first_name
        self.userLN = last_name

    def prFirst_name(self):
        print(self.userFN)

    def prLast_name(self):
        print(self.userLN)

    def prAll_name(self):
        print(self.userFN, self.userLN)