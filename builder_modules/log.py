_green = "\033[92m"
_yellow = "\033[93m"
_blue = "\033[96m"
_red = "\033[91m"

_bold = "\033[1m"
_reset = "\033[0m"

print_info = True
print_warning = True
print_debug = False
print_fatal = True

# ┃

def info(string: str):
    if print_info == False: return
    print(f"{_blue}{_bold}      Info{_reset} {string}")

def warning(string: str):
    if print_warning == False: return
    print(f"{_yellow}{_bold}   Warning{_reset} {string}")

def debug(string: str):
    if print_debug == False: return
    print(f"{_green}{_bold}     Debug{_reset} {string}")

def fatal(string: str):
    if print_fatal == False: return
    print(f"{_red}{_bold}     Fatal{_reset} {string}")

def error(string: str):
    if print_fatal == False: return
    print(f"{_red}{_bold}     Error{_reset} {string}")

# --------------------

def found(file: str):
    print(f"{_green}{_bold}     Found{_reset} {file}")

def built(file: str):
    print(f"{_green}{_bold}     Built{_reset} {file}")

def copied(file: str):
    print(f"{_green}{_bold}    Copued{_reset} {file}")

def reload(file: str):
    print(f"{_green}{_bold} Reloading{_reset} {file}")

class Loading:
    pass