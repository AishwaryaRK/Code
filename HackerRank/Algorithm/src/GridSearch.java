
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class GridSearch {

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
		int t = Integer.parseInt(bufferedReader.readLine());
		for (int i = 1; i <= t; i++) {
			String[] s = bufferedReader.readLine().split(" ");
			int R = Integer.parseInt(s[0]);
			int C = Integer.parseInt(s[1]);
			int[][] grid = new int[R][C];
			for (int j = 0; j < R; j++) {
				s = bufferedReader.readLine().split("");
				for (int k = 0; k < C; k++) {
					grid[j][k] = Integer.parseInt(s[k]);
				}
			}
			s = bufferedReader.readLine().split(" ");
			int r = Integer.parseInt(s[0]);
			int c = Integer.parseInt(s[1]);
			int[][] pattern = new int[r][c];
			for (int j = 0; j < r; j++) {
				s = bufferedReader.readLine().split("");
				for (int k = 0; k < c; k++) {
					pattern[j][k] = Integer.parseInt(s[k]);
				}
			}
			// print(grid);
			// print(pattern);
			System.out.println(isPatternPresent(grid, pattern));
		}
	}

	private static String isPatternPresent(int[][] grid, int[][] pattern) {
		int R = grid.length;
		int C = grid[0].length;
		int r = pattern.length;
		int c = pattern[0].length;
		int start = pattern[0][0];
		for (int i = 0; i < grid.length; i++) {
			for (int j = 0; j < grid.length; j++) {
				if (grid[i][j] == start) {
					if (checkValidity(i, j, grid, pattern)) {
						return "YES";
					}
				}
			}
		}
		return "NO";
	}

	private static boolean checkValidity(int startR, int startC, int[][] grid, int[][] pattern) {
		for (int i = startR, x = 0; x < pattern.length && i < grid.length; i++, x++) {
			for (int j = startC, y = 0; y < pattern[0].length && j < grid[0].length; j++, y++) {
				if (grid[i][j] != pattern[x][y]) {
					return false;
				}
			}
		}
		return true;
	}

	private static void print(int[][] grid) {
		for (int i = 0; i < grid.length; i++) {
			for (int j = 0; j < grid[i].length; j++) {
				System.out.print(grid[i][j] + " ");
			}
			System.out.println();
		}
	}

}
