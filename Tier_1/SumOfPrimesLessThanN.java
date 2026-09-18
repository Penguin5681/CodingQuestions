package Tier_1;

public class SumOfPrimesLessThanN {
    static boolean isPrime(int n) {
        if (n < 2) return false;
        for (int i = 2; i * i <= n; i++) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }

    static int getPrimeSum(int n) {
        int sum = 0;
        for (int i = 1; i < n; i++) {
            if (isPrime(i)) {
                sum += i;
            }
        }
        return sum;
    }
    public static void main(String[] args) {
        testGetPrimeSum(0, 0);
        testGetPrimeSum(1, 0);
        testGetPrimeSum(2, 0);
        testGetPrimeSum(3, 2);
        testGetPrimeSum(10, 17);
        testGetPrimeSum(20, 77);
        System.out.println("All test cases passed");
    }

    private static void testGetPrimeSum(int n, int expected) {
        int actual = getPrimeSum(n);
        if (actual != expected) {
            throw new AssertionError(
                    "getPrimeSum(" + n + ") expected " + expected + " but got " + actual);
        }
    }
}
