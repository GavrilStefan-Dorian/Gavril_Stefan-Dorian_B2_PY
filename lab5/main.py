
def ex1():
    class Stack:
        def __init__(self):
            self.stack = []
        def push(self, item):
            self.stack.append(item)
        def pop(self):
            if 0 == len(self.stack):
                return None
            return self.stack.pop()
        def peek(self):
            if 0 == len(self.stack):
                return None
            return self.stack[-1]

    newStack = Stack()
    newStack.push(1)
    newStack.push(2)
    newStack.push(3)
    print(newStack.stack)
    print(newStack.peek())
    print(newStack.stack)
    print(newStack.pop())
    print(newStack.stack)


def ex2():
    class Queue:
        def __init__(self):
            self.queue = []
        def push(self, item):
            self.queue.append(item)
        def pop(self):
            if 0 == len(self.queue):
                return None
            value = self.queue[0]
            self.queue.remove(value)
            return value
        def peek(self):
            if 0 == len(self.queue):
                return None
            value = self.queue[0]
            return value

    newQueue = Queue()
    newQueue.push(1)
    newQueue.push(2)
    newQueue.push(3)
    print(newQueue.queue)
    print(newQueue.peek())
    print(newQueue.queue)
    print(newQueue.pop())
    print(newQueue.queue)


def ex3():
    class Matrix:
        def __init__(self, n, m):
            self.n = n
            self.m = m
            self.matrix = [[0 for _ in range(0, m)] for _ in range(0, n)]

        def __str__(self):
            newPrint = ""
            for i in range(0, matrix.n):
                for j in range(0, matrix.m):
                    newPrint += f"{self.get_at(i, j)} "
                newPrint += "\n"
            return newPrint

        def get_at(self, i, j):
            return self.matrix[i][j]
        def set_at(self, value, row, column):
            self.matrix[row][column] = value

        def transpose(self):
            self.matrix = [[self.matrix[i][j] for i in range(0, self.n)] for j in range(0, self.m)]
            self.n, self.m = self.m, self.n

        def __mul__(self, other):
            if not isinstance(other, Matrix):
                raise ValueError("Other operand not of Matrix")
            if self.m != other.n:
                raise ValueError("Matrixes have incompatible dimensions")

            newOther = Matrix(other.n, other.m)
            newOther.matrix = [row[:] for row in other.matrix]
            newOther.transpose()

            newMatrix = Matrix(self.n, other.m)
            newMatrix.matrix = [
                [sum(a * b for a, b in zip(self.matrix[i], newOther.matrix[j]))
                                 for j in range(0, other.m)]
                                 for i in range(0, self.n)
            ]
            return newMatrix

        def apply_iter(self, func):
            self.matrix = [[func(self.matrix[i][j]) for j in range(0, self.m)] for i in range(0, self.n)]

    matrix = Matrix(2, 2)
    print(matrix.matrix)
    matrix.set_at(1, 0, 0)
    print(matrix.matrix)
    matrix.set_at(2, 0, 1)
    print(matrix.matrix)
    matrix.set_at(3, 1, 0)
    print(matrix.matrix)
    matrix.set_at(4, 1, 1)
    print(matrix.matrix)


    print("First Matrix")
    print(matrix)

    otherMatrix = Matrix(2, 2)
    otherMatrix.set_at(1, 0, 0)
    otherMatrix.set_at(2, 0, 1)
    otherMatrix.set_at(3, 1, 0)
    otherMatrix.set_at(4, 1, 1)

    otherMatrix.transpose()

    print("Second Matrix (transposed first)")
    print(otherMatrix)

    mulMatrix = matrix * otherMatrix
    print("Multiplied result Matrix")
    print(mulMatrix)

    print("First Matrix, x2 applied")
    matrix.apply_iter(lambda x: x * 2)

    print(matrix)




def main():
    print("======EX 1======")
    ex1()

    print("======EX 2======")
    ex2()

    print("=======EX 3======")
    ex3()

if __name__ == '__main__':
    main()
