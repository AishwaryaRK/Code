
public class FoxAndChess {

	public static void main(String[] args) {
		System.out.println(ableToMove("L", "."));
	}

	public static String ableToMove(String begin, String target) {
		if (begin == target) {
			return "Possible";
		}
		String begin1 = begin;
		String target1 = target;
		while (begin.length() > 0 && (begin.contains("R") || target.contains("R"))) {
			int beginRIndex = begin.lastIndexOf('R');
			int targetRIndex = target.lastIndexOf('R');
			if (targetRIndex < beginRIndex || (targetRIndex < 0 && beginRIndex >= 0)
					|| (beginRIndex < 0 && targetRIndex >= 0)) {
				return "Impossible";
			}
			if (begin.substring(beginRIndex, targetRIndex + 1).contains("L")) {
				return "Impossible";
			}
			begin = begin.substring(0, beginRIndex);
			target = target.substring(0, targetRIndex);
		}
		begin = begin1;
		target = target1;
		while (begin.length() > 0 && (begin.contains("L") || target.contains("L"))) {
			int beginLIndex = begin.indexOf('L');
			int targetLIndex = target.indexOf('L');
			if (targetLIndex > beginLIndex || (targetLIndex < 0 && beginLIndex >= 0)
					|| (beginLIndex < 0 && targetLIndex >= 0)) {
				return "Impossible";
			}
			if (begin.substring(targetLIndex, beginLIndex + 1).contains("R")) {
				return "Impossible";
			}
			begin = begin.substring(beginLIndex + 1, begin.length());
			target = target.substring(targetLIndex + 1, target.length());
		}
		return "Possible";
	}

}
