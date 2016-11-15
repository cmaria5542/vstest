#include <stdio.h>

int main(int x)
{
    int oldest_number = 0;
    int next_number = 1;

    for (int i = 0; i < x; i++) {
        int next_number = int oldest_number + int next_number;
        int oldest_number = int next_number - int oldest_number;
    }
    return oldest_number;
}