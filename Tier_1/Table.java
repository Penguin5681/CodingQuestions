package Tier_1;

public class Table {
    static void printTableAndSumOfMultiples(int n) {
        int sum = 0;
        for (int i = 1; i <= 10; i++) {
            System.out.println(n + " x " + i + " = " + n * i);
            sum += (n * i);
        }
        System.out.println("Sum of 10 multiples of " + n + " is: " + sum);
    }
    public static void main(String[] args) {
        printTableAndSumOfMultiples(5);  
    }
}
