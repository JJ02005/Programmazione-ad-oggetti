"""Se il login è sbagliato solleva delle eccezioni"""

class AuthError(Exception):
    pass

class UsernameError(AuthError):
    pass

class PasswordError(AuthError):
    pass



class CLoginSystem:
    def __init__(self, username, password):
        self.username = username
        self.password = password

        def login(self, username, password):
            if username != self.username:
                raise UsernameError("Username non trovato.")

            if password != self.password:
                raise PasswordError("Password incorretta.")

                return True



    class CLoginManager:
        def __init__(self, login_system):
            self._login_system = login_system

        def login_da_tastiera(self):
            username = input("inserisci l'username ")
            password = input ("inserisci la password ")
            self._login_system.login(username, password)

        login_system = CLoginSystem("lala", "m14p4sw0rd")
        login_manager = CLoginManager(login_system)
        login_manager.login_da_tastiera()