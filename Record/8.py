def check():
    global i, j, c
    for z in range(c):
        if stk[z] == '4':
            print("REDUCE TO E -> 4")
            stk[z] = 'E'
            stk[z + 1] = ''
            print("$" + ''.join(stk) + "\t" + a[j+1:] + "$\t")
    for z in range(c - 2):
        if stk[z:z+3] == ['2', 'E', '2'] or stk[z:z+3] == ['3', 'E', '3']:
            print(f"REDUCE TO E -> {''.join(stk[z:z+3])}")
            stk[z:z+3] = ['E', '', '']
            print("$" + ''.join(stk) + "\t" + a[j+1:] + "$\t")
            i -= 2
            c -= 2
if __name__ == "__main__":
    print("GRAMMAR is -\nE->2E2 \nE->3E3 \nE->4\n")
    a = "32423"
    c = len(a)
    print("\nstack \t input \t action")
    print("$\t" + a + "$\t")
    i = j = 0
    stk = [''] * 15
    for j in range(c):
        stk[i] = a[j]
        i += 1
        check()
        print("SHIFT")
        print("$" + ''.join(stk) + "\t" + a[j+1:] + "$\t") 
    check()
    print("Accept" if stk[:2] == ['E', ''] else "Reject")