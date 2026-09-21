package Tier_2;

public class MaxExponentOf2 {
    static int countTwos(int n) {
        int count = 0;
        while (n > 0) {
            n /= 2;
            count++;
        }
        return count;
    }

    static int maxExponent(int a, int b) {
        int maxExponent = -1;
        int result = a;
        for (int i = a; i <= b; i++) {
            int exponent = countTwos(i);
            if (exponent > maxExponent) {
                maxExponent = exponent;
                result = i;
            } else if (exponent == maxExponent && i < result) {
                result = i;
            }
        }        
        return result;
    }

    public static void main(String[] args) {
        System.out.println(maxExponent(7, 12));
    }
}
