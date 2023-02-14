#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct vector {
    void **items;
    int capacity;
    int total;
} vector;

void vector_init(vector *v) {
    v->capacity = 1; //VECTOR_INIT_CAPACITY;
    v->total = 0;
    v->items = malloc(sizeof(void *) * v->capacity);
}

void vector_add(vector *v, void *item) {
    v->total += 1;
    if (v->capacity == v->total) {
        printf("%s", (char*)item); // casting item to char
        // printf("%i", v->capacity);
    }

}

int main(void) {
    vector v;
    vector_init(&v);
    // printf("%i", v.total);
    vector_add(&v, "aonjour");
}
