
public class FoxAndGomoku {

	public static void main(String[] args) {
		String[] board = { "....o.", "...o..", "..o...", ".o....", "o.....", "......" };
		System.out.println(win(board));
	}

	public static String win(String[] board) {
		for (int i = 0; i < board.length; i++) {
			for (int j = 0; j < board.length; j++) {
				if (board[i].charAt(j) == 'o'
						&& (isHorizontal(i, j, board) || isVertical(i, j, board) || isDiagonal(i, j, board))) {
					return "found";
				}
			}
		}
		return "not found";
	}

	private static boolean isDiagonal(int i, int j, String[] board) {
		System.out.println(i+", "+j);
		boolean isDiagonal = true;
		if (i + 5 <= board.length && j + 5 <= board.length) {
			for (int k = i; k < i + 5; k++, j++) {
				if (board[k].charAt(j) != 'o') {
					isDiagonal = false;
					break;
				}
			}
			if (isDiagonal) {
				return true;
			}
		}
		if (i + 5 <= board.length && j - 5 >= -1) {
			System.out.println("in");
			for (int k = i; k < i + 5; k++, j--) {
				if (board[k].charAt(j) != 'o') {
					return false;
				}
			}
			return true;
		}
		return false;
	}

	private static boolean isVertical(int i, int j, String[] board) {
		if (i + 5 <= board.length) {
			for (int k = i; k < i + 5; k++) {
				if (board[k].charAt(j) != 'o') {
					return false;
				}
			}
			return true;
		}
		return false;
	}

	private static boolean isHorizontal(int i, int j, String[] board) {
		if (j + 5 <= board.length) {
			for (int k = j; k < j + 5; k++) {
				if (board[i].charAt(k) != 'o') {
					return false;
				}
			}
			return true;
		}
		return false;
	}

}
