# Chapter 2 - Notes

## Arrays vs Linked Lists

When you are a beginner, it is natural that you may think that arrays and linked lists can perform the same function equally, but there are some nuances in their structures that can make them be used for different functions. 

Basically, both arrays and lists are linear data structures that store data in memory, however the main difference is that an <mark>**Array** stores data elements in contiguous memory locations, thus allowing faster access using array indexes</mark> while a <mark>**Linked list** contains a sequence of data elements where each element is linked to its next element with the help of pointers.</mark>

For better fixation, you can think of a linked list like a "treasure map": when you go to the first item and it says *"the next item can be found at address 123"* and when you go there, it says *"the next item can be found at address 456"* and so on. Also, because a linked list uses addresses in memory, it doesn't have a fixed length and that's why adding items on it is much easier. 

![linked-list](https://scaler.com/topics/images/creating-a-linked-list.webp)

However, this also gives a "problem" to linked lists. Imagine you have a list of 10 elements and want to check the 8th element. In a linked list, because you can only know the address of the next item, to go to the 8th element you need to first go to the 1st item to know the address of the 2nd item. Then you go to the 2nd item to know the address of the 3rd item and so on until you can finally achieve the 8th item address... now imagine if this list had 1000 items! 

That's why if you want to know random values inside a list arrays are much more efficient! You know the address of each item and they are independent on each other! However, because arrays stores elements in a contiguous memory location, it need to have a fixed length and if you need to insert or delete an item it takes more time because you need to rearrange everything.

![array](https://scaler.com/topics/images/reading-and-writing-of-an-array.webp)

According to the book's author, here is a table with the execution time of reading and operating on each of the lists:

| Operation | **Array** | **Linked List** |
| ----------- | ----------- | ------|
| Read | O(1) | O(n)|
| Insert / Delete | O(n) | O(1)|
Where: *O(n) = Linear execution time* and *O(1) = Constant execution* tiem

Bellow is a table I took from [Scaler.com](https://www.scaler.com/topics/difference-between-array-and-linked-list/) where it resumes well the differences between arrays and linked lists:

| **Array**      | **Linked List** |
| ----------- | ----------- |
| An array is a collection of elements of a similar data type.     | A Linked list is a group of objects called nodes, which consists of two fields: data and address to the next node       |
| An array stores elements in a contiguous memory location.   | Linked lists store elements randomly at any address in the memory.        |
| In an array, memory size is fixed while declaration and cannot be altered at run time.   | Linked lists utilize dynamic memory, i.e. memory size can be altered at run time.       |
| Elements in an array are not dependent on each other.  | Elements in a linked list are dependent on each other, as each node stores the address of its next node.       |
| Operation like insertion, deletion, etc., takes more time in an array.  | Operations like insertion, deletion, etc., take less time than arrays.        |
| Memory is allocated at compile time.   | Memory is allocated at run time.       |
| It is easier and faster to access the element in an array with the help of Indices.   | Accessing an element in a linked list is time-consuming as we have to start traversing from the first element.        |
| Memory utilization is ineffective in arrays. For example, if the array size is 5 and contains only 2 elements, the rest of the space will be wasted.   | In linked lists, memory utilization is effective, as it can be allocated or deallocated at the run time according to our requirement.        |






