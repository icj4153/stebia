
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;

public class Main {
	public static void main(String[] args) throws IOException {
		int n, m;
		int cnt = 0;
		String [] arr;
		HashMap<String, Boolean> hi = new HashMap<>();
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String input = br.readLine();
		arr = input.split(" ");
		n = Integer.parseInt(arr[0]);
		m = Integer.parseInt(arr[1]);

		for (int i = 0; i < n; i++) {
			hi.put(br.readLine(), Boolean.FALSE);
		}
		for (int i = 0; i < m; i++) {
			if (hi.containsKey(br.readLine())){
				cnt++;
			}
		}
		br.close();
		System.out.println(cnt);
	}
}