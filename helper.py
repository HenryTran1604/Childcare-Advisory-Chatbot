from colorama import init, Style, Fore
init()

username ='>>> TÔI   : '
chatbot = ">>>CHATBOT: "

def user_print(text):
    print(f'\033[1A{Fore.CYAN}{username}{text}{Style.RESET_ALL}\033[K')

def chatbot_print(str):
    print(f'{Fore.GREEN}{chatbot}{str}{Style.RESET_ALL}')

def chatbot_print2(str):
    print(f'{Fore.GREEN}{" " * 12}{str}{Style.RESET_ALL}')

def options_print(str):
    print(f'{Fore.MAGENTA}{" " * 9}{str}{Style.RESET_ALL}')