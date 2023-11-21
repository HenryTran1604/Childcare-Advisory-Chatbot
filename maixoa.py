from colorama import Fore, Back, Style, init

# Khởi tạo Colorama
init()

# In ra một dòng màu
print(f"{Fore.RED}This is red text{Style.RESET_ALL}")

# In ra một dòng khác
print(f"{Fore.BLUE}This is blue text{Style.RESET_ALL}")
print('normal')
