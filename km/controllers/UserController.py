import os
import json
from km.models.User import User

class UserController:
    
    # route = "data/users.json"
    
    def show_user(self, user):
        print(f"Document: {user.document}")
        print(f"Name: {user.name}")
        print(f"mail: {user.mail}")
        
    # ----------------------------------- CRUD --------------------------
    
    # Añadir Usuario
    
    def search_user(self, user):
        user_list = []
        
        with open("data/users.json", "r") as file:
            user_list = json.load(file)
        
        for u in user_list:
           if u['document'] == user.document:
                print("existo")
                return True
        print("no existo")
        return False   
                
           
    
    def add_user(self, new_user):
        self.search_user(new_user)
        
        #pasarlo a formato json
        format = [{
            "document" : new_user.document,
            "name" : new_user.name,
            "mail" : new_user.mail
        }]
        
        #añadir usuario
        with open("data/users.json", "w") as file:
            json.dump(format, file, indent=4)
    
    
       
        