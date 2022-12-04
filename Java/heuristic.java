package cs271project;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

public class heuristic {
	public static Map<Long, double[]> dict;
	public static boolean searched = false;
	public static int len_Graph = 0;
	public static List<Double> minpath = new ArrayList<Double>(heuristic.len_Graph);
	public static final int limit = 25165820;

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
		if (len_Graph < 24) {
			dict = new HashMap<Long, double[]>(33554432);
		} else {
			dict = new LinkedHashMap<Long, double[]>(33554432) {

				private static final long serialVersionUID = 1L;

				protected boolean removeEldestEntry(Map.Entry<Long, double[]> eldest) {
					return size() > limit;
				}
			};
		}
		return true;

	}

	private static long genKey(List<Integer> visited, int current) {
		long result = current;
		for (int i : visited) {
			result = ((1L << (63 - i)) | result);
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

		dict.put(key, heuristic);
		return heuristic;
	}

	// don't call this unless you know what you are doing
	private static double fun_heuristic_recursive(double max, double cost, double[][] graphmap, int current,
			List<Integer> visited, int n) {
		if (cost >= max) {
			return cost;
		}

		long key = genKey(visited, current);
		if (dict.containsKey(key)) {
			double min = Double.MAX_VALUE;
			int i = 0;
			double[] hx = dict.get(key);
			for (int a = 0; a < hx.length; a++) {
				double d = hx[a];
				if (d < min) {
					min = d;
					i = a;
				}
			}
			return min + cost + graphmap[current][i] - minpath.get(current);
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

}
