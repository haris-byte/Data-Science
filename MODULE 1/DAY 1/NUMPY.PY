import numpy as n
# Array Creation
h_arr = n.array([1,2,3,4,5,6,7,8,9,10])
print(h_arr)
print(type(h_arr),n.shape(h_arr),n.ndim(h_arr))
# Zero Array
h = n.zeros((2,3))
print(f"zeros \n {h}")
# Ones Array
h1 = n.ones((2,3))
print(f"Ones \n {h1}\n{n.ones(5)}")
# Arrange
h2 = n.arange(20, 80, 7)
print(f"Arrange: \n{h2}")
h3 = n.linspace(0,10, 20)
print(f"linespace:\n {h3}")
print(f"Reshpape:\n {n.reshape(h1,6)}")
test = n.arange(20).reshape(4,5)
print(test)
print(f"reval()\n{test.ravel}")
print(f"Reshape -1: \n {test.reshape(-1)}")
array2 = n.arange(12).reshape(2,3,2).swapaxes(1,2)
print("\narray2 \n", array2)

print(n.random.rand(2,3))
print(n.random.rand(8))
print(n.random.randint(5,40))
quest = n.random.randint(0,100,(5,5))
print(quest)
print(n.min(quest))
print(n.max(quest))
print(n.mean(quest))
D1 = n.reshape(quest,-1)
print(D1)
print(n.sort(quest, axis=1))
print("Groiuping\n grouping")
group = D1.reshape(5,5)
for i , group in enumerate(group,9):
    print(i, group)