class Doggy:
    num_of_dogs = 0
    birth_of_dogs = 0

    def __init__(self, name, index, num_of_dogs, birth_of_dogs):
        self.name = name
        self.index = index
        num_of_dogs += 1
        birth_of_dogs += 1

    def __del__(self, num_of_dogs):
        num_of_dogs -= 1
    
    def bark(self):
        print('멍멍')

    def get_status(self, num_of_dogs, birth_of_dogs):
        print(f'num_of_dogs = {num_of_dogs}, birth_of_dogs = {birth_of_dogs}')