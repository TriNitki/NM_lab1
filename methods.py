from utils import Bounds, Result, f, d

def dyhotomy(func: str, bounds: Bounds, eps: float) -> Result:
    root = None
    while abs(f(func, bounds.r)-f(func, bounds.l)) > eps:
        mid = (bounds.l+bounds.r) / 2
        if f(func, mid) == 0 or abs(f(func, mid)) < eps:
            root = mid
            break
        elif f(func, bounds.l)*f(func, mid) < 0:
            bounds.r = mid
        else:
            bounds.l = mid

    func_value = f(func, root)

    result = Result(root, func_value, func_value)
    return result

def chord(func: str, bounds: Bounds, eps: float) -> float:
    i = 1
    while True:
        assert f(func, bounds.l) != f(func, bounds.r), "Деление на 0"
        
        root = (bounds.l-(bounds.r-bounds.l)*f(func, bounds.l) / 
            (f(func, bounds.r) - f(func, bounds.l)))
        
        bounds.l, bounds.r = bounds.r, root
        i = i + 1
        
        if abs(f(func, root)) <= eps:
            break
    
    func_value = f(func, root)
    result = Result(root, func_value, func_value)
    return result

def newton(func: str, bounds: Bounds, eps: float):    
    
    while True:
        assert d(func, bounds.l) != 0.0, "Деление на 0"
        
        root = bounds.l-f(func, bounds.l)/d(func, bounds.l)
        bounds.l = root
        
        if abs(f(func, root)) <= eps:
            break
        
    func_value = f(func, root)
    result = Result(root, func_value, func_value)
    return result