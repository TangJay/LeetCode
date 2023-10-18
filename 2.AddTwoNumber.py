class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def makeIntoListNode(self, listnode, numList):
        listnode2 = listnode
        for i in numList:
            listnode2.val = i
            listnode2.next = ListNode()
            listnode2 = listnode2.next
        return listnode


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        list1 = []
        list2 = []
        while True:
            list1.append(l1.val)
            if l1.next == None:
                break
            else:
                l1 = l1.next
        while True:
            list2.append(l2.val)
            if l2.next == None:
                break
            else:
                l2 = l2.next
        num1 = 0
        num2 = 0
        for i in range(len(list1)):
            num1 += list1[i] * (10**i)
        for i in range(len(list2)):
            num2 += list2[i] * (10**i)
        num3 = num1 + num2
        print(num3)
        times = 0
        listnode = ListNode()
        numList = []
        while True:
            numList.append(num3 // (10**times)) % 10
            if num3 // (10 ** (times + 1)) == 0:
                break
            times += 1
        answer = listnode.makeIntoListNode(listnode, numList)
        return answer


if __name__ == "__main__":
    obj = Solution()
    listNode = ListNode()
    listNode2 = ListNode()
    l1 = listNode.makeIntoListNode(listNode, [int(i) for i in input().split()])
    l2 = listNode2.makeIntoListNode(listNode, [int(i) for i in input().split()])
    ans = obj.addTwoNumbers(l1, l2)
    print(ans)
