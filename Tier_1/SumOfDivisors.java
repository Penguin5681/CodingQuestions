package Tier_1;

public class SumOfDivisors {
    static int getSumOfDivisors(int n) {
        int sum = 0;
        for (int i = 1; i <= Math.sqrt(n); i++) {
            if (n % i == 0) {
                sum += i;

                if (i != n / i) {
                    sum += n / i;
                }
            }
        }
        return sum;
    }
    public static void main(String[] args) {
        testGetSumOfDivisors();
    }

    private static void testGetSumOfDivisors() {
        assertSumOfDivisors(1, 0);
        assertSumOfDivisors(2, 1);
        assertSumOfDivisors(6, 6);
        assertSumOfDivisors(12, 16);
        assertSumOfDivisors(25, 6);
        System.out.println("All test cases passed");
    }

    private static void assertSumOfDivisors(int input, int expected) {
        int actual = getSumOfDivisors(input);
        if (actual != expected) {
            throw new AssertionError("Expected " + expected + " for input " + input + ", but got " + actual);
        }
    }
}
