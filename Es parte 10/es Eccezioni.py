"""Creare una classe chiamata User con un attributo modificabile chiamato username. L’attributo deve essere una stringa e la sua lunghezza deve essere compresa tra 3 e 5 caratteri. Altrimenti sollevare le apposite eccezioni. """

class User:
    def __init__(self, username):
        self.username = username


    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        if type(username) is not str:
           raise TypeError("username deve essere string minchione!!")

        if len(username) <3 or len(username) >5:
            raise ValueError("username deve essere 3 e 5 caratteri minchione!!")

        self._username = username



user=User("Nigga")
print(user.username)