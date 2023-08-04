import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;

public class Main {
	public static void main(String[] args) throws IOException {
		int n;
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		PriorityQueue<Integer> hi = new PriorityQueue<>(((o1, o2) -> o2 - o1));
		String s = br.readLine();

		n = Integer.parseInt(s);
		for(int i= 0; i<n;i++){
			String[] str = br.readLine().split(" ");
			for(int j= 0;j<n;j++){
				hi.add(Integer.parseInt(str[j]));
			}
		}

		for(int i=1; i<n;i++){
			hi.remove();
		}
		System.out.println(hi.peek());
	}
}