import os
import json
from km.models.User import User

class UserController:
    
    def show_user(self, user):
        print(f"Document: {user.document}")
        print(f"Name: {user.name}")
        print(f"mail: {user.mail}")
        
    # ----------------------------------- CRUD --------------------------
    
    # Añadir Usuario
    
    def add_user(self, user):
        #pasarlo a formato json
        format = {
            "document" : user.document,
            "name" : user.name,
            "mail" : user.mail
        }
        
        #abrir archivo
        with open("data/usuarios.json", "w") as file:
            json.dump(format, file, indent=4)
        