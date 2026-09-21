package Tier_3;

public class MaxFavouriteSong {
    static int countA(String songs) {
        int count = 0;
        for (char ch : songs.toCharArray()) {
            if (ch == 'a') {
                count++;
            }
        }
        return count;
    }

    static int maxFavouriteSong(String songs, int k) {
        int maxA = -1;

        for (int i = 0; i <= songs.length() - k; i++) {
            String currSubString = songs.substring(i, i + k);
            maxA = Math.max(maxA, countA(currSubString));
        }

        return maxA;
    }
    public static void main(String[] args) {
        System.out.println(maxFavouriteSong("acdbaaca", 3));
    }
}
