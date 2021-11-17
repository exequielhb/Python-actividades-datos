from collections import deque
from collections import deque

cola = deque()

print(cola)

#eliminamos el primer elemento a diferencia del ultimo con pop()
cola = deque([1, 3, 5, "holass"])
cola.popleft()
print(cola)