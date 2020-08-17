#include <iostream>

using namespace::std;

void selection_sort(int x[40],int n);

int main()
{
    int a[40], n;
    cout<<"enter the numebr of elements in the data to be sorted:"<<endl;
    cin>>n;
    cout<<"enter data:"<<endl;
    for(int i=0;i<n;i++)
        cin>>a[i];
    selection_sort(a,n);
    cout<<"sorted data is:"<<endl;
    for(int i=0;i<n;i++)
        cout<<a[i]<<endl;
}
void selection_sort(int x[40],int n)
{
    int small, pos=0;
    for(int i=0;i<n;i++)
    {
        small=x[i];
        for(int j=i;j<n;j++)
        {
            if(small>x[j])
            {
                small=x[j];
                pos=j;
            }
        x[pos]=x[i];
        x[i]=small;
        }

    }
}
