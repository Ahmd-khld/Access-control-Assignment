import speech_recognition as sr

recognizer = sr.Recognizer()


def speech_recognize():
    with sr.Microphone() as source:
        print("Clearing noise....")
        recognizer.adjust_for_ambient_noise(source)
        print("Listening...")
        audio_data = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio_data)
            return text

        except sr.UnknownValueError:
            print("Hmm, I'm not sure how to respond to that.")

        except sr.RequestError as e:
            print("Error: Could not request results from Google Speech Recognition service;")


users = {
    "admin": {"password": "admin123", "role": "admin",
              "command": {"create user", "delete user", "edit user profile", "reset user password", "view all users",
                          "manage permissions", "generate report", "audit log", "view security alert",
                          "update system settings",
                          "access control", "view system status", "backup data", "restore data", "delete data",
                          "approve user requests", "set security policies", "manage network settings",
                          "logout all users", "logout"}},
    "user": {"password": "user123", "role": "user",
             "command": {"login", "view profile", "edit profile", "change password",
                         "view alert", "search data", "download data", "submit request", "logout"}}
}


def check_access(user, password):
    if user in users and users[user]["password"] == password:
        return users[user]["role"]
    else:
        return None


def main():
    not_end = True
    while not_end:
        username = input("Enter Username: ")
        password = input("Enter Password: ")
        role = check_access(username, password)
        if role:
            print(f"Access for {role}")
            while True:
                command = speech_recognize()
                print(f"You Said: {command}")
                if command:
                    if command.lower() == "exit":
                        print("Thanks for using the app")
                        not_end = False
                        break
                    if role == "admin":
                        if command in users["admin"]["command"]:
                            print(f"{command} is being executed...")
                        else:
                            print("Not known Command")
                    elif role == "user":
                        if command in users["user"]["command"]:
                            print(f"{command} is being executed...")
                        else:
                            print("Not known command")
        else:
            print("denied access.....Try Again")


main()
