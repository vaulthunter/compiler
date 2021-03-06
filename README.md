# Language X 
### Win : [![Build status](https://ci.appveyor.com/api/projects/status/xe77ex6oxl497xjm/branch/master?svg=true)](https://ci.appveyor.com/project/Headline22/compiler/branch/master)

### Lin : [![Build status](https://ci.appveyor.com/api/projects/status/jmyjt6k511y0xqdy?svg=true)](https://ci.appveyor.com/project/Headline22/compiler-xoo5i)

### Mac : [![Build status](https://travis-ci.org/Headline/compiler.svg?branch=master)](https://travis-ci.org/Headline/compiler)

## Description
A basic compiler for a scripting language named Language X. This language is C-like, and is designed to be easy to learn for beginners. While it's functionality is currently limited, it will have the following properties.

- Not OOP, meaning classes and structs will never be supported
- Like this projects inspiriation, it is typeless. The only type is the 32-bit integer `int`
- This project will always be backwards compatable, meaning old scripts will never break

## Build Instructions
#### Dependencies
 - [AMBuild](https://github.com/alliedmodders/ambuild)
#### Instructions
Once AMBuild is installed on your system, compilation is easy. Compiler wise, clang, gcc, and msvc are all supported.
- cd to the compiler folder in this project
- mkdir build && cd build
- python ../configure.py (view configure.py for futher compilation options)
- ambuild

## Usage
Beauty is in the eye of the beholder and this project is no exception to that. While crude, this project's is intended to run *very* quickly, with performance and ease-of-use as it's first and second priorities. As development continues, more documentation will be created & guides will be released with instruction on how to embed the language into your use-case.

## Development
The first focus is on the design of the compiler, whose construction will pause when code generation is on the horizon. TaghaVM (this project's cousin), will be the compilation target. Tagha's goals align with that of this compiler, which is speed and a minimal footprint. 

This project will not be rushed and periods of stale development may occur. If you'd like to contribute to this compiler and help out you're more than welcome, but I request that you collaborate heavily with me or your pull requests may go stale or be declined (something I hate doing). 
