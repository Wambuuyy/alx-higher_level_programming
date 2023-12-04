#include "lists.h"
#include <stdlib.h>

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to pointer of the first node of the list
 * Return: 1 if it is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
    listint_t *slow, *fast, *prev = NULL, *temp;
    int is_palindrome = 1;

    if (*head == NULL || (*head)->next == NULL)
        return 1; // An empty list or a list with one element is a palindrome

    slow = *head;
    fast = *head;

    // Find the middle of the list using slow and fast pointers
    while (fast != NULL && fast->next != NULL)
    {
        fast = fast->next->next;

        // Reverse the first half of the list
        temp = slow->next;
        slow->next = prev;
        prev = slow;
        slow = temp;
    }

    // If the list has odd number of elements, move slow to the next node
    if (fast != NULL)
        slow = slow->next;

    // Compare the reversed first half with the second half
    while (prev != NULL && slow != NULL)
    {
        if (prev->n != slow->n)
        {
            is_palindrome = 0;
            break;
        }

        // Move to the next nodes for comparison
        prev = prev->next;
        slow = slow->next;
    }

    // Restore the original list by reversing the first half back
    while (slow != NULL)
    {
        temp = slow->next;
        slow->next = prev;
        prev = slow;
        slow = temp;
    }

    // Update the head to point to the start of the restored list
    *head = prev;

    return is_palindrome;
}

