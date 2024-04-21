//LINk : https://leetcode.com/problems/keys-and-rooms

//DFS BASED
class Solution {
   
    
    public boolean canVisitAllRooms(List<List<Integer>> rooms) {
        Stack<Integer> stack = new Stack<>();
        HashSet<Integer> vis = new HashSet<>();
        
        int N = rooms.size();
        stack.add(0);
        vis.add(0);
        
        while(!stack.isEmpty()){
            int node = stack.pop();
            
            for(int x : rooms.get(node)){
                if(!vis.contains(x)){
                    vis.add(x);
                    stack.push(x);
                }
                
                if(vis.size() == N) return true;
            }
        }
        
        return vis.size() == rooms.size();
        
    }


}

// HashSet based
class Solution {
   
    private void addKey(int room, List<List<Integer>> rooms,Set<Integer> visited) {
        visited.add(room);
        for (int key: rooms.get(room))
            if (!visited.contains(key)) addKey(key, rooms,visited);
        // return;
    }
    
    public boolean canVisitAllRooms(List<List<Integer>> rooms) {
        Set<Integer> visited=new HashSet<>();
        addKey(0, rooms,visited);
        return visited.size() == rooms.size();
    }


}

//DFS based
