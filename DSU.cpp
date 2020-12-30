#include <bits/stdc++.h>
using namespace std;

#define MAXIMUM 100001

int frnds[MAXIMUM];
int conns[MAXIMUM];

void init(int n)
{
    for (int i = 0; i <= n; i++)
    {
        frnds[i] = i;
        conns[i] = 1;
    }
    return;
}

int find(int v)
{
    if (frnds[v] == v)
        return frnds[v];
    return frnds[v] = find(frnds[v]);
}

int make_union(int x, int y)
{
    x = find(x);
    y = find(y);
    if (x != y)
    {
        if (conns[x] < conns[y])
            swap(x, y);
        conns[x] += conns[y];
        frnds[y] = x;
    }
    return conns[x];
}

int main()
{

    int t;
    cin >> t;
    while (t--)
    {
        int n;
        cin >> n;
        init(min(n * 2, MAXIMUM));
        map<string, int> name_id;
        int size = 0;
        for (int i = 0; i < n; i++)
        {
            string x, y;
            cin >> x >> y;
            int id_x = name_id[x];
            if (id_x == 0)
            {
                id_x = ++size;
                name_id[x] = id_x;
            }
            int id_y = name_id[y];
            if (id_y == 0)
            {
                id_y = ++size;
                name_id[y] = id_y;
            }
            cout << make_union(id_x, id_y) << endl;
        }
    }

    return 0;
}

/*
Sample Input
1
3
Fred Barney
Barney Betty
Betty Wilma
Sample Output
2
3
4
*/