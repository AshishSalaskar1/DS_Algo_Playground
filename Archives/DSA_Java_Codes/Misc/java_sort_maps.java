package p1;
import java.util.*;


public class Main {
	
	static void sortCount(int[] arr) {
		int n = arr.length;
		
		HashMap<Integer,Integer> map = new HashMap<>();
		
		for(int i=0;i<n;i++) {
			int key = arr[i];
			
			if(map.containsKey(key))
				map.replace(key, map.get(key)+1);
			else
				map.put(key,1);
		}
		
		System.out.println(map.entrySet());
		
		List<Map.Entry<Integer, Integer> > list = new ArrayList<>(map.entrySet());
		
		Collections.sort(list,new Comparator< Map.Entry<Integer,Integer> >(){
			public int compare(Map.Entry<Integer, Integer> a,Map.Entry<Integer, Integer> b) {
				return b.getValue().compareTo(a.getValue());
			}
		});
		
		System.out.println(list);
	}
	
    public static void main(String args[]) { 
       
    	Scanner in = new Scanner(System.in);
    	int n = in.nextInt();
    	
    	int[] arr = new int[n];
    	
    	for(int i=0;i<n;i++)	arr[i] = in.nextInt();
    	
    	sortCount(arr);
    }

}
//
//TreeMap<Integer,Integer> map = new TreeMap<>();
//map.put(45, 3);
//map.put(1,56);
//map.put(4, 1);
//map.put(10,564);
//
//Set<Integer> keys = map.keySet();
//
////System.out.println(map.entrySet());
//
//List<Map.Entry<Integer, Integer> > list = 
//        new LinkedList<Map.Entry<Integer, Integer> >(map.entrySet()); 
//
// // Sort the list 
// Collections.sort(list, new Comparator<Map.Entry<Integer, Integer> >() { 
//     public int compare(Map.Entry<Integer, Integer> o1,  
//                        Map.Entry<Integer, Integer> o2) 
//     { 
//         return (o1.getValue()).compareTo(o2.getValue()); 
//     } 
// }); 
//
// for(int i=0;i<list.size();i++) {
//	 System.out.println(list.get(i).getKey());
// }
