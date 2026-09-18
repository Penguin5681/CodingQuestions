package Tier_1;

import java.io.ByteArrayOutputStream;
import java.io.PrintStream;

public class StandardDeviation {
    static void deviation(int[] numbers) {
        int mean = 0;
        for (int number : numbers) {
            mean += number;
        }

        mean /= numbers.length;

        int msd = 0;
        int sum = 0;
        for (int i = 0; i < numbers.length; i++) {
            sum += (numbers[i] - mean) * (numbers[i] - mean);
        }

        msd = sum / numbers.length;

        System.out.println("MEAN: " + mean);
        System.out.println("MSD: " + msd);
    }
    public static void main(String[] args) {
        testDeviation(new int[]{1, 2, 3, 4, 5}, "MEAN: 3\nMSD: 2\n");
        testDeviation(new int[]{5, 5, 5}, "MEAN: 5\nMSD: 0\n");
        testDeviation(new int[]{-2, 0, 2}, "MEAN: 0\nMSD: 2\n");
        System.out.println("All tests passed.");
    }

    private static void testDeviation(int[] numbers, String expected) {
        ByteArrayOutputStream output = new ByteArrayOutputStream();
        PrintStream originalOut = System.out;
        try {
            System.setOut(new PrintStream(output));
            deviation(numbers);
        } finally {
            System.setOut(originalOut);
        }

        String actual = output.toString().replace(System.lineSeparator(), "\n");
        if (!actual.equals(expected)) {
            throw new AssertionError("Expected:\n" + expected + "Actual:\n" + actual);
        }
    }
}
