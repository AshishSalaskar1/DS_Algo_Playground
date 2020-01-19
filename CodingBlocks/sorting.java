

class SelectionSort{
	static void sort(int[] a) {
		for (int i = 0; i < a.length; i++) {
			int min = i;
			
			for (int j = min; j < a.length; j++) {
				if(a[min] > a[j])
					min = j;
					
			}
			
			if(min != i) {
				int temp = a[min];
				a[min] = a[i];
				a[i] = temp;
			}
		}
		
	
	}
}

class InsertionSort{
	static void sort(int[] arr) {
		for (int i = 1; i < arr.length; i++) {
			int val = arr[i];
			int j = i-1;
			
			while(j>=0 && arr[j]>val) {
				arr[j+1] = arr[j];
				j--;
			}
			
			//+1 bcoz while exiting while it bcomes j-- once
			arr[j+1] = val;
		}
	}
}

class QuickSort{
	
	private static int partition(int[] arr,int low,int high) {
		int partitionIndex = low;
		
		//selecting last element as pivot element
		int pivot = arr[high];
		for (int i = low; i <= high; i++) {
			if(arr[i] < pivot) {
				
				//swap i with pIndex
				int temp = arr[i];
				arr[i] = arr[partitionIndex];
				arr[partitionIndex] = temp;
			
				partitionIndex++;
			}
		}
		
		//finally swap pIndex with assumed pivot i.e Last ele
		int temp = arr[high];
		arr[high] = arr[partitionIndex];
		arr[partitionIndex] = temp;
		
		return partitionIndex;
		
		
	}
	
	
	static void sort(int[] arr,int low,int high) {
		if(low<high) {
			int pi = partition(arr, low, high);
			sort(arr, low, pi-1);
			sort(arr, pi+1,high);
		}
	}
}

class MergeSort{
	
	private static void merge(int[] arr,int low,int mid,int high) {
		int n1=mid-low+1;
		int n2= high-mid;
		int[] left = new int[n1];
		int[] right = new int[n2];
		
		for(int i=0;i<n1;i++)
			left[i] = arr[low+i];
		
		for(int i=0;i<n2;i++)
			right[i] = arr[mid+1+i];
		
		int i=0,j=0;
		int k = low;
		
		while(i<n1 && j<n2) {
			if(left[i] < right[j]) 
				arr[k++] = left[i++];
			
			else 
				arr[k++] = right[j++]; 
			
		}
		
		while(i<n1) 
			arr[k++] = left[i++];
		
		while(j<n2) 
			arr[k++] = right[j++];
		
	}
	
	static void sort(int[] arr,int low,int high) {
		
		if(low<high) {
			int mid = (low+high)/2;
			sort(arr, low, mid);
			sort(arr, mid+1, high);
			merge(arr,low,mid,high);
		}
		
	}
}

public class Main {
	
	static void printArr(int[] arr) {
		for(int x:arr)
			System.out.print(x+" ");
		
		System.out.println();
	}
	

	public static void main(String[] args) {
		int[] arr = {1,4,3,21,7,234,45,2,34,6,231};
		
//		printArr(arr);
//		MergeSort.mergeSort(arr, 0, arr.length-1);
//		printArr(arr);
//		
		printArr(arr);
		SelectionSort.sort(arr);
		printArr(arr);



	}

}

