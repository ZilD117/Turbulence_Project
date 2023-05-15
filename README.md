# Turbulence_Project

# AthenaPK Build instruction:
> module purge
> module load GCCcore/11.2.0 CMake/3.22.1 git/2.27.0 GCC/11.2.0 Ninja/1.10.2 OpenMPI/4.1.1-CUDA-11.8.0 
> cmake -S . -Bbuild-pk -DKokkos_ARCH_NATIVE=ON -DKokkos_ENABLE_OPENMP=ON -DKokkos_ENABLE_CUDA=ON -DKokkos_ARCH_AMPERE80=ON
> cd build-pk && make
