import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.math.BigInteger;

public class AVeryBigSum {

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader bufferedReader=new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(bufferedReader.readLine());
		BigInteger a = new BigInteger("0");
		String[] s = bufferedReader.readLine().split(" ");
		for (int i = 0; i < n; i++) {
			a=a.add(new BigInteger(s[i]));
		}
		System.out.println(a);

	}

}
