package Tier_3;

public class SetMatrixZeros {
    static void printMatrix(int[][] matrix) {
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[i].length; j++) {
                System.out.print(matrix[j] + " ");
            }
            System.out.println();
        }
    }

    static void setMatrixZeros(int[][] matrix) {
        
    }
    public static void main(String[] args) {
        setMatrixZeros(new int[][] {{1, 1, 1}, {1, 0, 1}, {1, 1, 1}});
    }
}
