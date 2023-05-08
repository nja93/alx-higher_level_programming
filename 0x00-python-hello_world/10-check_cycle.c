#include "lists.h"


/**
 *check_cycle -checks if a signly linked list  has a cycle in it
 * by chege
 * @list: pointer to head of the linked list
 * Return: if 1 has a cycle. 0 is there is nocycle
 */

int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	if (list == NULL)
		return (0);

	slow = list;
	fast - list->next;

		while (fast != NULL && fast ->next != NULL)
		{
		if (slow == fast)
			return (1);

		slow = slow->next;
		fast = fast->next->next;
		}

		return (0);
}
