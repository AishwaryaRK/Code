
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.math.BigInteger;

public class ExtraBigFactorial {

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
		BigInteger N = new BigInteger(bufferedReader.readLine());
		for (int i = N.intValue() - 1; i > 1; i--) {
			N = N.multiply(BigInteger.valueOf(i));
		}
		System.out.println(N);
	}

}
