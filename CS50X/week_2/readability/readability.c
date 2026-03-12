#include <ctype.h>
#include <cs50.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int grade(string t);

int main(void)
{
    string texto = get_string("Text: ");
    if (grade(texto)>16)
    {
        printf("Grade 16+\n");
    }
    else if (grade(texto)<1)
    {
        printf("Before Grade 1\n");
    }
    else
    {
        printf("Grade %i\n",grade(texto));
    }
}

int grade(string t)
{
    float letras = 0;
    float palavras = 1;
    float sent = 0;

    int i = 0;
    while (t[i] != '\0')
    {
        if (t[i] != '.' && t[i] != '!' && t[i] != '?' && t[i] != ',' && t[i] != ' ' && t[i] != '\'')
        {
            letras++;
        }
        if (t[i] == ' ')
        {
            palavras++;
        }
        if (t[i] == '.' || t[i] == '!' || t[i] == '?')
        {
            sent++;
        }

        i++;
    }

    float l = (letras/palavras)*100;
    float s = (sent/palavras)*100;
    float grade = 0.0588 * l - 0.296 * s - 15.8;
    ///
    //printf("letras: %f\n",letras);
    //printf("palavras: %f\n",palavras);
    //printf("sent: %f\n",sent);
    //printf("l: %f\n",l);
    //printf("s: %f\n",s);
    //printf("grade: %f\n",grade);
    ///
    return round(grade);
}
