import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class DivideByZero {

	public static void main(String[] args) {
		int[] numbers = { 9, 2 };
		System.out.println(CountNumbers(numbers));
	}

	public static int CountNumbers(int[] numbers) {
		List<Integer> nums = new ArrayList<Integer>();
		for (Integer n : numbers) {
			nums.add(n);
		}
		for (int i = 0; i < nums.size(); i++) {
			for (int j = 0; j < nums.size(); j++) {
				int n = nums.get(i) / nums.get(j);
				if (!nums.contains(n) && n != 0 && j != i) {
					nums.add(n);
				}
			}
		}
		return nums.size();
	}

}
