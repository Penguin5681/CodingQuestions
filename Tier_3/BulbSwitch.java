package Tier_3;

import java.util.Arrays;

public class BulbSwitch {
    static int findMinSwitches(int[] arr) {
        int count = 0;
        int flipped = 0;
        for (int i = 0; i < arr.length; i++) {
            int current = arr[i] ^ flipped;

            if (current == 0) {
                count++;
                flipped = flipped ^ 1;
            }
        }

        return count;
    }

    public static void main(String[] args) {
        System.out.println(findMinSwitches(new int[] {0, 1, 0, 1}));
        System.out.println(findMinSwitches(new int[] {1, 0, 0, 0, 0}));
    }
}
