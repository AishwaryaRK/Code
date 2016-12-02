import java.util.Collections;
import java.util.HashMap;
import java.util.Map;

public class TreeAndVertex {

	public static void main(String[] args) {
		int[] tree = {0, 1, 2, 0, 1, 5, 6, 1, 7, 4, 2, 5, 5, 8, 6, 2, 14, 12, 18, 10, 0, 6, 18, 2, 20, 11, 0, 11, 7, 12, 17, 3, 18, 31, 14, 34, 30, 11, 9};
		System.out.println(get(tree));
	}

	public static int get(int[] tree) {
		Map<Integer, Integer> counts = new HashMap<Integer, Integer>();
		for (int i = 0; i < tree.length; i++) {
			int vertex1 = i + 1;
			int vertex2 = tree[i];
			if (counts.containsKey(vertex1)) {
				counts.put(vertex1, counts.get(vertex1) + 1);
			} else {
				counts.put(vertex1, 1);
			}
			if (counts.containsKey(vertex2)) {
				counts.put(vertex2, counts.get(vertex2) + 1);
			} else {
				counts.put(vertex2, 1);
			}
		}
		return Collections.max(counts.values());
	}

}
