import numpy as np

class solution():

    def __init__(self):
        pass

    def gen(self):
        x = np.random.randint(20,110, size=(100))
        return x

    def warningSys(self):
        x = self.gen()
        print(f"All temperatures: {x}")
        res = [int(num) for num in x if num > 80]
        return res

class main():

    def __init__(self):
        self.solution = solution()

    def run(self):
        x = self.solution.warningSys()
        print(f"Faulty temperatures: {x}")

if __name__ == "__main__":
    application = main()
    application.run()