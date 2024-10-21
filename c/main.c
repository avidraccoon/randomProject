
#include <stdio.h>
#include "memory.h"

int main(){
    struct MemoryBlock block = createMemoryBlock(20);
    prepareMemoryBlock(block);
    memblocks = block;
    int address = allocateMemory(5);
    int address2 = allocateMemory(5);
    printf("%d %d\n", address, address2);
    //freeMemory(address);
    //allocateMemory(2);
    printMemory();
    return 1;
}