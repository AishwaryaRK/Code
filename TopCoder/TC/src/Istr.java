
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Istr {

	public static void main(String[] args) {
		System.out.println(count("wersrsresesrsesrawsdsw", 11));
	}

	public static int count(String s, int k) {
		Map<Character, Integer> charFrequencies = new HashMap<Character, Integer>();
		for (char ch : s.toCharArray()) {
			if (charFrequencies.containsKey(ch)) {
				charFrequencies.put(ch, charFrequencies.get(ch) + 1);
			} else {
				charFrequencies.put(ch, 1);
			}
		}
		List<Integer> cnts = new ArrayList<Integer>();
		for (int i : charFrequencies.values()) {
			cnts.add(i);
		}
		Collections.sort(cnts);
		
		System.out.println(cnts);
		int count = 0;
		for (int i = 1; i <= k; i++) {
			Collections.sort(cnts);
			int lastIndex = cnts.size() - 1;
			while (cnts.get(lastIndex)==0) {
				cnts.remove(lastIndex);
				lastIndex--;
			}
			cnts.set(lastIndex, cnts.get(lastIndex) - 1);
		}
		for (int i = 0; i < cnts.size(); i++) {
			count += cnts.get(i) * cnts.get(i);
		}
		return count;
	}

}
