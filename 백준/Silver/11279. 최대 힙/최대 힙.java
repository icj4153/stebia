import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;

public class Main {
	public static void main(String[] args) throws IOException {
		int n;
		PriorityQueue<Integer> hi = new PriorityQueue<>((o1, o2) -> o2 - o1);
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String s = br.readLine();
		n = Integer.parseInt(s);

		for(int i = 0; i<n; i++){
			int num;
			num = Integer.parseInt(br.readLine());

			if( num == 0){
				if (hi.isEmpty()) {
					System.out.println(0);
				}else{
					System.out.println(hi.poll());
				}
			}else{
				hi.add(num);
			}
		}
	}
}