import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

public class heuristic {
	public static HashMap<Long, double[]> dict = new HashMap<Long, double[]>();
	public static HashMap<Long, double[]> dict2 = new HashMap<Long, double[]>();
	public static boolean searched = false;
	public static int len_Graph = 0;
	public static List<Double> minpath = new ArrayList<Double>(heuristic.len_Graph);
	public static final int limit = (int) (Integer.MAX_VALUE * 0.75);

	public static boolean init(double[][] map) {
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

		double size = (Math.pow(2, len_Graph) * len_Graph / 0.75) + 1;
		dict = new HashMap<Long, double[]>((int) size);
		return true;

	}

	private static long genKey(List<Integer> visited, int current) {
		long result = current;
		for (int i : visited) {
			result = ((1 << (63 - i)) | result);
		}
		return result;
	}

	// input different n(steps) may help with the speed and memory usage
	public static double[] fun_heuristic(double max, double[][] graphmap, int current, List<Integer> visited, int n) {
		long key = genKey(visited, current);

		if (dict.containsKey(key)) {
			return dict.get(key);
		}
		double fix = 0;
		double[] heuristic = new double[len_Graph];
		for (int i = 0; i < len_Graph; i++) {
			if (visited.contains(i)) {
				continue;
			}
			fix += minpath.get(i);
		}
		for (int i = 0; i < len_Graph; i++) {
			if (visited.contains(i)) {
				heuristic[i] = -1d;
				continue;
			}
			visited.add(i);
			double a = fun_heuristic_recursive(max, graphmap[current][i] + fix, graphmap, i, visited, n - 1);
			visited.remove((Object) i);
			heuristic[i] = a;
		}
		if (dict.size() > limit) {
			System.out.println("clean");
			dict.clear();
		}
		dict.put(key, heuristic);
		return heuristic;
	}

	// don't call this unless you know what you are doing
	private static double fun_heuristic_recursive(double max, double cost, double[][] graphmap, int current,
			List<Integer> visited, int n) {
		if (cost >= max) {
			return cost;
		}
		if (n == 0 || (visited.size() == len_Graph)) {
			return cost;
		}
		double min = Double.MAX_VALUE;
		for (int i = 0; i < len_Graph; i++) {
			if (visited.contains(i)) {
				continue;
			}
			visited.add(i);
			double a = fun_heuristic_recursive(max, cost + graphmap[current][i] - minpath.get(current), graphmap, i,
					visited, n - 1);
			visited.remove((Object) i);
			if (a < min) {
				min = a;
				continue;
			}
		}
		return min;
	}

	public static double[] fun_nodict_heuristic(double max, double[][] graphmap, int current, List<Integer> visited,
			int n) {
		double fix = 0;
		double[] heuristic = new double[len_Graph];
		for (int i = 0; i < len_Graph; i++) {
			if (visited.contains(i)) {
				continue;
			}
			fix += minpath.get(i);
		}
		for (int i = 0; i < len_Graph; i++) {
			if (visited.contains(i)) {
				heuristic[i] = -1d;
				continue;
			}
			visited.add(i);
			double a = fun_heuristic_recursive(max, graphmap[current][i] + fix, graphmap, i, visited, n - 1);
			visited.remove((Object) i);
			heuristic[i] = a;
		}
		return heuristic;
	}
}
