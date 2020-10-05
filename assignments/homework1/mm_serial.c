#include <stdio.h>
#include <stdlib.h>

#define NRA 62          /* number of rows in matrix A */
#define NCA 15          /* number of columns in matrix A */
#define NCB 7           /* number of columns in matrix B */

int main(int argc, char *argv[])
{
  struct timeval start_time, end_time;
  gettimeofday(&start_time, NULL);

  int    i, j, k;         /* misc */
  double a[NRA][NCA],         /* matrix A to be multiplied */
         b[NCA][NCB],         /* matrix B to be multiplied */
         c[NRA][NCB];     /* result matrix C */

  printf("Starting serial matrix multiple example...\n");
  printf("Using matrix sizes a[%d][%d], b[%d][%d], c[%d][%d]\n",
          NRA,NCA,NCA,NCB,NRA,NCB);

  /* Initialize A, B, and C matrices */
  printf("Initializing matrices...\n");
  for (i=0; i<NRA; i++)
     for (j=0; j<NCA; j++)
        a[i][j]= i+j;
  for (i=0; i<NCA; i++)
     for (j=0; j<NCB; j++)
        b[i][j]= i*j;
  for(i=0;i<NRA;i++)
     for(j=0;j<NCB;j++)
        c[i][j] = 0.0;

  /* Perform matrix multiply */
  printf("Performing matrix multiply...\n");
  for(i=0;i<NRA;i++)
     for(j=0;j<NCB;j++)
        for(k=0;k<NCA;k++)
           c[i][j]+= a[i][k] * b[k][j];

  /*
  printf("Here is the result matrix:");
  for (i=0; i<NRA; i++) {
     printf("\n");
     for (j=0; j<NCB; j++)
        printf("%6.2f   ", c[i][j]);
     }
  */
  printf ("\nDone.\n");
  gettimeofday(&end_time, NULL);
  long seconds = (end_time.tv_sec - start_time.tv_sec);
  long micros = ((seconds * 1000000) + end_time.tv_usec) - (start_time.tv_usec);
  printf("Time elpased is %d seconds and %d micros\n", seconds, micros);
}
