from utils import Bounds, Input
from user_data import get_input, function_parser

def main():
    # user_input = get_input()
    func = input("func: ")
    result = function_parser(func, 1)
    
    print(f"result = {result}")
    
    pass

if __name__ == "__main__":
    main()