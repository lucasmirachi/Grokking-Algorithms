#include <iostream>
#include <vector>
using namespace std;

vector<int> newArr;
int arr[] = {5, 3, 6, 2, 10};
int length = size(arr);

int searchLower(int arr[]){
    int lower = arr[0];
    int lower_index = 0;

    for (int i = 0; i <= length; i++){
        if (arr[i] < arr[lower_index]){
            lower = arr[i];
            lower_index = i;
        }
    return lower_index;
    }
}

vector<int> selectionSort(int arr[]){
    for (int i = 0; i <= length; i++){
        int lower =  searchLower(arr);
        newArr.push_back(lower);
    }
    return newArr;
}

// function to print an array
void printArray(vector<int> arr, int size) {
  for (int i = 0; i < size; i++) {
    cout << arr[i] << " ";
  }
  cout << endl;
}

int main() {
   newArr = selectionSort(arr); 
   printArray(newArr, length);
   return 0;
}