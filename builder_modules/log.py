print_info = True
print_warning = True
print_debug = False
print_fatal = True

# ┃

import platform
import builder_modules.design as design
from builder_modules.core import __version__

def intro(ip, lan):
	icon = "[]"

	os = platform.system()

	# For some reason python on windows dosen't like displaying emojis in terminals.
	match os:
		case 'Windows': icon = "<>"
		case 'Linux': icon = "🚀"
		case _: icon = "<>"

	print(f"\n{design.reset}  {icon} \033[102m\033[90m builder.py {design.reset} {design.addinfo}v{design.green}{__version__}\n")
	print(f"{design.reset}  Local:   http://localhost:8080")

	if lan == True: 
		print(f"{design.reset}  Network: http://{ip}\n")
	else:
		print(f"{design.reset}  Network: {design.addinfo}use lan=True to expose{design.reset}\n")

	# Maybe add a "serving from" thing?

def info(string: str):
	if print_info == False: return
	print(f"{design.blue}{design.bold}      Info{design.reset} {string}")

def warning(string: str):
	if print_warning == False: return
	print(f"{design.yellow}{design.bold}   Warning{design.reset} {string}")

def debug(string: str):
	if print_debug == False: return
	print(f"{design.green}{design.bold}	 Debug{design.reset} {string}")

def fatal(string: str):
	if print_fatal == False: return
	print(f"{design.red}{design.bold}    Fatal{design.reset} {string}")

def error(string: str):
	if print_fatal == False: return
	print(f"{design.red}{design.bold}    Error{design.reset} {string}")

# --------------------

def found(file: str):
	print(f"{design.green}{design.bold}    Found{design.reset} {file}")

def built(file: str):
	print(f"{design.green}{design.bold}     Built{design.reset} {file}")

def copied(file: str):
	print(f"{design.green}{design.bold} Copied{design.reset} {file}")

def reload(file: str):
	print(f"{design.green}{design.bold} Reloading{design.reset} {file}")

class Loading:
	pass