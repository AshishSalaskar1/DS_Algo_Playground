package p1;

import java.util.*;
import java.lang.*;
import java.io.*;

class Main
 {
	

	
	static HashMap<Character,Integer> getMap(String str){
		HashMap<Character,Integer> map = new HashMap<>();
		
		for(char c : str.toCharArray()) {
			if(map.containsKey(c))
				map.replace(c, map.get(c)+1);
			else
				map.put(c,1);
		}
		
		return map;
	}
	

	public static void main (String[] args) throws Exception
	 {
		String[] arr = {"eat", "tea", "tan", "ate", "nat", "bat"};
		
		HashMap<HashMap<Character,Integer>,List<String>> map = new HashMap<>();
		
		List<List<String>> res= new ArrayList<>();
		
		for(String str : arr) {
			HashMap<Character,Integer> tMap = getMap(str);
			System.out.println(str);
			if(!map.containsKey(tMap)) {
				List<String> l = new ArrayList<>();
				l.add(str);
				map.put(tMap,l);
			}
			else
				map.get(tMap).add(str);
		}
		
		
		for(List<String> l : map.values()) {
			res.add(l);
		}
		
		System.out.println(res);
		
		
	  
 	 }
}
