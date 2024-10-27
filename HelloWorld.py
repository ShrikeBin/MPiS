for i in range(256):
    print("\033[38;5;"+str(i)+"mHello World\033[0m", end=' ')
    
    if (i + 1) % 14 == 0:
        print()
print()
