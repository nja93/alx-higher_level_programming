#include "lists.h"
/**
 * is_palindrome - function that checks if a singly linked list is a palindrom
 * Authhored byLorna Chege
 * @head: a pointer to the head node of linked list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *tmp_head = *head;
	int x = 0;
	int arr[10000];
	int index;
	int j;

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
	for (index = 0, j = x - 1; index < j; index++, j--)
	{
		if (arr[index] != arr[j])
			return (0);
	}
	return (1);
}
