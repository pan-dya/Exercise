def num_atoms (m,M = 196.97):
    n = m / M
    avogadro = 6.022 * 10 **23
    result = n * avogadro
    print(result)

num_atoms(10, 12.001)