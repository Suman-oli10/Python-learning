import os

def list_directory_contents(path='.'):
    try:
        # List all files and directories in the given path
        contents = os.listdir(path)
        print(f"Contents of directory '{path}':")
        for item in contents:
            print(item)
    except FileNotFoundError:
        print(f"The directory '{path}' does not exist.")
    except PermissionError:
        print(f"Permission denied to access '{path}'.")

# Example usage
directory_path = input("Enter the path of the directory (leave blank for current directory): ") or '.'
list_directory_contents(directory_path)
