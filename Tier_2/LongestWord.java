package Tier_2;

public class LongestWord {
    static String returnLongestWord(String sentence) {
        String[] words = sentence.split(" ");
        int maxLength = -1;
        int maxIdx = -1;
        for (int i = 0; i < words.length; i++) {
            if (words[i].length() > maxLength) {
                maxLength = Math.max(maxLength, words[i].length());
                maxIdx = i;
            }
        }        

        return words[maxIdx];
    }
    public static void main(String[] args) {
        System.out.println(returnLongestWord("The quick brown fox"));
        assert returnLongestWord("The quick brown fox") .equals("quick");
        System.out.println(returnLongestWord("Java is fun"));
        assert returnLongestWord("Java is fun") .equals("Java");
        System.out.println(returnLongestWord("one three seven"));
        assert returnLongestWord("one three seven") .equals("three");
        System.out.println(returnLongestWord("hello"));
        assert returnLongestWord("hello") .equals("hello");
        System.out.println(returnLongestWord("yes no number"));
    }
}
