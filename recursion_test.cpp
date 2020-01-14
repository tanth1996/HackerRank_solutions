#include <cstdlib>
#include <iostream>

typedef struct list_node 
{
    int data;
    struct list_node * next;
} node;

int sum_list(node* l)
{
    if(l == NULL)
    {
        return 0;
    }
    int sum = l->data + sum_list(l->next);
    std::cout << l->data << std::endl;
    return sum;
}

int main() {
    node Head;
    node* Head_ptr = &Head;
    Head_ptr->data = 1;
    Head.next = NULL;
    std::cout << Head.data << std::endl;
    std::cout << Head.next << std::endl;
    
    node* node_ptr = Head_ptr;
    
    for (int i=0; i < 10; i++)
    {
        node_ptr->data = i;
        node_ptr->next = (node*) malloc(sizeof(node));
        node_ptr = node_ptr->next;
        node_ptr->next = NULL;
        node_ptr->data = 0;
    }
    
    int sum = 0;
    sum = sum_list(Head_ptr);
    std::cout << sum;
}