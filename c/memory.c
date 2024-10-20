
#include "memory.h"
#include <stdio.h>
#include <stdlib.h>

struct MemoryBlock createMemoryBlock(int size){
    struct MemoryBlock block;
    block.size = size;
    block.free = size;
    block.address = 0;
    block.memory = (int *) malloc (size * sizeof(int));
    block.hasNext = false;
    return block;
}

struct MemoryBlock memblocks;

struct MemoryBlock getBlock(int address){
    struct MemoryBlock block = memblocks;
    while (address<block.address || address > block.address+block.size){
        if (block.hasNext){
            block = *block.next;
        }else{
            printf("Memory address not managed");
            return;
        }
    }
    return block;
}

struct Chunk getChunk(struct MemoryBlock block, int address){
    struct Chunk chunk;
    chunk.free = (block.memory[address-block.address] >= 0);
    chunk.size = abs(block.memory[address-block.address]);
    chunk.next = block.memory[address+1-block.address];
    chunk.prev = block.memory[address+2-block.address];
    return chunk;
}

void prepareMemoryBlock(struct MemoryBlock block){
    if (block.size<3){
        printf("To little memory to prepare block\n");
    }
    block.memory[0] = block.size - 3;
    block.memory[1] = -1;
    block.memory[2] = -1;
}



void handleAllocateChunk(struct MemoryBlock block, int address, int size, int previous){
    struct Chunk chunk = getChunk(block, address);
    int remainingSpace = chunk.size - size;
    if (remainingSpace<3){
        size = chunk.size;
        remainingSpace = -1;
    }
    block.memory[address] = -size;
    if (remainingSpace > 2){
        int newAddress = address+3+size;
        block.memory[newAddress-block.address] = remainingSpace - 3;
        block.memory[newAddress+1-block.address] = chunk.next;
        block.memory[newAddress+2-block.address] = address;
        if (chunk.prev >= 0){
            block.memory[chunk.prev+1-block.address] = newAddress;
        }
        block.memory[previous+1-block.address] = newAddress;
    }else{
        if (chunk.prev >= 0){
            block.memory[chunk.prev+1-block.address] = chunk.next;
        }
        block.memory[previous+1-block.address] = chunk.next;
    }
}

int allocateBlockMemory(struct MemoryBlock block, int size){
    if (block.free<3+size){
        printf("to little memory to allocate block\n");
        return -1;
    }
    int previous = block.address;
    int address = block.address;
    struct Chunk currentChunk = getChunk(block, address);
    while (currentChunk.size<size || !currentChunk.free){
        if (currentChunk.next == -1){
            printf("no chunk found\n");
            return -1;
        }
        previous = address;
        address = currentChunk.next;
        currentChunk = getChunk(block, address);
    }
    handleAllocateChunk(block, address, size, previous);
    return address;
}

int allocateMemory(int size){
    struct MemoryBlock memblock = memblocks;
    int address = allocateBlockMemory(memblock, size);
    while (address == -1){
        if (memblock.hasNext){
            memblock = *memblock.next;
        }else{
            printf("No suitable block\n");
            return -1;
        }
        address = allocateBlockMemory(memblock, size);
    }
    return address+3;
}

void mergeChunkNext(struct MemoryBlock block, struct Chunk chunk, int address){
    struct Chunk nextChunk = getChunk(block, address+chunk.size+3);
    if (nextChunk.free){
        int nextAddress = address+chunk.size+3-block.address;
        block.memory[address-block.address] = (chunk.size + nextChunk.size+3);
        block.memory[address-block.address+1] = block.memory[nextAddress+1];
        block.memory[nextAddress+nextChunk.size+3+2] = address;
    }
}

int mergeChunkPrev(struct MemoryBlock block, struct Chunk chunk, int address){
    struct Chunk prevChunk = getChunk(block, chunk.prev);
    if (prevChunk.free){
        block.memory[chunk.prev-block.address] = chunk.size + prevChunk.size+3;
        return chunk.prev;
    }
    return address;
}


void freeChunk(struct MemoryBlock block, struct Chunk chunk, int address){
    block.memory[address-block.address] = chunk.size;
    mergeChunkNext(block, chunk, address);
    chunk = getChunk(block, address);
    int chunkAddress = mergeChunkPrev(block, chunk, address);
    int previous = -1;
    int curAddress = block.address;
    struct Chunk curChunk = getChunk(block, block.address);
    struct Chunk nextChunk = getChunk(block, block.address+curChunk.size);
    while (curAddress<chunkAddress){
        previous = curAddress;
        curAddress = nextChunk.next;
        curChunk = nextChunk;
        nextChunk = getChunk(block, curAddress+curChunk.size);
        if (curAddress == -1){
            break;
        }
        if (previous == curAddress){
            break;
        }
    }
    if (previous>=0){
        block.memory[previous-block.address+1] = chunkAddress;
    }
}

void freeMemory(int chunkAddress){
    struct MemoryBlock block = getBlock(chunkAddress);
    struct Chunk chunk = getChunk(block, chunkAddress-3);
    freeChunk(block, chunk, chunkAddress-3);
}











void printMemory(){
    char mem[memblocks.size+1];
    mem[memblocks.size] = '\0';
    char status = '-';
    int counter = 0;
    for (int i = 0; i<memblocks.size; i++){
        if (counter == 0){
            struct Chunk chunk = getChunk(memblocks, i);
            if (chunk.free){
                status = '-';
            }
            else{
                status = '#';
            }
            counter = chunk.size + 3;
            printf("%d %d %d %d %d\n", i, chunk.free, chunk.size, chunk.next, chunk.prev);
            
        }
        mem[i] = status;
        counter--;
    }
    printf(mem);
    printf("\n");
}