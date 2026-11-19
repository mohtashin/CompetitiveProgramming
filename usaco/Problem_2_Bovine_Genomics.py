def main():
    # Step 1: Read the input
    with open("cownomics.in", "r") as f:
        N, M = map(int, f.readline().split())

        # Read the N spotty cow genomes
        spotty = []
        for _ in range(N):
            spotty.append(tuple(map(str, f.readline().strip())))
        # Read the N plain cow genomes
        plain = []
        for _ in range(N):
            plain.append(tuple(map(str, f.readline().strip())))

    # Step 2: Check each position in the genome
    answer = 0
    for i in range(M):
        tempspotty = "" #AGG
        tempplain = "" #CCA
        strike = 0
        for j in range(N):
            tempspotty += spotty[j][i]
            tempplain += plain[j][i]

        for num1 in tempspotty:
            for num2 in tempplain:
                if num1 == num2:
                    strike+=1
        if strike == 0:
            answer+=1

    
    # Step 3: Write the output
    with open("cownomics.out", "w") as f:
        f.write(str(answer) + "\n")


if __name__ == "__main__":
    main()
