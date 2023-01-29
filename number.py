class Number:
    def __init__(self, value: int):
        self.value = value

    def get_number(self):
        """
        Returns the number.

        returns: int
        """
        return self.value

    def is_odd(self):
        """
        Returns True if the number is odd, otherwise False.

        returns: bool

        """
        return self.value % 2 == 1

    def is_even(self):
        """
        Returns True if the number is even, otherwise False. 

        returns: bool
        """
        return self.value % 2 == 0

    def is_prime(self):
        """
        Returns True if the number is prime, otherwise False.

        returns: bool
        """
        count = 0
        for num in range(2, self.value):
            if self.value % num == 0:
                count += 1
        if count == 0:
            return True
        else:
            return False

    def get_divisors(self):
        """
        Returns a list of all the divisors of the number.

        returns: list
        """
        list = []
        value = self.value
        for n in range(1, value+1):
            if value % n == 0:
                list.append(n)
        return list

    def get_length(self):
        """
        Returns the number of digits in the number.

        returns: int
        """
        return len(str(self.value))

    def get_sum(self):
        """
        Returns the sum of all the digits in the number.

        returns: int
        """
        num_value = self.value
        sum = 0
        while num_value:
            sum += num_value % 10
            num_value //= 10
        return sum

    def get_reverse(self):
        """
        Returns the number in reverse.

        returns: int
        """
        value = self.value
        rev = 0
        while value:
            dig = value % 10
            rev = rev*10+dig
            value //= 10
        return rev

    def is_palindrome(self):
        """
        Returns True if the number is a palindrome, otherwise False.

        returns: bool
        """
        d = self.get_digits()
        n = len(d)
        if n % 2 == 0:
            return d[:n//2] == d[:n//2-1:-1]
        else:
            return d[:n//2] == d[:n//2:-1]

        #      d==d[::-1]

    def get_digits(self):
        """
        Returns a list of all the digits in the number.

        returns: list
        """
        list = []
        value = self.value

        while value > 0:
            num = value % 10
            list.append(num)
            value //= 10
        if len(list) == 0:
            list.append(0)
        return list[::-1]

    def get_max(self):
        """
        Returns the largest digit in the number.

        returns: int
        """
        value = self.value
        lis = []
        while value:
            dig = value % 10
            lis.append(dig)
            value //= 10
        max = lis[0]
        for n in range(1, len(lis)):
            if lis[n] > max:
                max = lis[n]
        return max

    def get_min(self):
        """
        Returns the smallest digit in the number.

        returns: int
        """
        value = self.value
        list = []
        while value:
            dig = value % 10
            list.append(dig)
            value //= 10
        min = list[0]
        for n in range(1, len(list)):
            if list[n] < min:
                min = list[n]
        return min

    def get_average(self):
        """
        Returns the average of all the digits in the number.

        returns: float
        """
        data = self.get_digits()
        return sum(data)/len(data)
        # sum = 0
        # value = self.value
        # list = []
        # while value:
        #     num = value % 10
        #     sum += num
        #     list.append(num)
        #     value //= 10
        # return sum/len(list)

    def get_median(self):
        """
        Returns the median of all the digits in the number.

        returns: float
        """
        data = self.get_digits()
        data.sort()
        leng = len(data)
        median = 0
        m1 = 0
        m2 = 0
        if leng % 2 == 1:
            median = data[leng//2]
        else:
            m1 = data[leng//2-1]
            m2 = data[leng//2]
            median = (m1+m2)/2
        return float(median)

    def get_range(self):
        """
        Returns the range of all the digits in the number.

        returns: list
        """
        data = self.get_digits()
        return [min(data), max(data)]

    def get_frequency(self):
        """
        Returns a dictionary of the frequency of each digit in the number.

        returns: dict
        """
        data = self.get_digits()
        frequency = {}

        for d in data:
            if d in frequency:
                frequency[d] += 1
            else:
                frequency[d] = 1
        if len(frequency) == 0:
            frequency[0] = 1
        else:
            frequency
        return frequency


# Create a new instance of Number
number = Number(3)
