import java.io.File;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class DFS_H {

	public static double upper_bound = Double.MAX_VALUE;
	// public static long time_dfs = 0;
	// public static long time_hx = 0;
	// public static int total_t = 0;
	public static List<Integer> p = new ArrayList<Integer>();
	public static List<Integer> temp_p = new ArrayList<Integer>();

	public static void DFS(int startnode, double[][] adj_matrix, int node, double path, List<Integer> visited) {
		/* timing */
		// long t_msec = System.nanoTime();
		// total_t += 1;

		temp_p.add(node);

		visited.add(node);
		/* visit all the node,return the path */
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

		// long te_msec = System.nanoTime();
		// time_dfs += te_msec - t_msec;
		// t_msec = System.nanoTime();

		double[] hx = heuristic.fun_heuristic(upper_bound - path, adj_matrix, node, visited, 4);

		// te_msec = System.nanoTime();
		// time_hx += te_msec - t_msec;
		// t_msec = System.nanoTime();

		List<Double> hxc = new ArrayList<Double>();
		int count = 0;
		for (double d : hx) {
			/* break condition */
			if (d <= 0 || path + d > upper_bound) {
				continue;
			}
			hxc.add(d);
			count++;
		}
		Collections.sort(hxc);

		count = 0;
		List<Integer> sorted_need = new ArrayList<Integer>();
		int l = hxc.size();

		while (count < l) {
			for (int i = 0; i < heuristic.len_Graph; i++) {
				if (hx[i] == hxc.get(count)) {
					sorted_need.add(i);
					count += 1;
					break;
				}
			}
		}

		// te_msec = System.nanoTime();
		// time_dfs += te_msec - t_msec;

		for (int i : sorted_need) {

			DFS(startnode, adj_matrix, i, path + adj_matrix[node][i], visited);
		}

		temp_p.remove((Object) node);
		visited.remove((Object) node);
		return;
	}

	public static void main(String[] args) {
		File file_input = new File("20_5.0_1.0.out");
		double[][] graph = input_trans.getInput(file_input);
		heuristic.findMin(graph);
		int Start_node = 0;

		List<Integer> v_visited = new ArrayList<Integer>();

		long time_msec = System.nanoTime();

		DFS(Start_node, graph, Start_node, 0, v_visited);

		long time_msec_end = System.nanoTime();

		p.add(Start_node);

		System.out.println("path: " + p);

		/* verfiy */
		double distance_verify = 0;
		for (int i = 0; i < p.size() - 1; i++) {
			distance_verify += graph[p.get(i)][p.get(i + 1)];
		}

		System.out.println("path_verify:" + distance_verify);
		System.out.println("shortest path cost: " + upper_bound);
		// System.out.println("cost to loop: " + total_t);

		// int t = 1;
		// for (int i = 1; i < heuristic.len_Graph; i++) {
		// t *= i;
		// }

		// System.out.println("cost to loop all: " + t);
		// System.out.println("dfs ns time: " + time_dfs);
		// System.out.println("hx ns time: " + time_hx);
		System.out.println("total ns time: " + (time_msec_end - time_msec));
	}
}