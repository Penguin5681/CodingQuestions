package Tier_2;

public class CountCarry {
    static int carryCounter(int num1, int num2) {
        int carryCount = 0;
        int currentCarry = 0;

        while (num1 != 0 || num2 != 0) {
            int num1LD = num1 % 10;
            int num2LD = num2 % 10;

            if (currentCarry + num1LD + num2LD > 9) {
                currentCarry = 1;
                carryCount++;
            } else {
                currentCarry = 0;
            }

            num1 /= 10;
            num2 /= 10;
        }

        return carryCount;
    }
    public static void main(String[] args) {
        testCarryCounter(0, 0, 0);
        testCarryCounter(5, 4, 0);
        testCarryCounter(9, 1, 1);
        testCarryCounter(99, 1, 1);
        testCarryCounter(99, 99, 2);
        testCarryCounter(123, 456, 0);
        testCarryCounter(555, 555, 3);
    }

    private static void testCarryCounter(int num1, int num2, int expected) {
        int actual = carryCounter(num1, num2);
        if (actual != expected) {
            throw new AssertionError(
                    "carryCounter(" + num1 + ", " + num2 + ") expected "
                            + expected + " but was " + actual);
        }
    }
}
