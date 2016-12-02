import java.io.*;
import java.util.Arrays;

public class CandidateCode1 {

	public static void main(String[] args) {
		int[] left = { 2, 1, 1, 0 };
		int[] arrangement = uniqueValue(4, left);
		for (int i = 0; i < arrangement.length; i++) {
			System.out.print(arrangement[i] + ",");
		}
	}

	public static int[] uniqueValue(int n, int[] left) {
		int[] arrangement = new int[n];
		for (int i = 0; i < left.length; i++) {
			int leftValue = left[i];
			System.out.println("person = "+i+", leftValue = "+leftValue);
			for (int j = leftValue; j < arrangement.length; j++) {
				if (arrangement[j] <= 0) {
					arrangement[j] = i + 1;
					break;
				}
			}
		}
		return arrangement;
	}
}