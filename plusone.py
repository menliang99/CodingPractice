def plusOne(digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        l = len(digits)
        if l == 0:
            return None
        carry = 1  
	print l
        for i in range (l-1, -1, -1):
	    print i
            newdig = (digits[i] + carry) % 10
            carry = (digits[i] + carry) / 10
            digits[i] = newdig
        
        if carry > 0:
            digits.insert(0, carry)
        
        return digits

digits = [0]
print plusOne(digits)
