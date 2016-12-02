
public class EqualSubstrings2 {

	public static void main(String[] args) {
		System.out.println(get("aaaab"));
	}

	public static int get(String s) {
		int count = 0;
		for (int i = 1; i <= s.length() / 2; i++) {
			System.out.println("i=" + i);
			for (int j = 0; j < s.length() && j + i < s.length(); j++) {
				String testStr = s.substring(j, j + i);
				int startIndex = j + i;
				while (startIndex + i <= s.length()) {
					String data = s.substring(startIndex);
					int index = data.indexOf(testStr);
					System.out.println("testStr=" + testStr);
					System.out.println("data=" + data);
					System.out.println("index=" + index);
					if (index >= 0) {
						count++;
						startIndex += index + i;
					} else {
						break;
					}
				}
			}
		}
		return count;
	}

}
