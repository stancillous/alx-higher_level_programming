int is_palindrome(listint_t **head)
{
  listint_t *trav = *head;
  int i = 0, len;
  int a , b; /*for looping*/
  int *mylist;

  if (*head == NULL)
  {
    return (1);
  }
  mylist = malloc(sizeof(int *));
  if (mylist == NULL)
  {
    return (0);
  }
  
  while (trav->next != NULL)
    {
      mylist[i] = trav->n;
      i++;
      trav = trav->next;
    }
  mylist[i] = trav->n;
  len = i + 1;

   int reversedList[len];
    
    /*Iterate through the original list and*/
  /*add elements to the new list in reverse order*/
    for (a = len - 1, b = 0; a >= 0; a--, b++) {
        reversedList[b] = mylist[a];
    }

  for (a = 0; a < len; a++)
    {
      if (mylist[a] != reversedList[a])
      {
        return (0);
      }
    }
  return (1);
  
}
