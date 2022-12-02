# Chapter 2 Notes

## Arrays vs Linked Lists

Basically the difference between **arrays** and **linked lists** is that arrays are 



| **Array**      | **Linked List** |
| ----------- | ----------- |
| Header An array is a collection of elements of a similar data type.     | A Linked list is a group of objects called nodes, which consists of two fields: data and address to the next node       |
| An array stores elements in a contiguous memory location.   | Linked lists store elements randomly at any address in the memory.        |
| In an array, memory size is fixed while declaration and cannot be altered at run time.   | Linked lists utilize dynamic memory, i.e. memory size can be altered at run time.       |
| Elements in an array are not dependent on each other.  | Elements in a linked list are dependent on each other, as each node stores the address of its next node.       |
| Operation like insertion, deletion, etc., takes more time in an array.  | Operations like insertion, deletion, etc., take less time than arrays.        |
| Memory is allocated at compile time.   | Memory is allocated at run time.       |
| It is easier and faster to access the element in an array with the help of Indices.   | Accessing an element in a linked list is time-consuming as we have to start traversing from the first element.        |
| Memory utilization is ineffective in arrays. For example, if the array size is 5 and contains only 2 elements, the rest of the space will be wasted.   | In linked lists, memory utilization is effective, as it can be allocated or deallocated at the run time according to our requirement.        |

![array](https://scaler.com/topics/images/reading-and-writing-of-an-array.webp)


![linked-list](https://scaler.com/topics/images/creating-a-linked-list.webp)