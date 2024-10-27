	static int str_to_int(String str,int ans) {
		if(str.length() == 1) {
			return (10*ans)+(str.charAt(0)-48);
		}
		
		int newAns = (10*ans)+(str.charAt(0)-48);
		
		return str_to_int(str.substring(1), newAns);
	}
	
	public static void main(String[] args) {
	
		String s = "9234";
		System.out.println(str_to_int("123123",0));
		
		
	}
