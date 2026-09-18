package Tier_1;

public class FirstKWords {
    static String firstK(String str, int k) {
        
        StringBuilder bStringBuilder = new StringBuilder("");
        String[] words = str.split(" ");

        for (int i = 0; i < k && i < str.length(); i++) {
            bStringBuilder.append(words[i] + " ");
        }

        return bStringBuilder.toString();
    }
    
    public static void main(String[] args) {
        System.out.println(firstK("Hello I am a passionate developer", 4));
    }
}
