package Tier_1;

public class MissingNumber {
    static int findMissingNumber(int[] numbers, int n) {
        int sum = n * (n + 1) / 2;

        int actualSum = 0;
        for (int number : numbers) {
            actualSum += number;
        }
        
        return Math.abs(sum - actualSum);
    }
    public static void main(String[] args) {
        System.out.println(findMissingNumber(new int[] {2, 3, 4, 5, 6}, 6));
    }
}
