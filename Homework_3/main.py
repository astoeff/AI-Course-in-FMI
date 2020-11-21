import random

from dot import Dot

def generate_n_different_random_dots(n):
    already_existing_dots_dict = {}
    generated_dots = []
    count = 0
    while count < n:
        dot = (random.randint(0, n - 1), random.randint(0, n - 1))
        try:
            already_existing_dots_dict[dot]
        except KeyError as e:
            count += 1
            already_existing_dots_dict[dot] = True
            generated_dots.append(Dot(dot))
        else:
            print("Povtarq se: ", dot)

    return generated_dots

def main():
    n = int(input('Enter number of cities to be travelled: '))

    assert n <= 100, 'Number of cities must be <= 100!'
    
    dots = generate_n_different_random_dots(n)
    for dot in dots:
        dot.print_coordinates()

if __name__ == '__main__':
    main()