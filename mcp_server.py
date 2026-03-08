"""
MCP server for the Todo app. Exposes tools so Cursor (or any MCP client) can list, add, remove, and toggle tasks.

Run for Cursor: use stdio (Cursor starts this script and talks via stdin/stdout).
To test with MCP Inspector: mcp run mcp_server.py (then connect to the shown URL).
"""

from mcp.server.fastmcp import FastMCP

from task import TaskStore

mcp = FastMCP("Todo MCP", json_response=True)
store = TaskStore()


@mcp.tool()
def todo_list() -> str:
    """List all todo tasks. Returns a formatted string of id, title, and done status."""
    tasks = store.get_tasks()
    if not tasks:
        return "No tasks."
    lines = []
    for t in tasks:
        done = "[x]" if t["done"] else "[ ]"
        lines.append(f"  {t['id']}. {done} {t['title']}")
    return "\n".join(lines)


@mcp.tool()
def todo_add(title: str) -> str:
    """Add a new todo task. Give the task title. Returns the created task summary."""
    if not (title and title.strip()):
        return "Error: title cannot be empty."
    task = store.add_task(title.strip())
    return f"Added task {task['id']}: {task['title']}"


@mcp.tool()
def todo_remove(task_id: int) -> str:
    """Remove a todo task by its id. Returns a short confirmation or error."""
    if store.remove_task_by_id(task_id):
        return f"Removed task {task_id}."
    return f"Task {task_id} not found."


@mcp.tool()
def todo_toggle(task_id: int) -> str:
    """Toggle the done state of a task by id. Returns the new state or error."""
    task = store.get_task_by_id(task_id)
    if not task:
        return f"Task {task_id} not found."
    idx = next(i for i, t in enumerate(store.get_tasks()) if t["id"] == task_id)
    store.toggle_done(idx)
    new_done = store.get_task(idx)["done"]
    return f"Task {task_id} is now {'done' if new_done else 'not done'}."


if __name__ == "__main__":
    # Stdio is the default when Cursor (or another client) runs this script.
    mcp.run(transport="stdio")
