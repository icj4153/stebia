
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.LinkedList;
import java.util.List;
import java.util.PriorityQueue;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	public static int[][] graph;

	public static int n;
	public static int m;
	public static int v;
	public static boolean[] visited_dfs;
	public static boolean[] visited_bfs;

	public static Queue<Integer> queue;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		v = Integer.parseInt(st.nextToken());

		visited_dfs = new boolean[n+1];
		visited_bfs = new boolean[n+1];
		graph = new int[n+1][n+1];

		for(int i = 0;i<m;i++){
			String [] tmp = br.readLine().split(" ");
			int start = Integer.parseInt(tmp[0]);
			int end = Integer.parseInt(tmp[1]);

			graph[start][end] = 1;
			graph[end][start] = 1;
		}

		DFS(v);
		System.out.println();
		BFS(v);
	}

	public static void DFS(int source) {
		// int start = source;
		visited_dfs[source] = true;
		System.out.print(source + " ");

		for(int i = 1 ; i< n+1;i++){
			if(graph[source][i] == 1 && !visited_dfs[i]){
				DFS(i);
			}
		}
	}

	public static void BFS(int source){
		queue = new LinkedList<>();
		queue.add(source);

		while(!queue.isEmpty()){
			int num = queue.poll();
			System.out.print(num+" ");
			visited_bfs[num] = true;
			for(int i = 1; i<n+1;i++){
				if(graph[num][i] == 1 && !visited_bfs[i]){
					visited_bfs[i] =true;
					queue.add(i);
				}
			}
		}
	}
}
