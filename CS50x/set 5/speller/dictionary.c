// Implements a dictionary's functionality

#include "dictionary.h"
#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// Number of buckets in hash table
const unsigned int TABLE_SIZE = 50000;

// Hash table //set N to a higher number to capture data.
node *table[TABLE_SIZE];

// Returns true if word is in dictionary else false
bool check(const char *word)
{
    // returns true if found else return false.
    int index = hash(word);
    // make a cursor node which points to the head of the hash table
    node *cursor = table[index];
    // for loop to go through the list until the final node is reached.
    for (node *temp = cursor; temp != NULL; temp = temp->next)
    {
        if (strcasecmp(temp->word, word) == 0)
        {
            return true;
        }
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // getting the lengh of the string and sumation the value of characters.
    unsigned int value = 0;
    for (int i = 0; i < strlen(word); i++)
    {
        value = value + tolower(word[i]);
        value = (value * tolower(word[i]));
        value = value % TABLE_SIZE;
    }
    return value;
}

int counter = 0;

// loading dictionary into memory and return true and fulse if that is successful or unsuccessful
bool load(const char *dictionary)
{

    // allocating memory for nodes and add data to them
    // copy words into the character array strcpy

    // OPEN DICTIONARY FILE and read the contents
    FILE *file = fopen(dictionary, "r");
    if (file == NULL)
    {
        fprintf(stderr, "There has been an error");
        return false;
    }

    // make a character array of the words
    char word_list[LENGTH + 1];

    // cheking fscanf != EOF
    while (fscanf(file, "%s", word_list) != EOF)
    {
        counter++;
        node *new_Node = malloc(sizeof(node));
        if (new_Node == NULL)
        {
            return 1;
        }

        // initialize the new node by copying the word in to the next node.
        strcpy(new_Node->word, word_list);
        new_Node->next = NULL;
        int index = hash(word_list);
        if (table[index] == NULL)
        {
            table[index] = new_Node;
        }

        else
        {
            // makes the next the new head
            new_Node->next = table[index];
            // head points to the new node.
            table[index] = new_Node;
        }
    }
    fclose(file);
    return true;
}

// Returns number of words in dictionary if loaded else 0 if not yet loaded
unsigned int size(void)
{
    // keep track of how many nodes have been added.
    return counter;
}

// Unloads dictionary from memory, returning true if successful else false
bool unload(void)
{

    // make a cursor which points to the head node
    node *tmp = NULL;
    node *cursor = NULL;
    for (int i = 0; i < TABLE_SIZE; i++)
    {
        cursor = table[i];
        while (cursor != NULL)
        {
            tmp = cursor;
            cursor = cursor->next;
            free(tmp);
        }
    }
    return true;
}