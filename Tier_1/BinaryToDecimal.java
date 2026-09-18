package Tier_1;

/**
 * BinaryToDecimal
 */
public class BinaryToDecimal {
    static int getDecimal(String binary) {
        int decimal = 0;
        for (int i = 0; i < binary.length(); i++) {
            decimal = decimal * 2 + (binary.charAt(i) - '0');
        }
        return decimal;
    }

    public static void main(String[] args) {
        System.out.println(getDecimal("0") == 0);
        System.out.println(getDecimal("1") == 1);
        System.out.println(getDecimal("101") == 5);
        System.out.println(getDecimal("1010") == 10);
        System.out.println(getDecimal("11111111") == 255);
    }    
}