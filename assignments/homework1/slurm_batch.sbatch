#!/bin/bash

#SBATCH --job-name=nikunj
#SBATCH --output=nikunj.out
#SBATCH --error=nikunj.err

##time: hh:mm:ss
#SBATCH --time=00:05:00

#SBATCH --partition=debug
#SBATCH --reservation=CSYE7374
#SBATCH -N 1


work=$HOME/csye7374-lad.n/homework1/part2/
cd $work

module load openmpi/3.1.2

mpicc mpi_hello.c -o mpi_hello
mpicc mpi_sendrecv.c -o mpi_sendrecv

gcc -o omp_func -fopenmp omp_func.c
gcc -o omp_hello -fopenmp omp_hello.c
gcc -o omp_loop -fopenmp omp_loop.c

gcc mm_serial.c -o mm_serial.c

mpirun -np 16 --mca btl ^openib --oversubscribe ./mpi_hello
mpirun -np 2 --mca btl ^openib --oversubscribe ./mpi_sendrecv

export OMP_NUM_THREADS=8

./omp_func
./omp_hello
./omp_loop

./mm_serial
