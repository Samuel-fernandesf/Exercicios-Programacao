i = 0
j = 1

while i <= 2:
    for k in range(0, 3): 
        
        if i == int(i):
            print(f'I={i:.0f} J={j:.0f}')

        else:
            print(f'I={i:.1f} J={j:.1f}')


        j += 1

    i = round(i + 0.2, 1)
    j = round(j - 2.8, 1)
    

