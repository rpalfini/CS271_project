import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;

public class heuristic {
	public static HashMap<String, double[]> dict = new HashMap<String, double[]>();
	public static boolean searched = false;
	public static int len_Graph = 0;
	public static List<Double> minpath = new ArrayList<Double>();

	public static void findMin(double[][] map) {
		len_Graph = map.length;
		minpath.clear();
		for (double[] arr : map) {
			for (double i : arr) {
				if (i <= 0) {
					continue;
				}
				minpath.add(i);
			}
		}
		Collections.sort(minpath);
	}

	public static double fun_heuristic_recursive(double[][] graphmap, int current, List<Integer> visited, int n) {
		if (n == 0 || (visited.size() == graphmap.length)) {
			// return graphmap[current][start]
			return 0;
		}
		double min = 0;
		for (int i = 0; i < graphmap.length; i++) {
			if (visited.contains(i)) {
				continue;
			}
			visited.add(i);
			double a = graphmap[current][i] + fun_heuristic_recursive(graphmap, i, visited, n - 1);
			visited.remove((Object) i);
			if (a == 0) {
				continue;
			}
			if (min == 0 || a < min) {
				min = a;
				continue;
			}
		}
		return min;
	}

	// this heuristic will only check next n steps and return smallest path value of
	// next step for n steps
	// input different n may help with the speed and memory usage
	public static double[] fun_heuristic(double[][] graphmap, int current, List<Integer> visited, int n) {
		Collections.sort(visited);
		String key = "" + current;
		for (int i : visited) {
			key += i;
		}
		if (dict.containsKey(key)) {
			return dict.get(key);
		}
		double fix = 0;
		for (int i = 0; i < Math.max(0, (len_Graph - visited.size() - n)); i++) {
			fix += minpath.get(i);
		}
		double[] heuristic = new double[len_Graph];
		for (int i = 0; i < len_Graph; i++) {
			if (n == 0) {
				heuristic[i] = 0d;
				continue;
			}
			if (visited.contains(i)) {
				heuristic[i] = -1d;
				continue;
			}
			visited.add(i);
			double a = graphmap[current][i] + fun_heuristic_recursive(graphmap, i, visited, n - 1) + fix;
			visited.remove((Object) i);
			heuristic[i] = a;
		}
		dict.put(key, heuristic);
		return heuristic;
	}

}
