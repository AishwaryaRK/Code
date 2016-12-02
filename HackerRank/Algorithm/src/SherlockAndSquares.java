
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class SherlockAndSquares {

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
		int t = Integer.parseInt(bufferedReader.readLine());
		String[] s;
		for (int i = 0; i < t; i++) {
			s = bufferedReader.readLine().split(" ");
			int a = Integer.parseInt(s[0]);
			int b = Integer.parseInt(s[1]);
			// System.out.println(getSquares(a, b));
			System.out.println(getNumberOfSquares(a, b));
		}
	}

	private static int getNumberOfSquares(int a, int b) {
		int numberOfSquares = 0;
		double sqrtA = Math.sqrt(a);
		double sqrtB = Math.sqrt(b);
		return (int) Math.floor(sqrtB) - (int) Math.ceil(sqrtA) + 1;
	}

	// private static int getSquares(int a, int b) {
	// int numberOfSquares = 0;
	// for (int i = a; i <= b; i++) {
	// if (isPerfectSquare(i)) {
	// numberOfSquares++;
	// }
	// }
	// return numberOfSquares;
	// }
	//
	// private static boolean isPerfectSquare(int n) {
	// String sum = n + "";
	// int unitPlaceDigit = Integer.parseInt(sum.charAt(sum.length() - 1) + "");
	// while (sum.length() != 1) {
	// sum = getDigitsSum(Integer.parseInt(sum));
	// }
	// int digitalRoot = Integer.parseInt(sum);
	// if ((unitPlaceDigit != 2 && unitPlaceDigit != 3 && unitPlaceDigit != 7 &&
	// unitPlaceDigit != 8)
	// && (digitalRoot == 1 || digitalRoot == 4 || digitalRoot == 7 ||
	// digitalRoot == 9)) {
	// double sqrt = Math.sqrt(n);
	// if (sqrt - (int) sqrt == 0) {
	// return true;
	// }
	// return false;
	// }
	// return false;
	// }
	//
	// private static String getDigitsSum(int n) {
	// char[] number = (n + "").toCharArray();
	// int sum = 0;
	// for (char c : number) {
	// sum += Integer.parseInt(c + "");
	// }
	// return sum + "";
	// }

}