
public class Main {
	
	static boolean isSorted(int arr[],int index) {
		
		if(arr.length-1 == index) 
			return true;
		
		
		if(arr[index] > arr[index+1])
			return false;
		
		else
			return isSorted(arr,index+1);
		
	}

	public static void main(String[] args) {
		System.out.println(isSorted(new int[]{12,2,3},0));
	}

}

