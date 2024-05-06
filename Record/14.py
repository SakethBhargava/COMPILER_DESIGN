class Quadruple:
    def __init__(self, op, arg1, arg2, result):
        self.op = op          
        self.arg1 = arg1      
        self.arg2 = arg2      
        self.result = result

class Triple:
    def __init__(self, op, arg1, arg2):
        self.op = op          
        self.arg1 = arg1      
        self.arg2 = arg2      

if __name__ == "__main__":
    quadruples = []
    print("Enter Quadruples (Enter 'done' when finished):")
    while True:
        op = input("Enter operation: ")
        if op == "done":
            break
        arg1 = input("Enter argument 1: ")
        arg2 = input("Enter argument 2: ")
        result = input("Enter result: ")
        quadruples.append(Quadruple(op, arg1, arg2, result))
        
    triples = []
    print("\nEnter Triples (Enter 'done' when finished):")
    while True:
        op = input("Enter operation: ")
        if op == "done":
            break
        arg1 = input("Enter argument 1: ")
        arg2 = input("Enter argument 2: ")
        triples.append(Triple(op, arg1, arg2))
    print("\nQuadruples:")
    for quad in quadruples:
        print(quad.op + ", " + quad.arg1 + ", " + quad.arg2 + ", " + quad.result)
    print("\nTriples:")
    for trip in triples:
        print(trip.op + ", " + trip.arg1 + ", " + trip.arg2)
