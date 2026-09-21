package Tier_2;

public class MoveHyphenstoFront {
    static String movedString(String string) {
        int hCount = 0;
        for (char ch : string.toCharArray()) {
            if (ch == '-') {
                hCount++;
            }
        }
        
        StringBuilder builder = new StringBuilder("-".repeat(hCount));

        for (char ch : string.toCharArray()) {
            if (ch != '-') {
                builder.append(ch);
            }
        }        

        return builder.toString();
    }
    // Move-Hyphens-to-Front
    public static void main(String[] args) {
        String[] testCases = {
            "Move-Hyphens-to-Front",
            "---hello-world",
            "hello---world",
            "hello world",
            "---",
            ""
        };

        for (String testCase : testCases) {
            System.out.println("Input:  " + testCase);
            System.out.println("Output: " + movedString(testCase));
            System.out.println();
        }
    }
}
