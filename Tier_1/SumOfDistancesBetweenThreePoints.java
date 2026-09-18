package Tier_1;

public class SumOfDistancesBetweenThreePoints {
    static double distanceHelper(int x1, int y1, int x2, int y2) {
        return Math.sqrt(Math.pow(x2 - x1, 2) + Math.pow(y2 - y1, 2));
    }

    static double distanceSum() {
        int x1 = 1;
        int y1 = 2;

        int x2 = 2;
        int y2 = 4;

        int x3 = 3;
        int y3 = 6;

        double sum = 0;

        sum += distanceHelper(x1, y1, x2, y2);
        sum += distanceHelper(x1, y1, x3, y3);
        sum += distanceHelper(x2, y2, x3, y3);

        return sum;
    }

    public static void main(String[] args) {
        System.out.println(distanceSum());
    }
}
