package SRM691;

import java.util.Arrays;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Plusonegame {

	public static void main(String[] args) {
		System.out.println(getorder("+0++"));
	}

	public static String getorder(String s) {
		Pattern pattern = Pattern.compile("[0-9]+");
		Matcher matcher = pattern.matcher(s);
		if (!matcher.find()) {
			return s;
		}
		char[] sCharArray = s.toCharArray();
		Arrays.sort(sCharArray);
		s = "";
		for (int i = 0; i < sCharArray.length; i++) {
			s += sCharArray[i];
		}
		if (!s.contains("+")) {
			return s;
		}
		int counter = 0;
		int index = s.lastIndexOf('+');
		int plusCount = s.substring(0, index + 1).length();
		s = s.substring(index + 1, s.length());
		String ans = "";
		for (int i = 0; i < s.length(); i++) {
			int val = Integer.parseInt(s.charAt(i) + "");
			while (counter != val && counter < plusCount) {
				counter++;
				ans += '+';
			}
			if (counter == val) {
				ans += val;
			} else {
				ans += s.substring(i, s.length());
				break;
			}
		}
		if (counter < plusCount) {
			while (counter < plusCount) {
				ans += '+';
				counter++;
			}
		}
		return ans;
	}
}
