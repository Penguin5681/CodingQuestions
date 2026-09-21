package Tier_2;

public class NegativeStockPriceDays {
    static int countYourDays(int[] arr) {
        int negativeGrowthDays = 0;

        for (int i = 0; i < arr.length - 1; i++) {
            if (arr[i + 1] < arr[i]) {
                negativeGrowthDays++;
            }
        }

        return negativeGrowthDays;
    }

    public static void main(String[] args) {
        System.out.println(countYourDays(new int[] { 2, 3, 1, 4, 5, 2 }));
    }
}
