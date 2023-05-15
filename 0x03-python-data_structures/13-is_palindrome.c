#include "lists.h"
/**
 * is_palindrome -checks if a singly linked list is a palindrome.
 * Authoreed by Lorna Chege
 * @head: a pointer to the head node of linked list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *tmp_head = *head;
	int x = 0,  arr[10000], index, y;

	if (tmp_head == NULL || tmp_head->next == NULL)
		return (1);
	/*An empty list is considered a palindrome*/

	while (tmp_head != NULL)
	/*Copy the linked list values into the array*/
	{
		arr[x] = tmp_head->n;
		tmp_head = tmp_head->next;
		x++;
	}
	/*Check if the array is a palindrome*/
	for (index = 0, y = x - 1; index < y; index++, y--)
	{
		if (arr[indexi] != arr[y])
			return (0);
	}
	return (1);
}
