CYAN_COLOR="\033[36;1m"
RED_COLOR="\033[31;1m"
BLUE_COLOR="\033[34;1m"
VIOLET_COLOR="\033[35;1m"
NO_COLOR="\033[0m"

def display_msg(msg, type="info"):
    match(type):
        case 'info': print(f"{CYAN_COLOR}{msg}{NO_COLOR}")
        case 'warning': print(f"{BLUE_COLOR}{msg}{NO_COLOR}")
        case 'danger': print(f"{RED_COLOR}{msg}{NO_COLOR}")
        case '04X': print(f"{VIOLET_COLOR}{msg:04X}{NO_COLOR}")
        case _: print(msg)