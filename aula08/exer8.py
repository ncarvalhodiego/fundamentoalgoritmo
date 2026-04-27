n = int(input("Digite o valor de n (entre 1 e 10): "))

if n > 10 or n < 1:
    print("Por favor, insira um número entre 1 e 10.")
else:
    print("Matriz %dx%d: " % (n,n), end="[")
    for i in range(n):
        print("[", end="")
        
        for j in range(n):
            if j == n-1:
                print("0", end="")
            else:
                print("0, ", end="")
            
        if i == n-1:
            print("]", end="")
        else:
            print("], ", end="")
    print("]", end="")