class LoadingBar:
    _progress: int
    _TOTAL: int

    _previous_length = 0

    _up_line = "\033[F"

    loaded_color = "\033[92m"
    unloaded_color = "\033[37m"
    symbol_color = "\033[37m"
    text_color = "\033[97m"

    begin_symbol = "["
    end_symbol = "]"
    loaded_symbol = "#"
    unloaded_symbol = "_"

    def __init__(self, required_progress: int, first_task):
        self.progress = 0
        self.total = required_progress

        self.__print(task=first_task)
    
    def load(self, task):
        """
        Increments the number of completed tasks, and re-prints the loading
        bar with the new provided task.
        """
        self.progress += 1
        self.__print(task=task)

    def __print(self, task="<Unknown>"):
        completed_percent = (self.progress * 100 / self.total)
        bar_competed_characters = round(completed_percent / 2, 0)

        if completed_percent == 0:
            print("\033[0m")

        bar_start = f"{self._up_line}{self.symbol_color}{self.begin_symbol}{self.loaded_color}"
        bar_progress = f"{self.loaded_symbol * int(bar_competed_characters)}{self.unloaded_color}{(50 - int(bar_competed_characters)) * self.unloaded_symbol}"
        bar_end = f"{self.symbol_color}{self.end_symbol}"
        bar_percentage = f"{self.text_color}{round(completed_percent, 1)}{self.symbol_color}%"
        bar_current_task = f"{self.text_color}{task}{' ' * self._previous_length}{self._up_line}"

        print(f"{bar_start}{bar_progress}{bar_end} {bar_percentage}")
        print(f"{bar_current_task}")

        # >= cause python jank
        if completed_percent >= 100:
            print("\033[0m") # Add a new line
        
        self._previous_length = len(task)