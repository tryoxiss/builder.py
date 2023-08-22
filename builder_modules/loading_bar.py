class LoadingBar:
    _progress: int
    _TOTAL: int

    _previous_length = 0

    _up_line = "\033[F"

    loaded_color = "\033[92m"
    unloaded_color = "\033[30m"
    symbol_color = "\033[37m"
    text_color = "\033[97m"

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

        print(f"{self._up_line}{self.symbol_color}[{self.loaded_color}{'#' * int(bar_competed_characters)}{self.unloaded_color}{(50 - int(bar_competed_characters)) * '.'}{self.symbol_color}] {self.text_color}{round(completed_percent, 1)}{self.symbol_color}%")
        print(f"{self.text_color}{task}{' ' * self._previous_length}{self._up_line}")

        # >= cause python jank
        if completed_percent >= 100:
            print("\033[0m") # Add a new line
        
        self._previous_length = len(task)