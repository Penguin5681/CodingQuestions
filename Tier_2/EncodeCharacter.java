package Tier_2;

public class EncodeCharacter {
    static String encodedString(int n) {
        StringBuilder bStringBuilder = new StringBuilder("");
        while (n > 0) {
            int digit = n % 10;
            bStringBuilder.insert(0, digit * digit);
            n /= 10;
        }

        return bStringBuilder.toString();
    }

    public static void main(String[] args) {
        System.out.println(encodedString(34));
        System.out.println(encodedString(12));
        System.out.println(encodedString(56));
        System.out.println(encodedString(907));
    }
}
