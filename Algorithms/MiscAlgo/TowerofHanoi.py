# Recursive function to solve Tower of Hanoi
def tower_of_hanoi(n, source, auxiliary, destination):
    # Base case: only one disk to move
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return

    # Step 1: Move n-1 disks from source to auxiliary
    tower_of_hanoi(n - 1, source, destination, auxiliary)

    # Step 2: Move nth disk from source to destination
    print(f"Move disk {n} from {source} to {destination}")

    # Step 3: Move n-1 disks from auxiliary to destination
    tower_of_hanoi(n - 1, auxiliary, source, destination)


# -------- Main Program --------

# Take input from user
n = int(input("Enter the number of disks: "))

# Call the function with source=A, auxiliary=B, destination=C
print(f"\nSteps to solve Tower of Hanoi with {n} disks:\n")
tower_of_hanoi(n, 'A', 'B', 'C')
