marks = int(input("Enter your marks(out of 100): "))

cutoff = int(input("Enter the pass mark: "))

diff = (marks - cutoff) + 1

if (diff + abs(diff)):
    print("Pass")