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
	listint_t *first;
	listint_t *second;

	first = second = list;

	if (list == NULL)
		return (0);

	while (first && second && first->next)
	{
		second = second->next;
		first = first->next->next;

		if (second == first)
		{
			return (1);
		}
	}
	
	return (0);
}


