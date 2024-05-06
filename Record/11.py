table = {}
while True:
    print("\nSYMBOL TABLE IMPLEMENTATION")
    print("1. INSERT\n2. DISPLAY\n3. DELETE\n4. END")
    op = input("\nEnter your option: ")
    if op == '1':
        label, symbol, addr = input("Enter label, symbol, and address (comma-separated): ").split(',')
        if label not in table:
            table[label] = {'symbol': symbol, 'address': int(addr)}
            print("Label inserted.")
        else:
            print("Label already exists. Duplicate not inserted.")
    elif op == '2':
        if table:
            print("\nLABEL\t\tSYMBOL\t\tADDRESS")
            for label, entry in table.items():
                print(f"{label}\t\t{entry['symbol']}\t\t{entry['address']}")
        else:
            print("Symbol table is empty.")
    elif op == '3':
        label = input("Enter the label to be deleted: ")
        if label in table:
            del table[label]
            print("Label deleted.")
        else:
            print("Label not found.")
    elif op == '4':
        break
    else:
        print("Invalid option. Please choose again.")