import java.io.File;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class DFS_H {

	public static double upper_bound = Double.MAX_VALUE;
	public static long time_dfs = 0;
	public static long time_hx = 0;
	public static int total_t = 0;
	public static List<Integer> p = new ArrayList<Integer>();
	public static List<Integer> temp_p = new ArrayList<Integer>();

	public static void DFS(int startnode, double[][] adj_matrix, int node, List<Integer> need_visit, double path,
			List<Integer> visited) {
		// time
		long t_msec = System.nanoTime();

		total_t += 1;
		//

		// break condition
		if (path > upper_bound) {
			return;
		}

		temp_p.add(node);

		// update this time complexicty. make deep copy of list,increase space
		// complexcity, may need to add node back in future/not linear space?

		// temp_visited = copy.deepcopy(visited)
		visited.add(node);
		// int N = adj_matrix.length;
		// visit all the node,return the path
		if (visited.size() == heuristic.len_Graph) {
			double new_distance = path + adj_matrix[node][startnode];
			if (new_distance <= upper_bound) {
				upper_bound = new_distance;
				p.clear();
				for (int i : temp_p) {
					p.add(i);
				}
			}
			temp_p.remove((Object) node);
			visited.remove((Object) node);
			return;
		}
		//

		long te_msec = System.nanoTime();
		time_dfs += te_msec - t_msec;
		t_msec = System.nanoTime();
		double[] hx = heuristic.fun_heuristic(adj_matrix, node, visited, 3);
		te_msec = System.nanoTime();
		time_hx += te_msec - t_msec;
		t_msec = System.nanoTime();
		List<Double> hxc = new ArrayList<Double>();
		int count = 0;
		for (double d : hx) {
			if (d <= 0) {
				continue;
			}
			hxc.add(d);
			count++;
		}
		Collections.sort(hxc);

		if (path + hxc.get(0) > upper_bound) {
			temp_p.remove((Object) node);
			visited.remove((Object) node);
			return;
		}
		count = 0;
		List<Integer> sorted_need = new ArrayList<Integer>();
		int l = hxc.size();

		while (count < l) {
			for (int i = 0; i < heuristic.len_Graph; i++) {
				if (hx[i] == hxc.get(count)) {
					// System.out.println(hxc.get(count));
					sorted_need.add(i);
					count += 1;
					break;
				}
			}
		}

		te_msec = System.nanoTime();
		time_dfs += te_msec - t_msec;

		for (int a = 0; a < sorted_need.size(); a++) {
			int i = sorted_need.get(a);
			// System.out.print(i + " ");
			DFS(startnode, adj_matrix, i, sorted_need, path + adj_matrix[node][i], visited);
		}
		// System.out.println();
		temp_p.remove((Object) node);
		visited.remove((Object) node);
		return;
	}

	public static void main(String[] args) {
		File file_input = new File("11_5.0_1.0.out");
		double[][] graph = input_trans.getInput(file_input);
		int N = graph.length;
		int Start_node = 0;
		List<Integer> need_visit = new ArrayList<Integer>();
		for (int i = 0; i < N; i++) {
			need_visit.add(i);
		}

		// 3/2 MST
		// upper_bound = 100000 * N;
		List<Integer> v_visited = new ArrayList<Integer>();

		heuristic.findMin(graph);
		// long time_msec = System.nanoTime()
		DFS(Start_node, graph, Start_node, need_visit, 0, v_visited);
		// long time_msec_end = System.nanoTime()

		p.add(Start_node);

		double distance_verify = 0;
		// verfiy
		for (int i = 0; i < p.size() - 1; i++) {
			distance_verify += graph[p.get(i)][p.get(i + 1)];
		}
		System.out.println("path: " + p);
		System.out.println("path_verify:" + distance_verify);
		//

		System.out.println("shortest path cost: " + upper_bound);
		System.out.println("cost to loop: " + total_t);
		int t = 1;
		for (int i = 1; i < N; i++) {
			t *= i;
		}
		System.out.println("cost to loop all: " + t);
		System.out.println("dfs ns time: " + time_dfs);
		System.out.println("hx ns time: " + time_hx);

		// g.render('1.png', format='png')
	}
}
