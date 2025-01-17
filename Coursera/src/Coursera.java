import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Coursera {

	public static void main(String[] args) throws IOException {
		String[] arr = new String[4];
		arr[0] = "1112";
		arr[1] = "1912";
		arr[2] = "1892";
		arr[3] = "1234";
		arr = cavityMap(arr);
		for (int i = 0; i < arr.length; i++) {
			System.out.println(arr[i]);
		}
	}

	public static String[] cavityMap(String[] arr) {
		int n = arr.length;
		String[] newMap = new String[arr.length];
		for (int row = 0; row < n; row++) {
			newMap[row] = arr[row];
		}
		for (int row = 1; row < n - 1; row++) {
			for (int col = 1; col < n - 1; col++) {
				if (isCavity(row, col, arr)) {
					char[] newMapRow = newMap[row].toCharArray();
					newMapRow[col] = 'X';
					newMap[row] = String.valueOf(newMapRow);
				}
			}
		}
		return newMap;
	}

	private static boolean isCavity(int row, int col, String[] arr) {
		int val = arr[row].charAt(col);
		int neighbor1 = arr[row].charAt(col - 1);
		int neighbor2 = arr[row].charAt(col + 1);
		int neighbor3 = arr[row - 1].charAt(col);
		int neighbor4 = arr[row + 1].charAt(col);
		if (val > neighbor1 && val > neighbor2 && val > neighbor3 && val > neighbor4) {
			return true;
		}
		return false;
	}

}
