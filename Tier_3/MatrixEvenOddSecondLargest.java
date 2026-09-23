package Tier_3;

import java.util.ArrayList;
import java.util.Collections;

public class MatrixEvenOddSecondLargest {
    static int solve(int[] arr) {
        ArrayList<Integer> evenArr = new ArrayList<>();
        ArrayList<Integer> oddArr = new ArrayList<>();
        
        for (int i = 0; i < arr.length; i++) {
            if (i % 2 == 0) {
                evenArr.add(arr[i]);
            } else {
                oddArr.add(arr[i]);
            }
        }

        Collections.sort(evenArr);
        Collections.sort(oddArr);

        return evenArr.get(evenArr.size() - 2).intValue() + oddArr.get(oddArr.size() - 2).intValue();
    }
    public static void main(String[] args) {
        System.out.println(solve(new int[] {3, 4, 1, 7, 9}));        
    }
}
