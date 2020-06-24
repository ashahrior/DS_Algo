#include<bits/stdc++.h>
using namespace std;

int linear_search(int ar[], int n, int x) {

    for(int i=0; i<n; i++) {
        if(ar[i]==x)
            return i;
    }

    return -1;
}

int main()
{
    int n = 5;

    int ar[n] = {1,4,6,2,0};

    int x = 2;

    int pos = linear_search(ar,n,x);

    if(pos>-1)
        cout<<x<<" Found at "<<pos+1<<endl;
    else cout<<x<< " Not found"<<endl;

    return 0;
}
