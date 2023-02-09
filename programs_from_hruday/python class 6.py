#m*n patterns
n=int(input("Enter a number: "))
m=int(input("Enter the number of repetations: "))
for i in range(n):
    for j in range(m):
        for k in range(i+1):
            print("*",end=" ")
        for k in range(n-i-1):
            print(" ",end=" ")
    print()
o/p:
Enter a number: 5
Enter the number of repetations: 5
*         *         *         *         *         
* *       * *       * *       * *       * *       
* * *     * * *     * * *     * * *     * * *     
* * * *   * * * *   * * * *   * * * *   * * * *   
* * * * * * * * * * * * * * * * * * * * * * * * * 

#spiral matrices
n=int(input("Enter a number: "))
size=2*n-1
a=[[n for i in range(size)]for j in range(size)]
for i in range(size//2):
    for j in range(i,size-i-1):
        a[i][j]=i+1
        a[j][size-i-1]=i+1
        a[size-i-1][size-j-1]=i+1
        a[size-j-1][i]=i+1
for i in a:
    for j in i:
        print(j,end=" ")
    print()
    
o/p:
Enter a number: 5
1 1 1 1 1 1 1 1 1 
1 2 2 2 2 2 2 2 1 
1 2 3 3 3 3 3 2 1 
1 2 3 4 4 4 3 2 1 
1 2 3 4 5 4 3 2 1 
1 2 3 4 4 4 3 2 1 
1 2 3 3 3 3 3 2 1 
1 2 2 2 2 2 2 2 1 
1 1 1 1 1 1 1 1 1