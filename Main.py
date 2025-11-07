from km.models.User import User
from km.models.Book import Book
from km.controllers.UserController import UserController

controller = UserController()

firstUser = User("1054862574", "Alejandro", "alejrios90@gmail.com", "alejo123")
secondUser = User("30338037", "Paulas", "paulita@gmail.com", "paulka13")

firstBook = Book("0123456789", "Holahola", "Alejandro", 40000, 1.3)

controller.add_user(firstUser)
