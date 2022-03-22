#include <iostream>
#include <cmath>
using namespace std;

int main()
{
    int t;
    scanf("%d", &t);

    // cout << "t: " << t << endl;

    for (int i = 0; i < t; i++)
    {
        int n, c;
        cin >> n >> c;
        // scanf("%d %d", &n, &c);
        cout << ceil(n/(c+0.0)) + 1 << endl;
    }

    return 0;
}