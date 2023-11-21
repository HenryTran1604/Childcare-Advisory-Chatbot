from colorama import init, Style, Fore
init()

def user_print(text):
    print(f'\033[1A{Fore.CYAN}{text}{Style.RESET_ALL}\033[K')

def chatbot_print(str):
    print(f'{Fore.GREEN}{str}{Style.RESET_ALL}')

def options_print(str):
    print(f'{Fore.MAGENTA}{str}{Style.RESET_ALL}')