package Tier_1;

public class DecimalToBinary {
    static String getBinary(int decimal) {
        if (decimal == 0) {
            return "0";
        }

        StringBuilder rsl = new StringBuilder("");
        while (decimal > 0) {
            int currentRemainder = decimal % 2;
            rsl.append(currentRemainder);
            decimal /= 2;
        }
        return rsl.reverse().toString();
    }

    public static void main(String[] args) {
        assertBinary(0, "0");
        assertBinary(1, "1");
        assertBinary(2, "10");
        assertBinary(5, "101");
        assertBinary(10, "1010");
        assertBinary(255, "11111111");
        System.out.println("All tests passed.");
    }

    private static void assertBinary(int decimal, String expected) {
        String actual = getBinary(decimal);
        if (!expected.equals(actual)) {
            throw new AssertionError(
                    "Expected " + expected + " for " + decimal + ", but got " + actual);
        }
    }
}
