def register():
    username = input("Choose username: ")
    password = input("Choose password: ")
    with open("users.txt", "a") as f:
        f.write(f"{username},{password}\n")
    print("Registered successfully!")
    return username

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    with open("users.txt", "r") as f:
        for line in f:
            u, p = line.strip().split(",")
            if u == username and p == password:
                print("Login successful!")
                return username
    print("Invalid credentials.")
    return None
