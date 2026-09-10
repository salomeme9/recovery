# === Stage 42: Добавь цветной вывод через ANSI-коды с возможностью отключения ===
# Project: VendorBook
import sys

if sys.platform != "win32":
    ANSI = True
else:
    ANSI = False

if ANSI:
    GREEN = "\033[32m"
    RED = "\033[31m"
    YELLOW = "\033[33m"
    CYAN = "\033[36m"
    RESET = "\033[0m"
    def print_green(text):
        print(f"{GREEN}{text}{RESET}")
    def print_red(text):
        print(f"{RED}{text}{RESET}")
    def print_yellow(text):
        print(f"{YELLOW}{text}{RESET}")
    def print_cyan(text):
        print(f"{CYAN}{text}{RESET}")
    def print_info(text):
        print(f"{CYAN}[INFO]{RESET} {text}")
    def print_success(text):
        print(f"{GREEN}[OK]{RESET} {text}")
    def print_error(text):
        print(f"{RED}[ERR]{RESET} {text}")
    def print_warning(text):
        print(f"{YELLOW}[WARN]{RESET} {text}")
    def print_header(text):
        print(f"\n{CYAN}{'='*40}{RESET}")
        print(f"{CYAN}{text}{RESET}")
        print(f"{CYAN}{'='*40}{RESET}\n")
