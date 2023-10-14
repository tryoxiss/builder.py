# This file makes use of classes to organise variables. That is why they are lowercase.

import platform

os = platform.system()

match os:
	case 'Windows': OS_PATH_DELIMINATOR = '\\'
	case _: OS_PATH_DELIMINATOR = '/'

class content:
	directory: str = "content"
	extensions: list[str] = [".md"]

class components:
	directory: str = "components"
	extensions: list[str] = [".htcl"]

class output:
	directory: str  = "target"
	exclude_tags: list[str] = ["#exclude", "#draft"]

	always_inline: bool = True
	prefer_figures: bool = True

	# syntax_stylesheets: dict = {
	# 	"resources":
	# 	{
	# 		"styles":
	# 		{
	# 			Tokens.STRONG: "strong.css"
	# 		}
	# 	}
	# }

# class verification:
# 	validate_html5: bool = False

max_recursion = 64