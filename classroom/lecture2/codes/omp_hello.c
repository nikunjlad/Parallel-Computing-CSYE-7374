#include <omp.h>
#include <stdio.h>
#include <stdlib.h>

int main (int argc, char *argv[])
{
    int nthreads, tidl;

    // fork a team of threads giving them their own copies of variables
    #pragma omp parallel private(nthreads, tid)
    {
        // obtain thread number
        tid  = omp_get_thread_num();
        printf("Hello World from thread = %d\n", tid);

        if (tid == 0)
        {
            nthreads = omp_get_num_threads();
            printf("Number of threads = %d\n", nthreads);
        }
    }  // all threads join master thread and disband
}
