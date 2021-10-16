import bcrypt

def welcome():
	print("Welcome to your dashboard")

def gainAccess(Username=None, Password=None):
    Username = input("Enter your username:")
    Password = input("Enter your Password:")
    
    if not len(Username or Password) < 1:
        if True:
            db = open("database.txt", "r")
            d = []
            f = []
            for i in db:
                a,b = i.split(",")
                b = b.strip()
                c = a,b
                d.append(a)
                f.append(b)
                data = dict(zip(d, f))
            try:
                if Username in data:
                    hashed = data[Username].strip('b')
                    hashed = hashed.replace("'", "")
                    hashed = hashed.encode('utf-8')
                    
                    try:
                        if bcrypt.checkpw(Password.encode(), hashed):
                        
                            print("Login success!")
                            print("Hi", Username)
                            welcome()
                        else:
                            print("Wrong password")
                        
                    except:
                        print("Incorrect passwords or username")
                else:
                    print("Username doesn't exist")
            except:
                print("Password or username doesn't exist")
        else:
            print("Error logging into the system")
            
    else:
        print("Please attempt login again")
        gainAccess()
		
		# b = b.strip()
# accessDb()

def register(Username=None, Password1=None, Password2=None):
    Username = input("Enter a username:")
    Password1 = input("Create password:")
    Password2 = input("Confirm Password:")
    db = open("database.txt", "r")
    d = []
    for i in db:
        a,b = i.split(",")
        b = b.strip()
        c = a,b
        d.append(a)
    if not len(Password1)<=8:
        db = open("database.txt", "r")
        if not Username ==None:
            if len(Username) <1:
                print("Please provide a username")
                register()
            elif Username in d:
                print("Username exists")
                register()		
            else:
                if Password1 == Password2:
                    Password1 = Password1.encode('utf-8')
                    Password1 = bcrypt.hashpw(Password1, bcrypt.gensalt())
                                       
                    db = open("database.txt", "a")
                    db.write(Username+", "+str(Password1)+"\n")
                    print("User created successfully!")
                    print("Please login to proceed:")

					
					# print(texts)
                else:
                    print("Passwords do not match")
                    register()
    else:
        print("Password too short")



def home(option=None):
	print("Welcome, please select an option")
	option = input("Login | Signup:")
	if option == "Login":
		gainAccess()
	elif option == "Signup":
		register()
	else:
		print("Please enter a valid parameter, this is case-sensitive")




# register(Username, Password1, Password2)
# gainAccess(Username, Password1)
home()

