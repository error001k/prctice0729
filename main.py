class PrimeLister:
    def __init__(self, n):
        self.n = n

    def is_prime(self, num):
        if num <= 1:
            return False
        if num <= 3:
            return True
        for i in range(2,num):
            if num % i == 0 :
                return False
            else :
                return True

    def list_primes(self):
        primes = []
        for num in range(2, self.n + 1):
            if self.is_prime(num):
                primes.append(num)
        return primes

# 實際使用
n = int(input("請輸入一個正整數:"))
lister = PrimeLister(n)
primes = lister.list_primes()
print(f"Prime numbers between 0 and {n}: {primes}")