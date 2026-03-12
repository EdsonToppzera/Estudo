#include <cs50.h>
#include <stdio.h>

int main(void)
{
    long number = get_long("Number: ");
    long reserva = number;
    int total = 0;
    int multiplicado = 0;
    int igual = 0;
    int i = 1;

    //printf("%ld\n",number);

    while (number > 0)
    {
        int digit = number % 10;
        // apagar
        //printf("%i\n",digit);

        i++;
        int partm1 = 0;
        int partm2 = 0;
        if (i%2 != 0)
        {
            multiplicado = digit * 2;
            igual = 0;
            if (multiplicado>9)
            {
                partm1=multiplicado/10;
                partm2=multiplicado%10;
                multiplicado = 0;
            }
        }
        else
        {
            multiplicado = 0;
            igual = digit;
        }
        total = total + multiplicado + partm1 + partm2 + igual;
        //apgar
        //printf("%i\n",total);

        number /= 10;
    }
    //printf("%i\n",i);
    if (total%10 == 0)
    {
        // visa/mastercard (16) length
        if (i == 17)
        {
            int start = reserva / 100000000000000;

            if (start >= 51 && start <= 55)
            {
                printf("MASTERCARD\n");
            }
            else if (start/10 == 4)
            {
                printf("VISA\n");
            }
            else
            {
                // modificar
                printf("INVALID\n");
            }
        }
        else if (i==14)
        {
            printf("VISA\n");
        }

        else if (i == 16)
        {
            int start = reserva / 10000000000000;

            if (start == 34||start == 37)
            {
                printf("AMEX\n");
            }
            else
            {
                // modificar
                printf("INVALID\n");
            }
        }
        else
        {
            printf("INVALID\n");
        }
        // apagar
        //printf("%i\n",start);
    }
    else
    {
        printf("INVALID\n");
    }
}
