class LoadingBar:
    progress: int
    TOTAL: int

    _previous_length = 0

    _up_line = "\033[F"

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

    def __print(self, *, task="<Unknown>"):
        completed_percent = (self.progress * 100 / self.total)
        bar_competed_characters = round(completed_percent / 2, 0)

        if completed_percent == 0:
            print("")

        print(f"{self._up_line}[{'#' * int(bar_competed_characters)}{(50 - int(bar_competed_characters)) * '.'}] {round(completed_percent, 1)}%")
        print(f"{task}{' ' * self._previous_length}{self._up_line}")

        # >= cause python jank
        if completed_percent >= 100:
            print("") # Add a new line
        
        self._previous_length = len(task)