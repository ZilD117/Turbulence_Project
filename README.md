# Turbulence_Project

In this file, there will be sections as follows:

1. AthenaPK build Instruction/Command   
2. Generating Turbulence files based on a given parameter file turbulence.in   
3. Analyzing hdf5 files using Philip's Energy Transfer Analysis code.

# 1. AthenaPK Build instruction:
> module purge
> 
> module load GCCcore/11.2.0 CMake/3.22.1 git/2.27.0 GCC/11.2.0 Ninja/1.10.2 OpenMPI/4.1.1-CUDA-11.8.0
> 
> cmake -S . -Bbuild-pk -DKokkos_ARCH_NATIVE=ON -DKokkos_ENABLE_OPENMP=ON -DKokkos_ENABLE_CUDA=ON -DKokkos_ARCH_AMPERE80=ON
> 
> cd build-pk && make
