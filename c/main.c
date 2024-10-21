
#include <stdio.h>
#include "memory.h"



int main(){
    //TODO Test with multiple memory blocks
    struct MemoryBlock block = createMemoryBlock(20);
    prepareMemoryBlock(block);
    memblocks = block;
    allocateMemory(1);
    allocateMemory(1);
    allocateMemory(1);
    freeMemory(3);
    freeMemory(11);
    freeMemory(7);
    printMemory();
    return 1;
}