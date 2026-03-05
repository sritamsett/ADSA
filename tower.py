
move_count = 0

def tower_of_hanoi(n, source, auxiliary, destination):
    global move_count

    if n == 1:
        move_count += 1
        print(f"Move disk 1 from {source} -> {destination}")
        return

    tower_of_hanoi(n-1, source, destination, auxiliary)

    move_count += 1
    print(f"Move disk {n} from {source} -> {destination}")

    tower_of_hanoi(n-1, auxiliary, source, destination)



n = int(input("Enter number of disks: "))

tower_of_hanoi(n, 'A', 'B', 'C')

print("\nTotal number of disk movements =", move_count)