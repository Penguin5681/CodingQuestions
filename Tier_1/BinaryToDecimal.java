package Tier_1;

/**
 * BinaryToDecimal
 */
public class BinaryToDecimal {
    static int getDecimal(String binary) {
        int decimal = 0;
        for (int i = 0; i < binary.length(); i++) {
            decimal = decimal * 2 + (binary.charAt(i) - '0');
        }
        return decimal;
    }

    public static void main(String[] args) {
        testGetDecimal("0", 0);
        testGetDecimal("1", 1);
        testGetDecimal("10", 2);
        testGetDecimal("1010", 10);
        testGetDecimal("11111111", 255);
        System.out.println("All tests passed.");
    }

    private static void testGetDecimal(String binary, int expected) {
        int actual = getDecimal(binary);
        if (actual != expected) {
            throw new AssertionError("For " + binary + ", expected "
                    + expected + " but got " + actual);
        }
    }    
}