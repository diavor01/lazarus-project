from pprint import pprint
import subprocess
import sys
import click

def get_changed_files() -> list[str]:
    result = subprocess.run(['git', 'diff', '--name-only'], 
                          capture_output=True, text=True)
    
    updated_file_paths = result.stdout.strip().split('\n') if result.stdout.strip() else []
    return updated_file_paths

# Here I make the api call to the api
def return_new_documentation(content):
    return content + '\nprint("Success")\n'

def return_new_file_path(file):
    path = file.split("/")
    file_name = path[-1]
    new_file_name = "new_" + file_name
    path[-1] = new_file_name
    updated_path = "/".join(path)
    return updated_path

def get_new_file_content_from_AI(file_path):
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

@click.command()
def output_diff() -> None:
    updated_file_paths = get_changed_files()

    for file_path in updated_file_paths:
        new_file_path = get_new_file_content_from_AI(file_path)

        run_diff(file_path, new_file_path)

        if click.confirm(f"Accept these changes in {file_path}?"):
            subprocess.run(['mv', new_file_path, file_path], 
                                capture_output=True, text=True)
            click.echo(f'Changed {file_path}')
        else:
            click.echo("No change executed")
            subprocess.run(['rm', '-rf', new_file_path], 
                                capture_output=True, text=True)

        # Just temporarily
        break

if __name__ == "__main__":
    output_diff()
