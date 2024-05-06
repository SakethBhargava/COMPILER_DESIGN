def NonT(a, NT):
    for i, nt in enumerate(NT):
        if nt == a:
            return i
    return -1

def Term(a, T):
    for i, ter in enumerate(T):
        if ter == a:
            return i
    return -1

def Lead(a, b, l, T, NT, s):
    if l[a][b] == 'f':
        l[a][b] = 't'
        s.append(T[b])
        s.append(NT[a])

def Trail(a, b, tr, T, NT, s):
    if tr[a][b] == 'f':
        tr[a][b] = 't'
        s.append(T[b])
        s.append(NT[a])

nt = int(input("Enter the number of non-terminals: "))
NT = input("Enter the non-terminals (space-separated): ").split()

t = int(input("Enter the number of terminals: "))
T = input("Enter the terminals (space-separated): ").split()

l = [['f'] * t for _ in range(nt)]
tr = [['f'] * t for _ in range(nt)]

n = int(input("Enter the number of production rules: "))
print("Enter the production rules (e.g., A -> x):")
for _ in range(n):
    A, arrow, alpha = input().split()
    idxA = NonT(A, NT)
    idxAlpha = NonT(alpha, NT) if alpha.isupper() else Term(alpha, T)
    s = []
    Lead(idxA, idxAlpha, l, T, NT, s)
    Trail(idxA, idxAlpha, tr, T, NT, s)

print("\nLeading Sets:")
for i in range(nt):
    print(f"{NT[i]}:", end=" ")
    for j in range(t):
        if l[i][j] == 't':
            print(T[j], end=" ")

print("\nTrailing Sets:")
for i in range(nt):
    print(f"{NT[i]}:", end=" ")
    for j in range(t):
        if tr[i][j] == 't':
            print(T[j], end=" ")