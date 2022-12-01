#include <iostream>
#include <cmath>
using namespace std;

int list[] = {1, 2, 3, 4, 5, 6, 7, 8, 9}; //Change these values for testing
int item = 8; //Can also change for testing

int guess;
int low = 0;
int high = size(list) - 1; 

int binarySearch(int list[], int item) {
    int mid = floor((low+high)/2);
    int guess = list[mid];
    while  (low <= high) {
        
        cout << "mid: " << mid << "\n" << "high: " << high << "\n" << "low: " << low << "\n";
        if (guess == item) {
            return guess;
        }
        else if (guess < item) {
            low = mid + 1;
        }
        else {
            high = mid - 1;
        }
        return guess;
    }
    return 0;
}

int main() {
    binarySearch(list, item);
    cout << "The chosen item was " << item << " and the algorithm guessed " << guess << "\n";
    return 0;
}


/* 
// Binary Search in C++

int binarySearch(int array[], int x, int low, int high) {
  
	// Repeat until the pointers low and high meet each other
  while (low <= high) {
    int mid = low + (high - low) / 2;

    if (array[mid] == x)
      return mid;

    if (array[mid] < x)
      low = mid + 1;

    else
      high = mid - 1;
  }

  return -1;
}

int main(void) {
  int array[] = {3, 4, 5, 6, 7, 8, 9};
  int x = 4;
  int n = sizeof(array) / sizeof(array[0]);
  int result = binarySearch(array, x, 0, n - 1);
  if (result == -1)
    printf("Not found");
  else
    printf("Element is found at index %d", result);
} */