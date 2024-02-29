from utils import get_input
from methods import dyhotomy, chord, newton


def main():
    user_input = get_input()
    
    result = newton(
        user_input.func,
        user_input.bounds, 
        user_input.eps)
    
    print(f"{result}")
    
    pass

if __name__ == "__main__":
    main()