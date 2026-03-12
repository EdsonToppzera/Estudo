#include <cs50.h>
#include <stdio.h>
#include <ctype.h>

int totalp(string p);
//int letras1 = {'A','E','I','L','N','O','R','S','T','U'};

int main(void)
{
    string p1 = get_string("Player 1: ");
    string p2 = get_string("Player 2: ");

    if (totalp(p1)>totalp(p2))
    {
        printf("Player 1 wins!\n");
    }
    else if (totalp(p2)>totalp(p1))
    {
        printf("Player 2 wins!\n");
    }
    else
    {
        printf("Tie!\n");
    }
}

int totalp(string p)
{
    int i = 0;
    int sum = 0;
    while (p[i] != '\0')
    {
        if (toupper(p[i])=='A' || toupper(p[i])=='E' || toupper(p[i])=='I' || toupper(p[i])=='L' || toupper(p[i])=='N' || toupper(p[i])=='O' || toupper(p[i])=='R' || toupper(p[i])=='S' || toupper(p[i])=='T' || toupper(p[i])=='U')
        {
            sum+=1;
        }
        else if (toupper(p[i])=='D' || toupper(p[i])=='G')
        {
            sum+=2;
        }
        else if (toupper(p[i])=='B' || toupper(p[i])=='C' || toupper(p[i])=='M' || toupper(p[i])=='P')
        {
            sum+=3;
        }
        else if (toupper(p[i])=='F' || toupper(p[i])=='V' || toupper(p[i])=='W' || toupper(p[i])=='Y')
        {
            sum+=4;
        }
        else if (toupper(p[i])=='K')
        {
            sum+=5;
        }
        else if (toupper(p[i])=='J' || toupper(p[i])=='X')
        {
            sum+=8;
        }
        else if (toupper(p[i])=='Q' || toupper(p[i])=='Z')
        {
            sum+=10;
        }
        else
        {
            sum+=0;
        }

        i++;
    }
    return sum;
}
