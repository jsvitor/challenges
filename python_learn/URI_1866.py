'''
Two friends ask the attendant a snack bar propose a challenge , so that whoever hit him more,
would not pay the bill. Then the following is proposed : Given the following sum below report
the result , with the same number of terms : S = 1 - 1 + 1 - 1 + 1 - 1 + 1 - 1 ... Write a program
that , given a number of terms, report the result of the sum above.

Input
An integer C shall be informed, which is the amount of test cases.
Each test case starts with an integer N ( 1 ≤ N ≤ 1000), indicating the number of terms of the sum .

Output
For each test case print a number S , which is the sum of N terms of expression.

Input Sample	Output Sample
3                     1
11                    1
7                     1
18                    0
'''

# resultado da soma
def S(C):
    if((C//2)==0 or (C==1)):
        return 0
    else:
        return 1

print(S(int(input())))

