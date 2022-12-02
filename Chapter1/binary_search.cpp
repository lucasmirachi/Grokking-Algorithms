#include <iostream>
#include <cmath>
using namespace std;

int list[] = {1, 2, 3, 4, 5, 6, 7, 8, 9}; //Change these values for testing
int item = 6; //Can also change for testing

int guess, mid;
int low = 0;
int high = size(list) - 1; 

int binarySearch(int list[], int item, int low, int high) {
    while  (low <= high) {
        int mid = floor((low+high)/2); //floor will round the division down in order to result in an integer
        int guess = list[mid];
        // cout << "mid: " << mid << "\n" << "high: " << high << "\n" << "low: " << low << "\n" << "guess: " << guess << "\n";
        if (guess == item) {
            return guess;
        }
        else if (guess < item) {
            low = mid + 1;
        }
        else {
            high = mid - 1;
        }
    }
    return 0;
}

int main() {
  guess = binarySearch(list, item, low, high);
  if (guess == 0){
    cout << "Error\n";
  }
  else{
    cout << "The chosen item was " << item << " and the algorithm guessed " << guess << "\n";
  }
  return 0;
}