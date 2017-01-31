#coding=utf-8
'''
a) Luku on aina sen kaksi edeltäjä yhteenlaskettuna.
'''

def Fi(k):
    K = [0, 1]
    if k == 0 or k == 1:
        return K[k]
    for i in range(2, k + 1):
        K.append(K[i - 2] + K[i - 1])

    return K[k]


def Fr(k):
    K = [0, 1]
    if k == 0 or k == 1:
        return K[k]
    return Fr(k-1) + Fr(k-2)

k = 10
print Fi(k)
print Fr(k)
