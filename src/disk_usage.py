# src/disk_usage.py

def total_size(node):
    """
    Compute total size of a nested file/dir tree.
    node format:
      - file: {"type": "file", "name": str, "size": int}
      - dir:  {"type": "dir", "name": str, "children": [nodes]}
    """
    if not node or not isinstance(node, dict):
        return 0

    node_type = node.get("type")

    if node_type == "file":
        return node.get("size", 0)

    elif node_type == "dir":
        total = 0
        for child in node.get("children", []):
            total += total_size(child)
        return total

    else:
        # Unknown type — ignore
        return 0
