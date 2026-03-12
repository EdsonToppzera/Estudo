#include <cs50.h>
#include <stdio.h>

void piramide(int n);
int main(void)
{
    int tamanho;
    do
    {
        tamanho = get_int("Height: ");
    }
    while (tamanho<1 || tamanho>8);

    piramide(tamanho);
}

void piramide(int n)
    {
        for (int i = 0; i<n; i++)
        {
            for (int espaço=n; espaço>i+1; espaço--)
            {
                printf(" ");
            }
            int espaço = n;
            for (int esquerda=0; esquerda<=i; esquerda++)
            {
                printf("#");
            }
            int esquerda = 0;
            printf("  ");
            for (int direita=0; direita<=i; direita++)
            {
                printf("#");
            }
            int direita = 0;
            printf("\n");
        }
    }
