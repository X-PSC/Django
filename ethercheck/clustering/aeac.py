#Automatic Etherium Address Clustering
#Based on http://bitfury.com/content/5-white-papers-research/clustering_whitepaper.pdf

from collections import namedtuple

Transaction = namedtuple("Transaction", "A B c")

def addr(A):
    return filter(lambda a_i , A_i : A_i , A)

def common_spending(t: Transaction) :
    return True

def one_time_change(t: Transaction) :
    addr_A = addr(t.A)
    addr_B = addr(t.B)
    if len(addr_B) != 2 :
        return False
    elif len(addr_A) == 2:
        return False
    elif (addr_B[0] in addr_A) or (addr_B[1] in addr_A) :
        return False
    return True

print("coucou")




