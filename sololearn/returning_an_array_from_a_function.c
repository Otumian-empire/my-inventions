/*
improvearrayfromfunction.c 
created (Editted) on Tuesday, 2019, 25 June
By Otumian
From a code created by Strugatskaya (https://www.sololearn.com/Profile/647730)
link: https://code.sololearn.com/c369R092tBDW/?ref=app#c
*/
#include <stdio.h>

void get_multiples(int n, int nums[], int size)
{
    int k;
    int multiple = 0;

    for (k = 0; k < size; k++)
    {
        nums[k] = multiple += n;
    }
}


int main()
{
    int asize = 10, a[asize];
    int bsize = 5, b[bsize];

    int k;

    get_multiples(2, a, asize); /* get first 10 even numbers */
    printf("a = [ ");
    for (k = 0; k < asize; k++)
        printf("%d ", a[k]);
    printf("]\n");
    /* output : a = [ 2 4 6 8 10 12 14 16 18 20]*/

    get_multiples(3, b, bsize); /* get first 5 multiples of 3 */
    printf("b = [ ");
    for (k = 0; k < bsize; k++)
        printf("%d ", b[k]);
    printf("]\n");
    /* output : b = [ 3 6 9 12 15 ]*/

    return 0;
}

