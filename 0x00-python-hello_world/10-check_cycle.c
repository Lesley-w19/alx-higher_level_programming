#include "lists.h"

/**
 * check_cycle - a function that checks if a singly linked
 * list has a cycle in it.
 * @list: the list
 *
 * Return: returns 1 if there is a cycle.
 * if there is no cycle, returns 0.
 */

int check_cycle(listint_t *list)
{
	listint_t *firstNext;
	listint_t *secondNext;

	firstNext = secondNext = list;

	if (list == NULL)
		return (0);

	while (firstNext && secondNext && firstNext->next)
	{
		secondNext = secondNext->next;
		firstNext = firstNext->next->next;

		if (secondHead == firstNext)
		{
			return (1);
		}
	}
	
	return (0);
}


