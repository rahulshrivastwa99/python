import os

# Get the current working directory
current_directory = os.getcwd()

# List all files and directories in the current directory
contents = os.listdir(current_directory)

print(f"Contents of directory '{current_directory}':")
for item in contents:
    print(item)
