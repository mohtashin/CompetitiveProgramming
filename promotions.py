def main():
    fin = open("promote.in", "r")
    b_before, b_after = map(int, fin.readline().split())
    s_before, s_after = map(int, fin.readline().split())
    g_before, g_after = map(int, fin.readline().split())
    p_before, p_after = map(int, fin.readline().split())
    fin.close()

    g2p = p_after - p_before
    s2g = (g_after - g_before) + g2p
    b2s = (s_after - s_before) + s2g

    fout = open("promote.out", "w")
    fout.write(str(b2s) + "\n")
    fout.write(str(s2g) + "\n")
    fout.write(str(g2p) + "\n")
    fout.close()


if __name__ == "__main__":
    main()
