package Tier_1;

public class LengthOfLastWord {
    static int getLen(String str) {
        str = str.trim();

        for (int i = str.length() - 1; i >= 0; i--) {
            if (str.charAt(i) == ' ') {
                System.out.println(str.substring(i + 1, str.length()));
                return str.substring(i + 1, str.length()).length();
            }
        }

        // A new game is here

        return -1;
    }

    public static void main(String[] args) {
        System.out.println(getLen("Hello I am a passionate developer"));
    }
}
