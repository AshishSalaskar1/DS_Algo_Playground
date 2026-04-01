class Node:
    def __init__(self, val="", next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

# class DLL:
#     def __init__(self):
#         self.head = Node()
#         self.tail = Node()
#         self.cursor = self.head
#         self.head.next = self.tail
#         self.tail.prev = self.head


class TextEditor:

    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.cursor = self.head
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def addText(self, text: str) -> None:
        # CURSOR <---> CURSOR_NEXT
        # CURSOR <---> NODE <---> CURSOR_NEXT
        for ch in text:
            node = Node(ch)
            node.prev = self.cursor
            node.next = self.cursor.next

            self.cursor.next.prev = node
            self.cursor.next = node
            self.cursor = node

        
    def deleteText(self, k: int) -> int:
        count = 0
        while k>0 and self.cursor != self.head:
            prev = self.cursor.prev
            prev.next = self.cursor.next
            self.cursor.next.prev = prev
            self.cursor = prev
            k -= 1
            count += 1
        
        return count
        

    def cursorLeft(self, k: int) -> str:
        while k>0 and self.cursor != self.head:
            self.cursor = self.cursor.prev
            k -= 1
        return self.get_last_10_chars()
        

    def cursorRight(self, k: int) -> str:
        while k>0 and self.cursor.next != self.tail:
            self.cursor = self.cursor.next
            k -= 1
        return self.get_last_10_chars() 


    def get_last_10_chars(self) -> str:
        text = ""
        curr = self.cursor
        count = 0
        while curr != self.head and count < 10:
            text += curr.val
            curr = curr.prev
            count += 1
        return text[::-1]
        


# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)