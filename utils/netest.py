import ast


def get_dependencies(file_path):
    with open(file_path, "r") as file:
        tree = ast.parse(file.read(), filename=file_path)

    dependencies = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                dependencies.add(alias.name)
        elif isinstance(node, ast.ImportFrom):
            dependencies.add(node.module)

    return dependencies


def write_dependencies_to_file(dependencies, output_file_path):
    with open(output_file_path, "w") as file:
        for dependency in dependencies:
            file.write(f"{dependency}\n")


# Example usage
file_path = "../main.py"
output_file_path = "dependencies.txt"

dependencies = get_dependencies(file_path)
write_dependencies_to_file(dependencies, output_file_path)

print(f"Dependencies written to {output_file_path}")
