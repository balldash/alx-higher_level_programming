#include "lists.h"

/**
 * check_cycle - Checks if a singly-linked list contains a cycle
 * @list: A singly_linked list
 * Return: 0 if non, 1 if there is one
 */

int check_cycle(listint_t *list)
{
	listint_t *t, *h;

	if (list == NULL || list->next == NULL)
		return (0);

	t = list->next;
	h = list->next->next;

	while (t && h && h->next)
	{
		if (t == h)
			return (1);
		t = t->next;
		h = h->next->next;
	}

	return (0);
}
