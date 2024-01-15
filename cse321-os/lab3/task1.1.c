#include <stdio.h>

typedef struct Paratha {
    int quantity;
    float unit_price;
} Paratha;

typedef struct Vegetable {
    int quantity;
    float unit_price;
} Vegetable;

typedef struct Water {
    int quantity;
    float unit_price;
} Water;

int main() {

    Paratha p;
    Vegetable v;
    Water w;
    int total_people;

    printf("Quantity of Paratha: ");
    scanf("%d", &p.quantity);
    printf("Unit price: ");
    scanf("%f", &p.unit_price);

    printf("Quantity of Vegetable: ");
    scanf("%d", &v.quantity);
    printf("Unit price: ");
    scanf("%f", &v.unit_price);

    printf("Quantity of Water: ");
    scanf("%d", &w.quantity);
    printf("Unit price: ");
    scanf("%f", &w.unit_price);

    printf("Number of people: ");
    scanf("%d", &total_people);

    float total_cost = 0;
    total_cost += p.quantity * p.unit_price;
    total_cost += v.quantity * v.unit_price;
    total_cost += w.quantity * w.unit_price;

    printf("Individual people will pay: %.2f tk\n", total_cost / total_people);

    return 0;
}
