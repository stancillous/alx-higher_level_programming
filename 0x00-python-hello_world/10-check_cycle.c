#include "lists.h"

/**
 * check_cycle - checks for loop in linked list
 * @list:  head pointer passed
 * Return: 0 (absent) or 1(present)
 */

int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	if (!list || !list->next)
		return (0);

	while (slow && fast && fast->next->next)
	{
		if (slow == fast)
			return (1);
		slow = slow->next;
		fast = fast->next->next;
	}
	return (0);
}
