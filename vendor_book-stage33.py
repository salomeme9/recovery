# === Stage 33: Добавь откат последнего действия там, где это разумно ===
# Project: VendorBook
class VendorBookUndoStack:
    def __init__(self):
        self._history = []
        self._max_size = 50

    def push(self, state):
        self._history.append(state)
        if len(self._history) > self._max_size:
            del self._history[0]

    def undo(self):
        if not self._history:
            return None
        return self._history.pop()
