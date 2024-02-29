class Bounds:
    def __init__(self, left_bound: float, right_bound: float) -> None:
        self.left_bound = left_bound
        self.right_bound = right_bound

class Input:
    def __init__(self, method_num: int, func: str, bounds: Bounds, accuracy: float) -> None:
        self.method_num = method_num
        self.func = func
        self.bounds = bounds
        self.accuracy = accuracy

