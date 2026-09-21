package Tier_2;

/**
 * EquilibriumSum
 */
public class EquilibriumSum {
    static int getIndex(int[] arr) {
        int totalSum = 0;
        int leftSum = 0;
        int rightSum = 0;

        for (int i = 0; i < arr.length; i++) totalSum += arr[i];

        for (int i = 0; i < arr.length; i++) {
            rightSum = totalSum - leftSum - arr[i];
            if (rightSum == leftSum) return i;
            leftSum += arr[i];
        }

        return -1;
    }
    public static void main(String[] args) {
        System.out.println(getIndex(new int[] {3, 4, 3, 1, 6}));
    }
}