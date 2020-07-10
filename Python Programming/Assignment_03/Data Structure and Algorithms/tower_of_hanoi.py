def tower_of_hanoi(height, from_pole, to_pole, with_pole):
    if height >= 1:
        tower_of_hanoi(height - 1, from_pole, with_pole, to_pole)
        moveDisk(from_pole, to_pole)
        tower_of_hanoi(height - 1, with_pole, to_pole, from_pole)


def moveDisk(fp, tp):
    print("moving disk from", fp, "to", tp)


tower_of_hanoi(3, "A", "B", "C")
