
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class UtopianTree {

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
		int t = Integer.parseInt(bufferedReader.readLine());
		for (int i = 0; i < t; i++) {
			int n = Integer.parseInt(bufferedReader.readLine());
			System.out.println(getTreeHeight(n));
		}
	}

	private static int getTreeHeight(int n) {
		int height = 1;
		for (int i = 1; i <= n; i++) {
			if (i % 2 == 0) {
				height++;
			} else {
				height *= 2;
			}
		}
		return height;
	}

}