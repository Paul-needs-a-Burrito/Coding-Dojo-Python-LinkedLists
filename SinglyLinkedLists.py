# Assignment: Singly Linked Lists
# Objectives:
# Learn how linked lists work
# Learn more about pointers
# Learn how to traverse through a linked list
# Assignment: Additional Challenges
# 1. remove_from_front(self) - remove the first node and return its value
# 2. remove_from_back(self) - remove the last node and return its value
# 3. remove_val(self, val) - remove the first node with the given value
# Consider the following cases:
# the node with the given value is the first node
# the node with the given value is in the middle of the list
# the node with the given value is the last node
# 4. insert_at(self, val, n) - insert a node with value val as the nth node in the list
# Consider the following cases:
# n is 0
# n is the length of the list
# n is between 0 and the length of the list
# SENSEI BONUS: consider and account for edge cases for all methods
class SLNode:
    def __init__(self, val):
        self.value = val
        self.next = None


class SLList:
    def __init__(self):
        self.head = None

    def add_to_front(self, val):
        new_node = SLNode(val)
        new_node.next = self.head
        self.head = new_node
        return self

    def print_values(self):
        runner = self.head
        while(runner is not None):
            print(runner.value)
            runner = runner.next
        return self

    def _add_to_back(self, val):
        if self.head is None:
            self.add_to_front(val)
            return self
        new_node = SLNode(val)
        runner = self.head
        while(runner.next is not None):
            runner = runner.next
        runner.next = new_node
        return self

    def remove_from_front(self):
        if self.head is not None:
            self.head = self.head.next
        return self

    def remove_from_back(self):
        if self.head is None:
            return self
        elif self.head.next is None:
            self.head = None
            return self
        else:
            runner = self.head
            while(runner.next.next is not None):
                runner = runner.next
            runner.next = None
            return self

    def remove_val(self, val):
        if self.head is None:
            return self
        elif self.head.value == val:
            self.head = self.head.next
            return self
        else:
            runner = self.head
            while(runner is not None):
                if runner.next.value == val:
                    runner.next = runner.next.next
                    return self
                runner = runner.next
                if runner.next is None:
                    print("Value not found")
                    return self

    def insert_at(self, val, n):
        new_node = SLNode(val)
        if n == 0:
            new_node.next = self.head
            self.head = new_node
            return self

        counter = 1
        runner = self.head
        while(runner is not None):
            if counter == n:
                new_node.next = runner.next
                runner.next = new_node
                return self

            counter += 1
            runner = runner.next
            if runner.next is None:
                runner.next = new_node
                return self


new_list = SLList()
new_list.add_to_front("are").add_to_front("Linked Lists")._add_to_back("fun!").add_to_front("The").remove_from_back().print_values().insert_at("poop", 5).print_values().remove_val("crap").print_values()

# while loops:
# runner = self.head translates to:
#     "runner point to where self.head is pointing to"

# runner = runner.next translates to:
#     "runner point to where runner.next is pointing to"

# insert_at(self, val, n) alternate (better) method:
#     instead of a counter, use a loop to move runner.next to correct node. For example:
#         for i in range(1, n-1):
#           runner = runner.next
#           return self
# then insert node:
#     new_node.next = runner.next
#     runner.next = new_node
