import java.util.HashMap;
import java.util.Map;

public class ManySquares {

	public static void main(String[] args) {
		int[] sticks = { 1, 3, 3, 6, 2, 1, 6, 1, 6, 3, 1, 1, 6, 6, 6, 3 };
		System.out.println(howManySquares(sticks));
	}

	public static int howManySquares(int[] sticks) {
		int numOfSquares = 0;
		Map<Integer, Integer> lengthsCount = new HashMap<Integer, Integer>();
		for (int length : sticks) {
			if (lengthsCount.containsKey(length)) {
				int count = lengthsCount.get(length) + 1;
				lengthsCount.put(length, count);
				if (count % 4 == 0) {
					numOfSquares++;
				}
			} else {
				lengthsCount.put(length, 1);
			}
		}
		return numOfSquares;
	}

}
