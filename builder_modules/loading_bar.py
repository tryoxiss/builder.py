class LoadingBar:
    progress: int
    TOTAL: int

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

        print(f"[{'#' * int(bar_competed_characters)}{(50 - int(bar_competed_characters)) * '.'}] {round(completed_percent, 1)}%{self._up_line}")