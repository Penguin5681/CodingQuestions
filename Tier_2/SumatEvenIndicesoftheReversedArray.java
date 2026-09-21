package Tier_2;

public class SumatEvenIndicesoftheReversedArray {
    static int getSum(int[] arr) {
        int left = 0;
        int right = arr.length - 1;
        
        while (left < right) {
            int temp = arr[left];
            arr[left] = arr[right];
            arr[right] = temp;

            left++; right--;
        }

        int sum = 0;

        for (int i = arr.length - 1; i >= 0; i--) {
            if (i % 2 == 0) {
                sum += arr[i];
            }
        }

        return sum;
    }
    public static void main(String[] args) {
        System.out.println(getSum(new int[] {10, 20, 30, 40, 50, 60}));
    }
}
