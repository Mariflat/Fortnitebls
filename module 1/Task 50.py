size = 9  # Size of the square (an odd number keeps the center symmetrical)

while True:
    print("\n=== SHAPE SELECTION MENU ===")
    print("Level 1: a, b, i, k (or а, б, і, к)")
    print("Level 2: v, g, j, z (or в, г, ж, з)")
    print("Level 3: d, e (or д, е)")
    print("0 - Exit")

    choice = input("Choose a shape letter: ").strip().lower()

    if choice == '0':
        print("Program finished.")
        break

    # Validate user input (supports both English and Ukrainian/Russian letters)
    valid_choices = ('a', 'b', 'i', 'k', 'v', 'g', 'j', 'z', 'd', 'e',
                     'а', 'б', 'і', 'и', 'к', 'в', 'г', 'ж', 'з', 'д', 'е')
    if choice not in valid_choices:
        print("Error: Invalid menu option! Please try again.")
        continue

    print()
    for i in range(size):
        for j in range(size):
            draw = False

            # Level 1
            if choice in ('a', 'а'):
                draw = (j >= i)
            elif choice in ('b', 'б'):
                draw = (j <= i)
            elif choice in ('i', 'і', 'и'):
                draw = (i + j <= size - 1)
            elif choice in ('k', 'к'):
                draw = (i + j >= size - 1)

            # Level 2
            elif choice in ('v', 'в'):
                draw = (j >= i) and (i + j <= size - 1)
            elif choice in ('g', 'г'):
                draw = (j <= i) and (i + j >= size - 1)
            elif choice in ('j', 'ж'):
                draw = (j <= i) and (i + j <= size - 1)
            elif choice in ('z', 'з'):
                draw = (j >= i) and (i + j >= size - 1)

            # Level 3
            elif choice in ('d', 'д'):
                draw = (j >= i and i + j <= size - 1) or (j <= i and i + j >= size - 1)
            elif choice in ('e', 'е'):
                draw = (j <= i and i + j <= size - 1) or (j >= i and i + j >= size - 1)

            # Print an asterisk with a trailing space so the square looks proportional
            print("* " if draw else "  ", end="")
        print()