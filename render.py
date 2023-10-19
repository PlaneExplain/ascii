from PIL import Image

import numpy as np

FILEPATH = 'dog.jpg'
SCALE = " @B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/|()1{}[]?-_+~i!lI;:,\"^`"

def get_terminal_dimensions() -> tuple[int, int]:
    '''Get the rows/cols of the terminal'''
    import os
    size = os.popen('stty size', 'r').read().split()
    return (int(size[1]), int(size[0])-1)

def get_proportion(dimensions: tuple[int,int]) -> float:
    '''Get the proportion value rounded to the first decimal place'''
    return round(dimensions[0]/dimensions[1],2)

def image_to_array(photo) -> np.ndarray:
    data = np.asarray(photo)
    return data

def calculate_perceived_brightness(arr: np.ndarray) -> int:
    R=arr[0]
    G=arr[1]
    B=arr[2]
    return round(0.2126*R + 0.7152*G + 0.0722*B,2)

def main() -> None:
    '''Driver code'''
    dog_image = Image.open(FILEPATH)

    dimensions = dog_image.size
    print(f'Dimensions of the image: {dimensions}')

    term_dimensions = get_terminal_dimensions()
    term_proportions = get_proportion(term_dimensions)
    print(f'Proportions of the terminal: {term_proportions}')
    print(f'Dimensions of the terminal: {term_dimensions}')

    new_image = dog_image.resize(term_dimensions)
    image_array = image_to_array(new_image)

    for i in range(len(image_array)):
        for j in range(len(image_array[0])):
            avg = calculate_perceived_brightness(image_array[i][j])
            char=SCALE[int((avg*63)/255)]
            print(char,end='')
        print()


if __name__=='__main__':
    main()
