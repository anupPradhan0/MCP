"""
Simple in-memory Task store. Uses instance-level list so each TaskStore
is independent (no shared state across instances).
"""


class TaskStore:
    def __init__(self):
        self._tasks = []  # instance-level: each store has its own list

    def add_task(self, title: str) -> dict:
        """Add a task. Returns the created task with id."""
        task_id = len(self._tasks) + 1
        task = {"id": task_id, "title": title, "done": False}
        self._tasks.append(task)
        return task

    def get_tasks(self) -> list:
        """Return all tasks."""
        return list(self._tasks)

    def get_task(self, index: int) -> dict | None:
        """Get task by 0-based index. Returns None if out of range."""
        if 0 <= index < len(self._tasks):
            return self._tasks[index]
        return None

    def get_task_by_id(self, task_id: int) -> dict | None:
        """Get task by id. Returns None if not found."""
        for t in self._tasks:
            if t["id"] == task_id:
                return t
        return None

    def remove_task(self, index: int) -> bool:
        """Remove task by 0-based index. Returns True if removed."""
        if 0 <= index < len(self._tasks):
            self._tasks.pop(index)
            return True
        return False

    def remove_task_by_id(self, task_id: int) -> bool:
        """Remove task by id. Returns True if removed."""
        for i, t in enumerate(self._tasks):
            if t["id"] == task_id:
                self._tasks.pop(i)
                return True
        return False

    def toggle_done(self, index: int) -> bool:
        """Toggle done flag by index. Returns True if updated."""
        if 0 <= index < len(self._tasks):
            self._tasks[index]["done"] = not self._tasks[index]["done"]
            return True
        return False
