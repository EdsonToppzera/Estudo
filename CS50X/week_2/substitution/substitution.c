#include <ctype.h>
#include <cs50.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

string cipher(string key, string text);
int main(int argc, string argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./substitution key\n");
        return 1;
    }

    string chave = argv[1];
    int qntsl = 0;
    int l = 0;

    while (chave[qntsl] != '\0')
    {
        qntsl++;
    }

    //if (argc < 2)
    //{
        //printf("Usage: ./substitution key");
        //return 1;
    //}
    if (qntsl != 26)
    {
        printf("Key must contain 26 characters.\n");
        return 1;
    }
    else
    {
        // tem nao letra??
        while (chave[l]!= '\0')
        {
            if (!isalpha(chave[l]))
            {
                printf("tem nao letra\n");
                return 1;
            }
            l++;
        }
        // tem duplicado??
        for (int h = 0; h<strlen(chave); h++)
        {
            for (int j=h+1;j<strlen(chave);j++)
            {
                if (toupper(chave[h])==toupper(chave[j]))
                {
                    printf("duplicadooo\n");
                    return 1;
                }
            }
        }


        string texto = get_string("plaintext: ");
        printf("ciphertext: %s\n",cipher(chave,texto));
        return 0;
    }
}

string cipher(string key,string text)
{
    string alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    string ciphertext = "";

    int i = 0;
    int y = 0;
    while (text[i] != '\0')
    {
        if (isalpha(text[i]))
        {
            while  (alphabet[y] != toupper(text[i]))
            {
                y++;
            }

            if (isupper(text[i]))
            {
                text[i] = toupper(key[y]);
            }
            else
            {
                text[i] = tolower(key[y]);
            }
        }
        y=0;
        i++;
    }
    ciphertext = text;
    return ciphertext;
}
