import os

# Get the current working directory
current_directory = os.getcwd()
print(f"Current working directory: {current_directory}")

# Create a new directory
new_directory_name = "my_new_folder"
os.makedirs(new_directory_name, exist_ok=True) # exist_ok=True prevents an error if the directory already exists
print(f"Created directory: {new_directory_name}")

# Change the current working directory
os.chdir(new_directory_name)
print(f"Changed directory to: {os.getcwd()}")

# List files and directories in the current directory
contents = os.listdir(".")
print(f"Contents of current directory: {contents}")

# Create a file and write to it
file_name = "example.txt"
with open(file_name, "w") as f:
    f.write("This is an example file.")
print(f"Created file: {file_name}")

# Rename a file
old_file_name = "example.txt"
new_file_name = "renamed_example.txt"
os.rename(old_file_name, new_file_name)
print(f"Renamed '{old_file_name}' to '{new_file_name}'")

# Check if a path exists and if it's a file or directory
print(f"Does '{new_file_name}' exist? {os.path.exists(new_file_name)}")
print(f"Is '{new_file_name}' a file? {os.path.isfile(new_file_name)}")
print(f"Is '{new_directory_name}' a directory? {os.path.isdir(current_directory)}") # Using the original directory path

# Remove a file
os.remove(new_file_name)
print(f"Removed file: {new_file_name}")

# Change back to the original directory and remove the created folder
os.chdir(current_directory)
os.rmdir(new_directory_name)
print(f"Removed directory: {new_directory_name}")