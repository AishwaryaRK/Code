import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class SolveMeFirst {

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader bufferedReader=new BufferedReader(new InputStreamReader(System.in));
		int a = Integer.parseInt(bufferedReader.readLine());
		int b = Integer.parseInt(bufferedReader.readLine());
		System.out.println(add(a, b));

	}

	private static int add(int a, int b) {
		return a + b;
	}

}
