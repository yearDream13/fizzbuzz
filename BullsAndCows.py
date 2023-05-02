import random

def get_random_four_digit_num() -> str:
    random_numbers = set()
    while len(random_numbers) != 4:
        random_numbers.add(random.randint(0, 9))
    
    return list(random_numbers)


def get_rightnum() -> int64:
    # 구현
    
    return -1
    
    
def get_rightpos() -> int64:
    # 구현
    
    return -1

def is_correct_guess() -> bool:
    # 구현
    
    return False


if __name__ == '__main__':
    number_to_guess = get_random_four_digit_num()
    
    is_correct = False
    
    while not is_correct:
        user_guess = input("enter 4 digit numbers")
        
        rightnum = get_rightnum(number_to_guess, user_guess)
        
        rightpos = get_rightpos(number_to_guess, user_guess)
        
        if is_correct_guess():
            is_correct = True