import sys

def main():
    data = sys.stdin.read().strip().splitlines()
    M, N, K = map(int, data[0].split())
    rows = data[1:1+M]

    for row in rows:
        enlarged = "".join(ch * K for ch in row)
        for _ in range(K):
            print(enlarged)

if __name__ == "__main__":
    main()
