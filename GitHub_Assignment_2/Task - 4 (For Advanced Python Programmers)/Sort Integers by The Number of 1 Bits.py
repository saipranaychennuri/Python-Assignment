def sortByBits(arr):
    def count_bits(n):
        count = 0
        while n > 0:
            if n % 2 == 1:
                count += 1
            n //= 2
        return count

    return sorted(arr, key=lambda x: (count_bits(x), x))
