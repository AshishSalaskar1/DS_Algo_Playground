class Node {
  Node left;
  Node right;
  int data;
}

class BinaryTree {

  Node headLinkedList;
  Node prev;

  public void bstToDoublyLinkedList(Node node) {
    if (node == null) {
      return;
    }

    bstToDoublyLinkedList(node.left);

    if (prev == null) {
      headLinkedList = node;
      prev = node;
    } else {
      node.left = prev;
      prev.right = node;
      prev = node;
    }

    bstToDoublyLinkedList(node.right);
  }
  
  public Node createNewNode(int val) {
    Node newNode = new Node();
    newNode.data = val;
    newNode.left = null;
    newNode.right = null;
    return newNode;
  }
}

public class BinaryTreeApp {

  public static void main(String[] args) {

    BinaryTree a = new BinaryTree();

    Node root = a.createNewNode(12);
    root.left = a.createNewNode(7);
    root.left.left = a.createNewNode(6);
    root.left.right = a.createNewNode(9);
    root.right = a.createNewNode(24);

    a.bstToDoublyLinkedList(root);

  }
}
