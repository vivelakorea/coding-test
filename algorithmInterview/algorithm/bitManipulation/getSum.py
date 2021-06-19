class Solution:
    def getSum(self, a: int, b: int):
        MASK = 0xFFFFFFFF
        MAX_INT = 0x7FFFFFFF

        a_bin = bin(a & MASK)[2:].zfill(32)
        b_bin = bin(b & MASK)[2:].zfill(32)

        result_ = []
        carry_in_ = 0
        carry_out_ = 0
        sum_ = 0

        for i in range(32):
            A = int(a_bin[31 - i])
            B = int(b_bin[31 - i])
            Q1_ = A & B
            Q2_ = A ^ B
            Q3_ = Q2_ & carry_in_
            sum_ = carry_in_ ^ Q2_
            carry_out_ = Q1_ | Q3_

            # print('A: {}, B: {}, C_in: {}, sum: {}, C_out: {}'.format(A, B, carry_in_, sum_, carry_out_))
            result_.append(str(sum_))
            carry_in_ = carry_out_
        
        result = int(''.join(result_[::-1]), 2) & MASK
        if result > MAX_INT:
            result = ~(result ^ MASK)
        return result


s = Solution()
print(s.getSum(1, 2))
print(s.getSum(2, 3))
print(s.getSum(-1, 2))
print(s.getSum(-1, -2))