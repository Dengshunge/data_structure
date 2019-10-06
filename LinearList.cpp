#include <iostream>
#include <vector>
using namespace std;

struct ListNode {
	int val;
	ListNode *next;
	ListNode(int x) : val(x), next(NULL) {}
};

class LinearList
{
public:
	ListNode * ListCreat(vector<int> nums)
	{
		if (nums.empty())
			return nullptr;
		ListNode *head = new ListNode(-1);
		ListNode *p = head;
		for (auto m : nums)
		{
			p->next = new ListNode(m);
			p = p->next;
		}
		return head->next;
	}

	void ListPrint(ListNode *head)
	{
		ListNode *p = head;
		while (p)
		{
			cout << p->val << " ";
			p = p->next;
		}
		cout << endl;
	}
};
