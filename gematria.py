# https://fivethirtyeight.com/features/can-you-find-a-number-worth-its-weight-in-letters/
"""If we consider all the whole numbers that are less than their alphanumeric value,
what is the largest of these numbers?"""

print("Highest number less than its alphanumeric value (and its alphanumeric value):")

# map letters to their numerical value
char_vals = {l: v + 1 for v, l in enumerate('abcdefghijklmnopqrstuvwxyz')}


def wordify(n):
    """
    Converts an integer into written English. Eg., 45 -> "forty five"
    :param n: int, 0 < n < 10^15
    :return: string, representing the written-out number
    """

    # group n into sets of three digits, the way they'd be divided by commas
    groups = []
    while n:
        groups.append(n % 1000)
        n //= 1000

    # set some English terms
    thousands = {0: '', 1: ' thousand', 2: ' million', 3: ' billion', 4: ' trillion'}
    tens = {2: ' twenty', 3: ' thirty', 4: ' forty', 5: ' fifty',
            6: ' sixty', 7: ' seventy', 8: ' eighty', 9: ' ninety'}
    teens = {10: ' ten', 11: ' eleven', 12: ' twelve', 13: ' thirteen',
             14: ' fourteen', 15: ' fifteen', 16: ' sixteen',
             17: ' seventeen', 18: ' eighteen', 19: ' nineteen'}
    ones = {1: ' one', 2: ' two', 3: ' three', 4: ' four', 5: ' five',
            6: ' six', 7: ' seven', 8: ' eight', 9: ' nine'}

    # each group is converted to a str, stored in result
    result = []
    for thousand, group in enumerate(groups):
        # get the hundreds, tens, and one-place values for the group
        hundred = group // 100
        ten = group % 100 // 10
        one = group % 10
        group_result = ''
        if hundred:
            group_result += f"{ones[hundred]} hundred"
        if ten == 1:
            group_result += teens[group % 100]
        else:
            if ten:
                group_result += tens[ten]
            if one:
                group_result += ones[one]
        group_result += thousands[thousand]
        result.append(group_result)
    return ' '.join(reversed(result))


# converts a number to an English string, then calculates the numeric score of that string
def score(n): return sum(char_vals[c] for c in wordify(n) if c.isalpha())


# find the highest number for which the number is less than its numeric score
def get_highest():
    for i in range(1000, 0, -1):
        if i < score(i):
            return f"{i} ({score(i)})"


print(get_highest())
