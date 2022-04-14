#include<iostream>
using namespace std;
class Sample
{
    private:
        int x; 
        int y;
    public:
        Sample(int p, int q) : x(5), y(15)
        {
            this -> x = p;
            this -> y = q;
        }
        void printxy()
        {
            cout << x << " " << y << "\n";
        }
};
int main(void)
{
    Sample s1(10,20);
    s1.printxy();
    return 0;
}