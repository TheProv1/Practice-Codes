/*
Fibonacci

The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, 
such that each number is the sum of the two preceding ones, starting from 0 and 1
*/


class Solution {
    public int fib(int n) {
        int num1 = 0;
        int num2 = 1;
        int num3 = 0;

        if (n == 1){
            return num2;
        }

        while (n > 1){
            num3 = num1 + num2;
            num1 = num2;
            num2 = num3;
            n--;
        }
        return num3;
    }
}
