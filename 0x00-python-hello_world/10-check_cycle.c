#include "lists.h"
/**
 * check_cycle - function that checks if a linked list has a cycle
 * @list: a pointer to a linked list
 *
 * Return: 0 if no cycle was found; 1 if there was any found
 */
int check_cycle(listint_t *list)
{
	listint_t *first *second;

	if (!list || !list->next)
		return (0);
	first = list;
	second = list;
	while (second != NULL && first != NULL && first->next != NULL)
	{
		second = second->next;
		first = first->next->next;
		if (second == first)
			return (1);
	}
	return (0);

}
