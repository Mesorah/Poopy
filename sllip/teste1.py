class P:
    def __init__(self, n):
        self.n = n
        


class G(P):
    def __init__(self, n, k):
        super().__init__(n)

        print(n, k)



gagf = G('no', 'kkkk')