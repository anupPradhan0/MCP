# Connect to the Todo MCP server

This project includes an MCP server so Cursor (or any MCP client) can use your todo list via **tools**: `todo_list`, `todo_add`, `todo_remove`, `todo_toggle`.

## 1. Install dependencies

From the project root:

```bash
cd /home/mors/Code/MCP
pip install -r requirements.txt
```

## 2. Add the server in Cursor

**Option A – Project config (already in repo)**  
If you opened Cursor from this project folder, the file `.cursor/mcp.json` is already set. Cursor uses it when the project is the workspace. Ensure you ran `pip install -r requirements.txt` in this project so `python mcp_server.py` finds the `mcp` package.

**Option B – Global config**  
Add the server to your user MCP config so it’s available in any project:

1. Open **Cursor Settings** → **MCP** (or edit the file directly).
2. Open `~/.cursor/mcp.json`.
3. Add a `"todo"` entry inside `mcpServers`:

```json
{
  "mcpServers": {
    "todo": {
      "command": "python",
      "args": ["/home/mors/Code/MCP/mcp_server.py"]
    }
  }
}
```

Use your real project path instead of `/home/mors/Code/MCP` if it’s different.

## 3. Restart Cursor

Restart Cursor (or reload the window) so it picks up the MCP config and starts the server.

## 4. Use the tools

In chat or Composer you can ask to:

- **List tasks** – e.g. “List my todos” (uses `todo_list`).
- **Add a task** – e.g. “Add todo: buy milk” (uses `todo_add`).
- **Remove a task** – e.g. “Remove todo 2” (uses `todo_remove`).
- **Toggle done** – e.g. “Mark task 1 done” (uses `todo_toggle`).

The server runs as a subprocess and talks to Cursor over **stdio**; no extra URL or token is needed. Tasks are stored in memory for the lifetime of that server process.
