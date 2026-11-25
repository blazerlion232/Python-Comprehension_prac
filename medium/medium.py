import numpy as np

class solution():

    def __init__(self):
        pass

    def gen(self):
        x = np.random.randint(20,110, size=(100))
        return x

    def warningSys(self):
        x = self.gen()
        print(x)
        res = [num for num in x for i in range(len(x)) if x[i] > 80]
        return res

class main():

    def __init__(self):
        self.solution = solution()

    def run(self):
        x = self.solution.warningSys()
        print(x)

if __name__ == "__main__":
    application = main()
    application.run()