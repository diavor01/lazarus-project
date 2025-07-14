import subprocess
import click

def get_changed_files() -> list[str]:
    result = subprocess.run(['git', 'diff', '--name-only'], 
                          capture_output=True, text=True)
    
    updated_file_paths = result.stdout.strip().split('\n') if result.stdout.strip() else []
    return updated_file_paths

# Here I make the api call to the AI
def return_new_documentation(content: str) -> str:
    return content + '\nprint("Success")\n'

def return_new_file_path(file: str) -> str:
    path = file.split("/")
    file_name = path[-1]
    new_file_name = "new_" + file_name
    path[-1] = new_file_name
    updated_path = "/".join(path)
    return updated_path

def writing_new_file(file_path):
    with open(file_path, "r") as file:
        content = file.read()

    new_content = return_new_documentation(content)
    new_file_path = return_new_file_path(file_path)

    with open(new_file_path, "w") as file:
        file.write(new_content)

    return new_file_path

def run_diff(initial_file: str, new_file: str) -> None:
    result = subprocess.run(['diff', '-y', initial_file, new_file], 
                            capture_output=True, text=True)
    print(result.stdout)

def filter_files_to_ignore(updated_file_paths: list[str]) -> list[str]:
    # Here I would implement a logic to be able to ignore certain files you wish not to 
    # update the docs of. It could just be a copy of .gitignore
    return updated_file_paths

@click.command()
def run_autodocs() -> None:
    updated_file_paths = get_changed_files()

    filtered_updated_file_paths = filter_files_to_ignore(updated_file_paths)

    for file_path in filtered_updated_file_paths:
        new_file_path = writing_new_file(file_path)

        run_diff(file_path, new_file_path)

        if click.confirm(f"Accept these changes in {file_path}?"):
            subprocess.run(['mv', new_file_path, file_path], 
                                capture_output=True, text=True)
            click.echo(f'Changed {file_path}')
        else:
            click.echo("No change executed")
            subprocess.run(['rm', '-rf', new_file_path], 
                                capture_output=True, text=True)
        click.echo("Moving to the next file\n")

if __name__ == "__main__":
    run_autodocs()
