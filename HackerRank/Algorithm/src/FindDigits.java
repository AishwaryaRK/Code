
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class FindDigits {

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
		int t = Integer.parseInt(bufferedReader.readLine());
		for (int i = 0; i < t; i++) {
			String n = bufferedReader.readLine();
			System.out.println(getNumberOfEvenlyDividingDigits(n));
		}
	}

	private static int getNumberOfEvenlyDividingDigits(String n) {
		int numberOfEvenlyDividingDigits = 0;
		char[] number = n.toCharArray();
		int N = Integer.parseInt(n);
		for (char c : number) {
			if (c != '0' && N % Integer.parseInt(c + "") == 0) {
				numberOfEvenlyDividingDigits++;
			}
		}
		return numberOfEvenlyDividingDigits;

	}

}