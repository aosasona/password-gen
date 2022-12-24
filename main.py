import random

CHARS = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890#!@$%&*+^")

class CustomException(Exception):
    def __init__(self, message) -> None:
        self.message = message
        super().__init__(self.message)

def validate_length(length: str) -> int:
    if not length:
        raise CustomException("No input provided!")
    try:
        result = int(length)
    except Exception:
        raise CustomException(f"{length} is not a valid number!")
    return result


def generate_random_str(length: int) -> str:
    random_str = ""
    for _ in range(0, length - 1):
        random_int = random.randint(0, len(CHARS) - 1) 
        random_str += CHARS[random_int]
    return random_str
    


def main():
    try:
        app_running: bool = True
        while app_running:
            user_input = input("Desired password length or type exit to quit program: ")
            if(user_input == "exit"):
                app_running = False
                continue
            length: int = validate_length(user_input)
            password = generate_random_str(length)
            print(f"Generated password is: \n{password}\n")
    except CustomException as e:
        print(e.message)


main()
