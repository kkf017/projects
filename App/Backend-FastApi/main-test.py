from services.database.database import *

from services.User.UserModel import *
from services.User.UserController import *

from services.Postit.PostitModel import *
from services.Postit.PostitController import *




if __name__ == "__main__":


    #createTableUser()    
    #createTablePostit()

    #createUserController("user.test@gmail.com", "Login-Test-x00")

    x = request(f'''SELECT * FROM {TABLE_POSTIT}''')
    print(f"\nPostit {x}")

    x = request(f'''SELECT * FROM {TABLE_USER}''')
    print(f"\nUser {x}")
