#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include "lists.h"
/**
 * insert_node - inserts number into the sorted list
 * @head: linked list
 * @number: number to insert
 * Return: pointer to the new head
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head;
	listint_t *new = NULL;
	listint_t *temporary = NULL;

	if (!head)
		return (NULL);
	new = malloc(sizeof(listint_t));

	if (!new)
		return (NULL);
	new->n = number;
	new->next = NULL;

	if (!head || (*head)->n > number)
	{
		new->next = *head;
		return (*head = new);
	}
	else
	{
		while (current && current->n < number)
		{
			temporary = current;
			current = current->next;
		}
		temporary->next = new;
		new->next = current;
	}
	return (new);
}

