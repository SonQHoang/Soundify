class Node {
    constructor(val) {
        this.val = val;
        this.next = null;
    }
}

const a = new Node('A');
const b = new Node('B');
const c = new Node('C');
const d = new Node('D');

a.next = b;
b.next = c;
c.next = d;

//  A => B => C => D => NUll
// cur

const printedLinkedList = (head) => {
    // Starting at the beginning of the linkedList
    let current = head;
    // If we aren't at null, then there's more to iterate over
    while (current !== null) {
        console.log(current.val)
        // Moves the current pointer to next
        current = current.next;
    }
}

printedLinkedList(a);

// RECURSIVE VERSION

//  A => B => C => D => NUll
//                      head

const printLinkedListRecursive = (head) => {
    if (head === null) return;
    console.log(head.val)
    printLinkedListRecursive(head.next)
}

printLinkedListRecursive(a)