
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class SherlockAndTheBeast {

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(bufferedReader.readLine());
		for (int i = 0; i < n; i++) {
			int numberOfDigits = Integer.parseInt(bufferedReader.readLine());
			System.out.println(getDecentNumber(numberOfDigits));
		}
	}

	private static StringBuilder getDecentNumber(int numberOfDigits) {
		int numberOfFives = numberOfDigits;
		int numberOfThrees = 0;
		while (true) {
			if (numberOfFives < 0) {
				return new StringBuilder("-1");
			}
			if (numberOfFives % 3 == 0) {
				break;
			}
			numberOfFives -= 5;
			numberOfThrees += 5;
		}
		StringBuilder decentNumber = new StringBuilder("");
		for (int i = 1; i <= numberOfFives; i+=3) {
			decentNumber.append("555");
			//decentNumber += "555";
		}
		for (int i = 1; i <= numberOfThrees; i+=5) {
			decentNumber.append("33333");
			//decentNumber += "33333";
		}
		return decentNumber;
	}

}