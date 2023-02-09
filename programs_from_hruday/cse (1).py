#paaterns
for i in range(4):
    print("* "*4)

'''output:
* * * * 
* * * * 
* * * * 
* * * * '''

for i in range(4):
    for j in range(4):
        if i==0 or i==3:
            print("*",end=" ")
        elif j==0 or j==3:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
'''
output:
* * * * 
*     * 
*     * 
* * * * '''

for i in range(10):
    print("* "*i)

'''output:
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * * * 
* * * * * * * 
* * * * * * * * 
* * * * * * * * * '''

n=int(input())
for i in range(1,n+1):
    for j in range(i):
        if i==1 or i==n or j==0 or j==i-1: 
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
'''
output:
10
* 
* * 
*   * 
*     * 
*       * 
*         * 
*           * 
*             * 
*               * 
* * * * * * * * * * '''

n=int(input())
for i in range(n):
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(i):
        print("*",end=" ")
    print()
'''
output:
    		  * 
                * * 
              * * * 
            * * * * 
          * * * * * 
        * * * * * * 
      * * * * * * * 
    * * * * * * * * 
  * * * * * * * * * '''

n=int(input())
for i in range(n):
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(n):
        if j==0 or j==i or i==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
'''
output:
	 	    *                   
                  * *                 
                *   *               
              *     *             
            *       *           
          *         *         
        *           *       
      *             *     
    *               *   
  * * * * * * * * * * '''
n=int(input())
for i in range(n):
    for j in range(n-i):
        print("*",end=" ")
    print(" ")
'''
output:
* * * * *  
* * * *  
* * *  
* *  
*  '''

n=int(input())
for i in range(n):
    for j in range(i):
        print(" ",end=" ")
    for j in range(n,i,-1):
        print("*",end=" ")
    print()

'''
output:
* * * * * 
  * * * * 
    * * * 
      * * 
        * '''

n=int(input())
for i in range(n):
    for j in range(n-i):
        print("*",end=" ")
    for j in range(2*i):
        print(" ",end=" ")
    for j in range(n,i,-1):
        print("*",end=" ")
    print(" ")
'''
output:
* * * * * * * * * * * * * * * * * * * *  
* * * * * * * * *     * * * * * * * * *  
* * * * * * * *         * * * * * * * *  
* * * * * * *             * * * * * * *  
* * * * * *                 * * * * * *  
* * * * *                     * * * * *  
* * * *                         * * * *  
* * *                             * * *  
* *                                 * *  
*                                     *  '''

n=int(input())
for i in range(n):
 for j in range(2*n):
    if(j<=i or j>=2*n-i-1):
        print("*",end=" ")
    else:
        print(" ",end=" ")
 print()

'''
output:
*                 * 
* *             * * 
* * *         * * * 
* * * *     * * * * 
* * * * * * * * * * '''

#11.model:2:

n=int(input())
for i in range(n):
 for j in range(2*n):
    if(j<=n-i-1 or j>=n+i):
        print("*",end=" ")
    else:
        print(" ",end=" ")
 print()
'''
output:
* * * * * * * * * * 
* * * *     * * * * 
* * *         * * * 
* *             * * 
*                 * '''

n=int(input())
for i in range(n):
    for j in range(2*n):
        if(j<=n-i-1 or j>=n+i):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
for i in range(n):
    for j in range(2*n):
        if(j<=i or j>=2*n-i-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

'''
output:
* * * * * * * * * * 
* * * *     * * * * 
* * *         * * * 
* *             * * 
*                 * 
*                 * 
* *             * * 
* * *         * * * 
* * * *     * * * * 
* * * * * * * * * * '''


n=int(input())
for i in range(n):
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(2*i+1):
        print("*",end=" ")
    print()
for i in range(n-2,-1,-1):
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(2*i+1):
        print("*",end=" ")
    print()

'''
output:
  	  * 
        * * * 
      * * * * * 
    * * * * * * * 
  * * * * * * * * * 
    * * * * * * * 
      * * * * * 
        * * * 
          * '''

n=int(input())
for i in range(n):
    for j in range(2**n):
        if (j>=0*n and j<i+1 and j<1*n) or (j>=1*n and j<1*n+i+1 and j<2*n) or (j>=2*n and j<2*n+i+1 and j<3*n) or (j>=3*n and j<3*n+i+1 and j<4*n):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

'''
output:
6
*           *           *           *                                                                                           
* *         * *         * *         * *                                                                                         
* * *       * * *       * * *       * * *                                                                                       
* * * *     * * * *     * * * *     * * * *                                                                                     
* * * * *   * * * * *   * * * * *   * * * * *                                                                                   
* * * * * * * * * * * * * * * * * * * * * * * *'''
