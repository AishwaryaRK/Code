
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class CutTheSticks {

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(bufferedReader.readLine());
		String[] s = bufferedReader.readLine().split(" ");
		List<Integer> stickLenghts = new ArrayList<Integer>();
		for (int i = 0; i < n; i++) {
			stickLenghts.add(Integer.parseInt(s[i]));
		}
		while (stickLenghts.size() > 0) {
			System.out.println(stickLenghts.size());
			stickLenghts = printSticksRemaining(stickLenghts);
		}

	}

	private static List<Integer> printSticksRemaining(List<Integer> stickLenghts) {
		int min = Collections.min(stickLenghts);
		List<Integer> newStickLengths = new ArrayList<Integer>();
		for (Integer stickLength : stickLenghts) {
			if (stickLength - min > 0) {
				newStickLengths.add(stickLength - min);
			}
		}
		return newStickLengths;
	}

}
