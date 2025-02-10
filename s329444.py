import numpy as np

# All numpy's mathematical functions can be used in formulas
# see: https://numpy.org/doc/stable/reference/routines.math.html

def f1(x: np.ndarray) -> np.ndarray:
    return np.sin(x[0])

def f2(x: np.ndarray) -> np.ndarray: 
    return ((((np.sqrt((((x[0] + x[2]) + (x[0] + (x[1] + x[0]))) + ((x[0] + (x[1] + x[0])) + x[2]))) + np.exp(((np.sqrt((x[0] + ((x[2] + np.log(x[2])) + x[2]))) + x[2]) + (x[2] + np.log((x[2] + np.log(x[2]))))))) + np.sqrt((x[0] + (x[2] + (x[1] + x[0]))))) + np.sqrt(((x[0] + x[0]) + (x[1] + x[2])))) + np.sqrt(((x[0] + (x[2] + (x[1] + x[0]))) + np.sin(x[2]))))

def f3(x: np.ndarray) -> np.ndarray: 
    return (((((((abs(np.exp(np.cos((np.abs(np.abs(np.abs(np.exp(np.sin(np.sin(np.sin(np.sin(np.sqrt(np.sqrt(x[1])))))))))) - x[1])))) - x[1]) - x[1]) + np.sin(np.sin(np.sqrt(x[1])))) + np.cos((np.abs(np.abs(np.abs(np.abs(np.exp(np.sin(np.sqrt(x[1]))))))) - x[1]))) + np.cos(np.cos(((np.abs(np.sqrt(np.sqrt(x[1]))) - np.cos((np.sqrt(x[1]) - x[1]))) - np.cos((np.sqrt(x[1]) - x[1])))))) + np.cos((np.abs(np.abs(np.exp(np.sin(np.sqrt(x[1]))))) - x[1]))) * 8.386974733167488)

def f4(x: np.ndarray) -> np.ndarray: 
    return ((np.sin((np.cos(x[1]) + np.sin((np.cos(x[1]) + (np.cos(x[1]) + np.cos((np.cos(x[1]) + np.cos(np.sin((np.cos(x[1]) + (np.cos(x[1]) + np.cos(x[1])))))))))))) + (np.cos(x[1]) + np.exp(np.cos(x[1])))) + (np.sin((np.cos(x[1]) + np.cos(np.sin((np.cos(x[1]) + (np.cos(x[1]) + np.cos((np.cos(x[1]) + np.exp(np.cos(x[1])))))))))) + ((np.cos(x[1]) + np.exp(np.cos(x[1]))) + np.cos(x[1]))))

def f5(x: np.ndarray) -> np.ndarray:
    return np.sin((-6.802595075418944 / np.exp((abs(np.exp(4.165482260553965)) / np.log(3.7495617084686668)))))

def f6(x: np.ndarray) -> np.ndarray: 
    return (np.log(np.exp(x[1])) + (((np.log(np.exp(x[1])) + (((x[1] + x[1]) - ((x[1] + x[1]) - x[0])) - x[0])) + ((x[1] - ((x[1] + x[1]) - ((x[1] + x[1]) - x[0]))) / -3.121302705566653)) - x[0]))

def f7(x: np.ndarray) -> np.ndarray: 
    return (np.sqrt(np.exp(np.exp(np.cos(-6.09018062873057)))) - (x[0] * ((x[1] * np.cos((((x[0] - x[1]) * ((x[1] + x[1]) * np.cos((((x[0] - x[1]) * x[1]) * x[0])))) * x[0]))) * ((((x[0] + x[1]) * np.cos(((x[0] - x[1]) * x[0]))) * np.cos(np.cos(np.cos((np.cos(-6.09018062873057) - -6.09018062873057))))) * ((((x[0] + x[1]) * np.cos(((x[0] - x[1]) * x[1]))) * np.cos((((x[0] - x[1]) * x[1]) * x[0]))) * -7.541497887204642)))))

def f8(x: np.ndarray) -> np.ndarray: 
    return ((np.exp(np.abs(x[5])) * x[5]) * np.abs((4.6361949565668255 * 4.6361949565668255)))
