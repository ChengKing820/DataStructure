"""
双链表数据结构

"""


class Node:   # 链表节点类
    def __init__(self, data, the_next=None, the_pre=None):
        self.data = data
        self.the_next = the_next
        self.the_pre = the_pre

    def __repr__(self):
        return str(self.data)


class ChainDouble:    # 双链表类
    def __init__(self):
        self.head = None
        self.length = 0

    def is_empty(self):
        return not self.length

    def append(self, item):    # 结尾插入新节点
        if isinstance(item, Node):
            node = item

        else:
            node = Node(item)

        if self.head is None:
            self.head = node
        else:
            pre_node = self.head
            while pre_node.the_next:  # 从头部开始找链表结尾
                pre_node = pre_node.the_next
            node.the_pre = pre_node
            pre_node.the_next = node
        self.length += 1

    def insert(self, index, item):   # 在某位置插入新节点
        if self.is_empty():
            print('当前链表为空')
            return 0

        if index >= self.length:
            print('index 溢出')
            return 0

        insert_node = Node(item)
        node = self.head

        if index < 0:   # index<0 则在链表头部添加
            node.the_pre = insert_node
            insert_node.the_next = node
            self.head = insert_node
            self.length += 1
            return 0

        count = 0
        while True:
            if count == index:
                next_node = node.the_next
                node.the_next = insert_node
                insert_node.the_next = next_node
                insert_node.the_pre = node
                self.length += 1
                return 0
            node = node.the_next
            count += 1

    def delete(self, index):
        if self.is_empty():
            print('当前链表为空')
            return 0
        if index < 0 or index >= self.length:
            print('index 溢出')
            return 0

        node = self.head
        if index == 0:   # index为0时特殊情况
            node_next = node.the_next
            node_next.the_pre = None
            self.head = node_next

        else:
            count = 0
            while True:
                count += 1
                if index == count:
                    node.the_next = node.the_next.the_next
                    if index < self.length-1:   # 如果删除最后一个节点，则不需要修改前置
                        node.the_next.the_pre = node
                    break
                node = node.the_next
        self.length -= 1

    def __repr__(self):
        if self.is_empty():
            return "当前链表为空"
        n_list = ""
        node = self.head
        while node:
            n_list += node.data + ''
            node = node.the_next
        return n_list


if __name__ == '__main__':
    chain = ChainDouble()
    chain.append('A')
    chain.append('B')
    chain.append('C')
    chain.append('D')
    chain.append('E')
    chain.append('F')
    chain.append('G')
    chain.delete(6)
    # chain.insert(-3, 'p')
    print(chain, chain.length)
