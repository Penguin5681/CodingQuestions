package Tier_2;

public class SumOfBinaryDistance {
    static int findSum(int n) {
        StringBuilder builder = new StringBuilder("");
        while (n > 0) {
            int curr = n % 2;
            builder.append(curr);
            n /= 2;
        }

        StringBuilder magicalString = new StringBuilder("");

        for (int i = 0; i < builder.toString().length(); i++) {
            if (builder.toString().toCharArray()[i] == '0') {
                magicalString.append(1);
            } else if (builder.toString().toCharArray()[i] == '1') {
                magicalString.append(2);
            }
        }

        int sum = 0;
        for (char ch : magicalString.toString().toCharArray()) {
            if (ch == '1') {
                sum += 1;
            } else {
                sum += 2;
            }
        }

        return sum;
    }

    public static void main(String[] args) {
        System.out.println(findSum(3));
        System.out.println(findSum(0));
        System.out.println(findSum(1));
        System.out.println(findSum(2));
        System.out.println(findSum(4));
        System.out.println(findSum(7));

    }
}
