package Tier_1;

public class GooglyPrimeNumbers {
    static int digitSum(int n) {
        int sum = 0;
        while (n > 0) {
            int currentDigit = n % 10;
            sum += currentDigit;
            n /= 10;
        }

        return sum;
    }

    static boolean isPrime(int n) {
        if (n < 2) {
            return false;
        }

        for (int i = 2; i * i <= n; i++) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }

    static boolean isGoggly(int n) {
        return isPrime(n) && isPrime(digitSum(n));
    }

    public static void main(String[] args) {
        testDigitSum();
        testIsPrime();
        testIsGoggly();
        System.out.println("All tests passed.");
    }

    private static void testDigitSum() {
        assertEquals(0, digitSum(0), "digitSum(0)");
        assertEquals(6, digitSum(123), "digitSum(123)");
        assertEquals(15, digitSum(5073), "digitSum(5073)");
    }

    private static void testIsPrime() {
        assertTrue(isPrime(2), "isPrime(2)");
        assertTrue(isPrime(17), "isPrime(17)");
        assertFalse(isPrime(0), "isPrime(0)");
        assertFalse(isPrime(1), "isPrime(1)");
        assertFalse(isPrime(15), "isPrime(15)");
    }

    private static void testIsGoggly() {
        assertTrue(isGoggly(2), "isGoggly(2)");
        assertTrue(isGoggly(23), "isGoggly(23)");
        assertTrue(isGoggly(47), "isGoggly(47)");
        assertFalse(isGoggly(1), "isGoggly(1)");
        assertFalse(isGoggly(13), "isGoggly(13)");
        assertFalse(isGoggly(25), "isGoggly(25)");
        assertFalse(isGoggly(29), "isGoggly(29)");
    }

    private static void assertEquals(int expected, int actual, String testName) {
        if (expected != actual) {
            throw new AssertionError(testName + " expected " + expected + " but got " + actual);
        }
    }

    private static void assertTrue(boolean actual, String testName) {
        if (!actual) {
            throw new AssertionError(testName + " expected true");
        }
    }

    private static void assertFalse(boolean actual, String testName) {
        if (actual) {
            throw new AssertionError(testName + " expected false");
        }
    }
    
}
