import time

MAX = 1000000
memo = [0] * MAX

def collatz(n):
    if n == 1:  
        return 1
    
    if n < MAX and memo[n] != 0: 
        return memo[n]
    
    steps = 1  
    if n % 2 == 0:
        steps += collatz(n // 2)
    else:
        steps += collatz(3 * n + 1)
    
    if n < MAX:
        memo[n] = steps
    
    return steps

def main():
    
    start = time.time()

    memo[1] = 1  

    max_steps = 0
    max_num = 0

    for i in range(2, MAX):
        steps = collatz(i)
        if steps > max_steps:
            max_steps = steps
            max_num = i

    
    end = time.time()

    print(f"O número que gera a sequência mais longa é: {max_num}")
    print(f"Comprimento da sequência: {max_steps}")
    print(f"Tempo de execução: {end - start:.2f} segundos")

if __name__ == "__main__":
    main()