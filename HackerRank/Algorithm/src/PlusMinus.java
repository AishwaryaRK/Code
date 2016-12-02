
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class PlusMinus {

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(bufferedReader.readLine());
		String[] s = bufferedReader.readLine().split(" ");
		int[] a = new int[n];
		for (int i = 0; i < n; i++) {
			a[i] = Integer.parseInt(s[i]);
		}
		printFractions(a);

	}

	private static void printFractions(int[] a) {
		float n = a.length;
		int positiveNumberCount = 0;
		int negativeNumberCount = 0;
		int zeroCount = 0;
		for (int i = 0; i < a.length; i++) {
			if (a[i] > 0) {
				positiveNumberCount++;
			} else {
				if (a[i] < 0) {
					negativeNumberCount++;
				} else {
					zeroCount++;
				}
			}
		}
		System.out.println(positiveNumberCount/n);
		System.out.println(negativeNumberCount/n);
		System.out.print(zeroCount/n);
	}

}
