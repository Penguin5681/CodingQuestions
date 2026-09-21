package Tier_2;

public class RearrangementOfBits {
    static int rearrangeBits(int n) {
        int result = 0;
        int count = Integer.bitCount(n);

        while (count > 0) {
            result = (result << 1) | 1;
            count--;
        }
        return result;
    }
    public static void main(String[] args) {
        System.out.println(rearrangeBits(2));  
    }
}
