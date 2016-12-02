import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class SimpleArraySum {

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader bufferedReader=new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(bufferedReader.readLine());
		int[] a = new int[n];
		String[] s = bufferedReader.readLine().split(" ");
		for (int i = 0; i < n; i++) {
			a[i] = Integer.parseInt(s[i]);
		}
		System.out.println(arraySum(a));

	}

	private static int arraySum(int[] a) {
		int sum = 0;
		for (int i = 0; i < a.length; i++) {
			sum+=a[i];
		}
		return sum;
	}

}
