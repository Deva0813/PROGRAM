#include<iostream.h>
#include<conio.h>
#include<process.h>
float lcost[100],a[100][100];
int closest[100],i,j,k,min,n;
int v1,v2,wt,c=0;
class prim
{
public:
 void get_mat()
  {
   cout<<"Enter the No of Vertices:";
   cin>>n;
   cout<<"enter 1000 for no path \n";
   cout<<"enter weighted matrix"<<endl;
    for(i=1;i<=n;i++)
    {
     for(j=1;j<=n;j++)
     {
     cout<<"cost between the edge\t"<<i<<","<<j<<":\t";
     cin>>a[i][j];
     }//inner for
    }//outer for
   }//fn
void prim1()
  {
     for(i=2;i<=n;i++)
     {
     lcost[i]=a[1][i];
     closest[i]=1;
     }
     cout<<"minimum cost spanning tree edges are"<<endl;
   for(i=2;i<=n;i++)
   {
      min=lcost[2];
      k=2;
       for(j=3;j<=n;j++)
       {
	  if(lcost[j]<min)
	 {
	     min=lcost[j];
	     k=j;
	 }
       }
     c=c+min;
     cout<<"("<<closest[k]<<","<<k<<")"<<"\t"<<"cost="<<min<<"\t";
     lcost[k]=2000;
      for(j=2;j<=n;j++)
	if((a[k][j]<lcost[j])&&(lcost[j]<2000))
	{
	lcost[j]=a[k][j];
	closest[j]=k;
	}
	cout<<"\n";
   }//outer for
cout<<"\n\nWeight of minimum cost spanning tree :"<<c;
getch();
}
};
void main()
{
clrscr();
int ch;
prim p;
 do
 {
 cout<<"\n1.get\n2.find path with minimum cost\n3.exit\nenter ur choice\n";
 cin>>ch;
  switch(ch)
  {
   case 1:
    p.get_mat();
    break;
   case 2:
    p.prim1();
    break;
  case 3:
   exit(0);
   break;
  }//switch
}while(ch<=3);//do
getch();
}
