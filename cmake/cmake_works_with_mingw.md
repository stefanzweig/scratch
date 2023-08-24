# How to make cmake make things with gcc

Nowadays I am working on a project running both on linux and on windows. I have to compile some libs with **cmake**. On ubuntu the compiler by default is the gcc, while in windows the toolchain is quite complicated that msvc is used by default. I need compile the lib with mingw64 toolchain. I have to configure the cmake's Makefile to use gcc.

The solution is `-G` option.

```shell
cmake -G"Unix Makefiles" ../

cmake -G"MinGW Makefiles" ../
```

A Makefile with gcc is made. The the build command works.

```shell
cmake --build .
```