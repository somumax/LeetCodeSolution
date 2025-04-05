import java.util.*;

class Solution {
    private long totalFuel = 0;
    
    public long minimumFuelCost(int[][] roads, int seats) {
        int n = roads.length + 1;
        List<List<Integer>> adj = new ArrayList<>();
        
        for (int i = 0; i < n; i++) {
            adj.add(new ArrayList<>());
        }
        
        for (int[] road : roads) {
            int u = road[0], v = road[1];
            adj.get(u).add(v);
            adj.get(v).add(u);
        }
        
        dfs(0, -1, adj, seats);
        return totalFuel;
    }
    
    private int dfs(int node, int parent, List<List<Integer>> adj, int seats) {
        int people = 1;
        
        for (int child : adj.get(node)) {
            if (child != parent) {
                people += dfs(child, node, adj, seats);
            }
        }
        
        if (node != 0) {
            // totalFuel += (people + seats - 1) / seats;
            totalFuel += (long) Math.ceil((double) people / seats);
        }
        
        return people;
    }
}