from data import DATA

TREE = '#'

def traverse(data, right, down):    
    rows = len(data)
    cols = len(data[0])

    trees = 0
    row = 0
    col = 0

    while row < rows:
        trees += data[row][col] == TREE
        

        row = row + down
        col = (col + right) % cols

    return trees


if __name__ == "__main__":
    print("PART ONE\n========")
    print(traverse(DATA, 3, 1))

    print("\nPART TWO\n========")
    product = 1
    for right, down in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
        trees = traverse(DATA, right, down)
        product *= trees

        print("Right: {}  Down: {}  Trees: {}".format(right, down, trees))
    print("Product: {}".format(product))

