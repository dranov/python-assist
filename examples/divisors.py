# Reads an integer from stdin and prints out its divisors

def divisors(n):
    l = []
    for i in range(1, n + 1):
        if n % i == 0:
            l.append(i)
    return l

if __name__ == "__main__":
    n = int(input("Enter a positive number: "))
    print("The divisors of {} are:".format(n))
    for d in divisors(n):
        print(d)
