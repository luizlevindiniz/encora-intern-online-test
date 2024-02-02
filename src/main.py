from typing import Union
from constants import QUARTERS_VALUE, PENNIES_VALUE, NICKELS_VALUE, DIMES_VALUE

"""
    The following class contains 2 functions, which, combined, will return a set
    of tuples containing all possible combinations to represent the change in 
    terms of quarters, dimes, nickels and pennies.

    To calculate the output, the following function will be used:

    number = QUARTERS_VALUE*x + DIMES_VALUE*y + NICKELS_VALUE*z + PENNIES_VALUE*w; 
    where x,y,z,w and number are non-negative integers.

    Input: non-negative integer
    Output: set of tuples containing all possible change possibilities

    Examples:

    If the input is 12, then the output will be:
    [[0,0,0,12], [0,0,1,7], [0,0,2,2], [0,1,0,2]]

"""


class Solution(object):

    # auxiliar method - perform calculation
    def calculate_needed_coins(
        self,
        number: int,
        answer: set,
        quarters: int,
        nickels: int,
        dimes: int,
        pennies: int,
        list_of_coins: list,
    ) -> None:

        # recursion stop condition! number == 0 will ALWAYS be reached since
        # we are subtracting 25, 10, 5 or 1 from number at each iteration
        if number == 0:
            # set is an immutable so add inside function scope is reflecting
            # in main scope
            answer.add((quarters, dimes, nickels, pennies))
            return None

        # Calculating all possible numbers of quarters coins
        if number >= QUARTERS_VALUE:
            list_of_coins[0] += 1
            self.calculate_needed_coins(
                number=number - QUARTERS_VALUE,
                answer=answer,
                quarters=quarters + 1,
                dimes=dimes,
                nickels=nickels,
                pennies=pennies,
                list_of_coins=list_of_coins,
            )
            list_of_coins[0] -= 1

        # Calculating all possible numbers of dimes coins
        if number >= DIMES_VALUE:
            list_of_coins[1] += 1
            self.calculate_needed_coins(
                number=number - DIMES_VALUE,
                answer=answer,
                quarters=quarters,
                dimes=dimes + 1,
                nickels=nickels,
                pennies=pennies,
                list_of_coins=list_of_coins,
            )
            list_of_coins[1] -= 1

        # Calculating all possible numbers of nickels coins
        if number >= NICKELS_VALUE:
            list_of_coins[2] += 1
            self.calculate_needed_coins(
                number=number - NICKELS_VALUE,
                answer=answer,
                quarters=quarters,
                dimes=dimes,
                nickels=nickels + 1,
                pennies=pennies,
                list_of_coins=list_of_coins,
            )
            list_of_coins[2] -= 1

        # Calculating all possible numbers of pennies coins
        if number >= PENNIES_VALUE:
            list_of_coins[3] += 1
            self.calculate_needed_coins(
                number=number - PENNIES_VALUE,
                answer=answer,
                quarters=quarters,
                dimes=dimes,
                nickels=nickels,
                pennies=pennies + 1,
                list_of_coins=list_of_coins,
            )
            list_of_coins[3] -= 1

    # main method
    def make_changes(self, number: int) -> Union[set[tuple], None]:
        # this empty set will hold our answer
        answer = set()

        # critical case: number less than 0
        if number < 0:
            print("Error! Integer must be positive!")
            return None

        # critical case: floating number
        if isinstance(number, float):
            print("Error! Number must be a positive integer!")
            return None

        # edge case:
        if number == 0:
            answer.add((0, 0, 0, 0))

        # base case:

        # list to count used coins in a iteration, quarters, dimes, nickels
        # and pennies all start at 0
        list_of_coins = [0, 0, 0, 0]

        self.calculate_needed_coins(
            number=number,
            answer=answer,
            quarters=0,
            dimes=0,
            nickels=0,
            pennies=0,
            list_of_coins=list_of_coins,
        )

        return answer


if __name__ == "__main__":
    s = Solution()

    print(s.make_changes(0))  # {(0, 0, 0, 0)}
    print(s.make_changes(-1))  # ERROR!
    print(s.make_changes(12))  # {(0,0,0,12), (0,0,1,7), (0,0,2,2), (0,1,0,2)}
    print(s.make_changes(12.55))  # ERROR!
