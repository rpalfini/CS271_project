package cs271project;

import java.io.File;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Scanner;

public class Main {
	private static void listFilesForFolder(final File folder) {
		for (final File fileEntry : folder.listFiles()) {
			if (fileEntry.isDirectory()) {
				listFilesForFolder(fileEntry);
			} else {
				if (fileEntry.getName().contains("txt") || fileEntry.getName().contains("out")) {
					double[][] graph = input_trans.getInput(fileEntry);
					System.out.println("Running DFS for: " + fileEntry.getName());
					dfs(graph);
					System.out.println("Running SLS for: " + fileEntry.getName());
					sls(graph);
					System.out.println("Ended");
					System.out.println();
				}
			}
		}
	}

	public static void Auto() {
		listFilesForFolder(new File("."));
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.println("Please input the filename of the graph, or input \"auto\" to run all txt and out files:");
		String filename = sc.nextLine();
		if (filename.equals("auto")) {
			Auto();
			sc.close();
			return;
		}
		File file_input = new File(filename);
		if (!file_input.exists()) {
			System.out.println("File not found, exited");
			sc.close();
			return;
		}
		double[][] graph = new double[0][0];
		try {
			graph = input_trans.getInput(file_input);
		} catch (Exception e) {
			System.out.println("File incorrect, exited");
			sc.close();
			return;
		}

		System.out.println("Input 1 to do DFS and 2 for SLS: ");
		int i = Integer.parseInt(sc.nextLine());
		if (i == 1) {
			dfs(graph);
		} else {
			sls(graph);
		}
		sc.close();
	}

	public static void sls(double[][] graph) {
		int N = graph.length;
		List<Integer> best_overall = LocalSearch.random_permutation(N);
		double best_overall_cost = LocalSearch.calc_cost(best_overall, graph);
		List<String> list_searched = new LinkedList<String>();
		int count = 500;
		while (count > 0) {
			List<Integer> path_random = LocalSearch.random_permutation(N);
			boolean not_converged = true;
			if (list_searched.contains(path_random.toString())) {
				continue;
			}
			list_searched.add(path_random.toString());
			if (list_searched.size() > LocalSearch.max_size) {
				list_searched.remove(0);
			}
			while (not_converged) {
				List<Integer> best_solution = LocalSearch.SLS(path_random, graph);
				if (best_solution.toString().equals(path_random.toString())) {
					not_converged = false;
				}
				path_random = best_solution;
				double newcost = LocalSearch.calc_cost(best_solution, graph);
				if (newcost < best_overall_cost) {
					best_overall = best_solution;
					best_overall.add(best_overall.get(0));
					best_overall_cost = newcost;

				}
				count -= 1;
			}
		}
		System.out.println(best_overall);
		System.out.println(best_overall_cost);
	}

	public static void dfs(double[][] graph) {
		heuristic.init(graph);

		if (heuristic.len_Graph < 50) {
			DFS_H.hx_steps = 4;
		} else if (heuristic.len_Graph <= 100) {
			DFS_H.hx_steps = 3;
		} else {
			DFS_H.hx_steps = 2;
		}

		DFS_H.time = System.currentTimeMillis() + 600000;
		DFS_H.upper_bound = Double.MAX_VALUE;
		// DFS_H.total_t = 0;
		int size = (int) (heuristic.len_Graph / 0.75 + 1);
		DFS_H.p = new ArrayList<Integer>(size);
		DFS_H.temp_p = new ArrayList<Integer>(size);

		int Start_node = 0;
		List<Integer> v_visited = new ArrayList<Integer>(size);

		long time_msec = System.currentTimeMillis();

		DFS_H.DFS(Start_node, graph, Start_node, 0, v_visited);

		long time_msec_end = System.currentTimeMillis();

		DFS_H.p.add(Start_node);

		System.out.println("path: " + DFS_H.p);
		/* verfiy */
		/*
		 * double distance_verify = 0; for (int i = 0; i < p.size() - 1; i++) {
		 * distance_verify += graph[p.get(i)][p.get(i + 1)]; }
		 * System.out.println("path_verify:" + distance_verify);
		 */
		System.out.println("shortest path cost: " + DFS_H.upper_bound);
		// System.out.println("cost of search: " + DFS_H.total_t);

		// long t = 1;
		// for (int i = 1; i < heuristic.len_Graph; i++) {
		// t *= i;
		// }

		// System.out.println("cost of search without heuristic/prune: " + t);
		// System.out.println("dfs ns time: " + time_dfs);
		// System.out.println("hx ns time: " + time_hx);
		System.out.println("total ms time: " + (time_msec_end - time_msec));
	}
}
