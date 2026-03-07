"""Demo: TaskStore uses instance-level list (each store is independent)."""

from task import TaskStore

store_a = TaskStore()
store_b = TaskStore()

print("Initial state:")
print("  store_a:", store_a.get_tasks())
print("  store_b:", store_b.get_tasks())

store_a.add_task("added via A")
store_b.add_task("added via B")

print("\nAfter each store adds one task:")
print("  store_a:", store_a.get_tasks())
print("  store_b:", store_b.get_tasks())
