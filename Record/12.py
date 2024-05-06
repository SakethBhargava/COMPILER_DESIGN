productions = {
    'E': ['TR'],
    'R': ['+TR', '#'],
    'T': ['FY'],
    'Y': ['*FY', '#'],
    'F': ['(E)', 'i']
}
first, follow = {}, {}
def First(nt):
    if nt in first: return
    for prod in productions[nt]:
        sym = prod[0]
        if sym.isupper():
            First(sym)
            first[nt] = first.get(nt, set()) | first[sym]
        else:
            first[nt] = first.get(nt, set()) | {sym}
def Follow(nt):
    if nt in follow: return
    for lhs, rhs in productions.items():
        for prod in rhs:
            pos = prod.find(nt)
            if pos != -1:
                if pos + 1 < len(prod):
                    next_sym = prod[pos + 1]
                    if next_sym.isupper():
                        First(next_sym)
                        follow[nt] = follow.get(nt, set()) | first[next_sym]
                    else:
                        follow[nt] = follow.get(nt, set()) | {next_sym}
                elif lhs != nt:
                    Follow(lhs)
                    follow[nt] = follow.get(nt, set()) | follow[lhs]
for nt in productions:
    First(nt)
    Follow(nt)
print("First Sets:")
for nt, f_set in first.items():
    print(f"First({nt}) = {{ {', '.join(f_set)} }}")
print("\nFollow Sets:")
for nt, fo_set in follow.items():
    print(f"Follow({nt}) = {{ {', '.join(fo_set)} }}")