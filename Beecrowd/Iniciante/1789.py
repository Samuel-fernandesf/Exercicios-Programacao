while True:
    try:
        n = int(input())
        lesmas = [int(i) for i in input().split()]

        maiorLesma = max(lesmas)

        if maiorLesma < 10:
            print(1)
        else:
            if maiorLesma >= 10 and maiorLesma < 20:
                print(2)
            else:
                print(3)
    except EOFError:
        break