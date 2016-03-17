class LinkedNode:
	
	def __init__(self, key = None, value = None, next = None):
		self.key = key
		self.value = value
		self.next = next

class LRUCache:
	
	def __init__(self, capacity):
		self.hash = {}
		self.head = LinkedNode()
		self.tail = self.head
		self.capacity = capacity

	def push_back(self, node):
		self.hash[node.key] = self.tail
		self.tail.next = node
		self.tail = node

	def pop_front(self):
		del self.hash[self.head.next.key]
		self.head.next = self.head.next.next
		self.hash[self.head.next.key] = self.head

	def kick(self, prev):
		node = prev.next
		if node == self.tail
			return
		prev.next = node.next
		if node.next is not None:
			self.hash[node.next.key] = prev
			node.next = None
		self.push_back(node)

	def get(self, key):
		if key not in self.hash:
			return -1
		self.kick(self.hash[key])
		return self.hash[key].next.value
	
	def set(self, key, value):
		if key in self.hash:
			self.kick(self.hash[key])
			self.hash[key].next.value = value
		else:
			self.push_back(LinkedNode(key, value))
			if len(self.hash) > self.capacity:
				self.pop_front()



































public class LRUCache {
	private class Node {
		Node prev;
		Node next;
		int key;
		int value;
		public Node(int key, int value){
			this.key = key;
			this.value = value;
			this.prev = null;
			this.next = null;
		}
	}

	private int capacity;
	private HashMap<Integer, Node> hs = new HashMap<Integer, Node>();
	private Node head = new Node(-1, -1);
	private Node tail = new Node(-1, -1);

	public LRUCache(int capacity){
		this.capacity = capacity;
		tail.prev = head;
		head.next = tail;
	}
	
	public int get(int key) {
		if ( !hs.containsKey(key)) {
			return -1;
		}

		Node current = hs.get(key);
		current.prev.next = current.next;
		current.next.prev = current.prev;
		
		move_to_tail(current);
		return hs.get(key).value;
	}

	public void set(int key, int value){
		if (get(key) != -1) {
			hs.get(key).value = value;
			return;
		}
		if (hs.size() == capacity) {
			hs.remove(head.next.key);
			head.next = head.next.next;
			head.next.prev = head;
		}
		
		Node insert = new Node(key, value);
		hs.put(key,insert);
		move_to_tail(insert);
	}

	private void move_to_tail(Node current) {
		current.prev = tail.prev;
		tail.prev = current;
		current.prev.next = current;
		current.next = tail;
	}
}


