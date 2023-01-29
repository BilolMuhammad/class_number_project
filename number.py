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
        for n in range(1, self.value+1):
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
        return list

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
        sum = 0
        value = self.value
        while value:
            num = value % 10
            sum += num
            value //= 10
        return sum/len(self.value)

    def get_median(self):
        """
        Returns the median of all the digits in the number.

        returns: float
        """
        data = self.get_digits()
        leng = len(data)
        sum = 0
        for d in data:
            sum += d
        return sum/leng

    def get_range(self):
        """
        Returns the range of all the digits in the number.

        returns: list
        """
        data = self.get_digits()
        max = data[0]
        min = data[0]

        for d in data:
            if d > max:
                max = d
            if d < min:
                min = d
        return max-min

        # data = self.get_digits()
        # return max(data)-min(data)

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
        return frequency


# Create a new instance of Number
number = Number(3)
