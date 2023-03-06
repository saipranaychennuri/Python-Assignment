class Solution(object):
    def singleNumber(self, nums):
        # XOR all elements to get XOR of the two unique elements
        xor_result = 0
        for num in nums:
            xor_result ^= num
            
        # Get the rightmost set bit in the XOR result
        rightmost_set_bit = 1
        while xor_result & rightmost_set_bit == 0:
            rightmost_set_bit <<= 1
            
        # Divide the elements in the array into two groups based on the rightmost set bit
        group1 = 0
        group2 = 0
        for num in nums:
            if num & rightmost_set_bit:
                group1 ^= num
            else:
                group2 ^= num
                
        return [group1, group2]

s = Solution()
print(s.singleNumber([1,2,1,3,2,5]))
