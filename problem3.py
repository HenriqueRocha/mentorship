def compareTripletsScore(a, b):
    score_alice = 0
    score_bob = 0

    for i in range(3):
        if a[i] > b[i]:
            score_alice += 1
        elif a[i] < b[i]:
            score_bob += 1

    return [score_alice, score_bob]
