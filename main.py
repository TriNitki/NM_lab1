import json

from utils import get_input, Input, Bounds
from methods import dyhotomy, chord, newton, combined, iteration, golden


def main():
    with open("input.json", "r") as f:
        user_data = json.load(f)
    
    input_data = Input(
        user_data["method"], 
        user_data["func"], 
        Bounds(
            user_data["border_l"], 
            user_data["border_r"]
        ), 
        user_data["eps"]
    )
    
    match (input_data.method):
        case 1:
            result = dyhotomy(
                input_data.func,
                input_data.bounds, 
                input_data.eps
            )
        case 2:
            result = chord(
                input_data.func,
                input_data.bounds, 
                input_data.eps
            )
        case 3:
            result = newton(
                input_data.func,
                input_data.bounds, 
                input_data.eps
            )
        case 4:
            result = combined(
                input_data.func,
                input_data.bounds, 
                input_data.eps
            )
        case 5:
            result = iteration(
                input_data.func,
                input_data.bounds, 
                input_data.eps
            )
        case 6:
            result = golden(
                input_data.func,
                input_data.bounds, 
                input_data.eps
            )
    
    with open("output.json", "w") as f: 
        json.dump(result.to_dict(), f)
    
    
    # result_0 = dyhotomy(
    #     input_data.func,
    #     input_data.bounds, 
    #     input_data.eps
    # )
    
    # result_1 = chord(
    #     input_data.func,
    #     input_data.bounds, 
    #     input_data.eps
    # )
    
    # result_2 = newton(
    #     input_data.func,
    #     input_data.bounds, 
    #     input_data.eps
    # )
    
    # result_3 = combined(
    #     input_data.func,
    #     input_data.bounds, 
    #     input_data.eps
    # )
    
    # result_4 = iteration(
    #     input_data.func,
    #     input_data.bounds, 
    #     input_data.eps
    # )
    
    # result_5 = golden(
    #     input_data.func,
    #     input_data.bounds, 
    #     input_data.eps
    # )
    
    # print("\nDehotomy: \n" + str(result_0) + "\n")
    # print("Chord: \n" + str(result_1) + "\n")
    # print("Newton: \n" + str(result_2) + "\n")
    # print("Combined: \n" + str(result_3) + "\n")
    # print("Iteration: \n" + str(result_4) + "\n")
    # print("Golden: \n" + str(result_5) + "\n")
    

if __name__ == "__main__":
    main()