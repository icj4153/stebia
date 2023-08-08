import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	static int[][] board;
	static int blue_cnt = 0;
	static int white_cnt = 0;

	public static void main(String[] args) throws IOException {
		int n;

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		n = Integer.parseInt(br.readLine());
		board = new int[n][n];

		for(int i=0; i<n;i++) {
			StringTokenizer st = new StringTokenizer(br.readLine()," ");
			for(int j = 0; j<n; j++){
				board[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		splitboard(0,0,n);
		System.out.println(white_cnt);
		System.out.println(blue_cnt);
	}

	public static void splitboard(int row, int col, int size) {
		if (sameColor(row, col, size)){
			if (board[row][col] == 1){
				blue_cnt++;
			}else {
				white_cnt++;
			}
		} else{
			// 4등분으로 쪼갬
			splitboard(row,col,size/2);
			splitboard(row, col + (size / 2), size / 2);
			splitboard(row + (size / 2), col, size / 2);
			splitboard(row+(size/2), col+(size/2), size/2);
		}
	}

	public static boolean sameColor(int row,int col, int size){
		int tmp = board[row][col];

		for (int i = row; i < row+size;i++){
			for(int j = col; j < col+size; j++){
				if(tmp != board[i][j]){
					return false;
				}
			}
		}
		return true;
	}
}