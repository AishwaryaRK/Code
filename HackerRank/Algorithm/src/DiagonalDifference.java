import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class DiagonalDifference {

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(bufferedReader.readLine());
		int[][] matrix = new int[n][n];
		String[] s;
		for (int i = 0; i < n; i++) {
			s = bufferedReader.readLine().split(" ");
			for (int j = 0; j < n; j++) {
				matrix[i][j] = Integer.parseInt(s[j]);
			}
		}
		System.out.println(getDiagonalDiff(matrix));

	}

	private static int getDiagonalDiff(int[][] matrix) {
		int d = matrix.length;
		int diag1Sum = 0;
		int diag2Sum = 0;
		for (int i = 0; i < matrix.length; i++) {
			diag1Sum += matrix[i][i];
			d--;
			diag2Sum += matrix[i][d];
		}
		return Math.abs(diag1Sum - diag2Sum);
	}

}
