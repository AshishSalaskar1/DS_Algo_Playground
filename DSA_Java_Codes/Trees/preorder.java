
class BST{
    class Node{
        int data;
        Node left;
        Node right;

        Node(int data){
            this.data = data;
            left = null;
            right = null;
        }
    }

        Node root = null;

        public void createBST(int[] arr){
            this.root = createBST(arr,0,arr.length-1);
        }

        private Node createBST(int[] arr,int low,int high){
            if(low>high)
                return null;

            int mid = (low+high)/2;

            Node node = new Node(arr[mid]);

            node.left = createBST(arr,low,mid-1);
            node.right = createBST(arr,mid+1,high);

            return node;
        }

        public  void preOrder(){
            preOrder(this.root);
        }

        private void preOrder(Node node){
            if(node == null)
                return;

            System.out.print(node.data);
            preOrder(node.left);
            preOrder(node.right);
        }

        void print() {
            print(this.root);
        }
        
        void print(Node node) {
            String str = "";
            
            if(node.left != null) {
                str = node.left.data+"=>"+str;
            }
            else {
                str = "END =>"+str;
            }
            
            str = str+node.data;
            
            if(node.right != null) {
                str = str+"<="+node.right.data;
            }
            else {
                str = str+" <=END";
            }
            
            System.out.println(str);
            
            //print left and right nodes
            if(node.left != null) {
                print(node.left);
            }
            if(node.right != null) {
                print(node.right);
            }
    }
}

public class Main {
    public static void main(String args[]) {

        int[] arr = {1 ,2 ,3 ,4 ,5 ,6 ,7};
        BST b = new BST();
        b.createBST(arr);
        // b.print();
        b.preOrder();
            // System.out.println("Hello World!"+b.root.data);
    }
}
