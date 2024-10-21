#include <stdbool.h>

struct Chunk{
    bool free;
    int size;
    int next;
    int prev;
};

struct MemoryBlock{
    int size;
    int free;
    int* memory;
    int address;
    struct MemoryBlock *next;
    bool hasNext;
};

extern struct MemoryBlock memblocks;

struct MemoryBlock createMemoryBlock(int size);
void prepareMemoryBlock(struct MemoryBlock block);

int allocateBlockMemory(struct MemoryBlock block, int size);
int allocateMemory(int size);
void freeMemory(int chunkAddress);

void printMemory();