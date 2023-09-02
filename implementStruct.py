from dataclasses import dataclass
import numpy as np

@dataclass
class Grid:
    ez: np.ndarray
    hy: np.ndarray
    sizeX: int
    maxTime: int
    cdtds: float #courant number

g = Grid(np.array([1,2,3]), np.array([5,6,7]), 3, 200,1.0)
print(g)