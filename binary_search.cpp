#include<bits/stdc++.h>
using namespace std;

int binary_search_recursive(int ar[], int x, int left, int right) {
    if(left>right)
        return -1;
    int mid = left + ((right-left)/2);
    if(ar[mid]==x)
        return mid;
    else if(ar[mid]>x)
        binary_search_recursive(ar, x, left, mid-1);
    else
        binary_search_recursive(ar,x,mid+1,right);
}

int binary_search_iterative(int ar[], int x, int right)
{
    int left = 0;

    while(left<=right) {
        int mid = left + ((right-left)/2);
        if(ar[mid]==x)
            return mid;
        else if(ar[mid]<x)
            left = mid+1;
        else right = mid-1;
    }
    return -1;
}

int main() {

    int ar[] = {1,5,7,8,12,34,65,99};
    size_t n = sizeof(ar)/sizeof(ar[0]);
    int x = 34;
    int y = 8;
    int p = binary_search_recursive(ar,x,0,n-1);
    int q = binary_search_iterative(ar,y,n-1);

    if(p>-1)
        cout<< x << " found at "<<p<<endl;
    else cout<< x << " not found"<<endl;

    if(q>-1)
        cout<< y << " found at "<<q<<endl;
    else cout<< y << " not found"<<endl;


    return 0;
}
