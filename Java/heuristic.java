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
			double min = Double.MAX_VALUE;
			for (double i : arr) {
				if (i <= 0) {
					continue;
				}
				if (i < min) {
					min = i;
				}
			}
			minpath.add(min);
		}
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
		for (int i = 0; i < graphmap.length; i++) {
			if (visited.contains(i)) {
				continue;
			}
			fix += minpath.get(i);
		}
		double[] heuristic = new double[len_Graph];
		for (int i = 0; i < len_Graph; i++) {
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

	public static double fun_heuristic_recursive(double[][] graphmap, int current, List<Integer> visited, int n) {
		if (n == 0 || (visited.size() == graphmap.length)) {
			return -minpath.get(current);
		}

		double min = Double.MAX_VALUE;
		for (int i = 0; i < graphmap.length; i++) {
			if (visited.contains(i)) {
				continue;
			}
			visited.add(i);
			double a = graphmap[current][i] + fun_heuristic_recursive(graphmap, i, visited, n - 1)
					- minpath.get(current);
			visited.remove((Object) i);
			if (a < min) {
				min = a;
				continue;
			}
		}
		return min;
	}
}
