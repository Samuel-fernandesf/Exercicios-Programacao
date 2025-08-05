def fatorial(n):
    fat = 1
    for i in range(1, n+1):
        fat = fat * i #ou *=
        
    return fat
    
def main():
    n = int(input())
    
    print(fatorial(n))

main()