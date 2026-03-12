#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

// Define o tipo BYTE para facilitar a leitura de blocos de 8 bits
typedef uint8_t BYTE;

int main(int argc, char *argv[])
{
    // 1. Verifica os argumentos da linha de comando
    if (argc != 2)
    {
        printf("Usage: ./recover IMAGE\n");
        return 1;
    }

    // 2. Tenta abrir a imagem forense
    FILE *raw_file = fopen(argv[1], "r");
    if (raw_file == NULL)
    {
        printf("Could not open %s\n", argv[1]);
        return 1;
    }

    // Variáveis auxiliares
    BYTE buffer[512];       // Buffer para ler um bloco por vez
    FILE *img = NULL;       // Ponteiro para o arquivo JPEG atual
    char filename[8];       // String para o nome: ###.jpg (7 chars + \0)
    int count = 0;          // Contador de imagens encontradas

    // 3. Lê blocos de 512 bytes até o fim do arquivo
    while (fread(buffer, 1, 512, raw_file) == 512)
    {
        // 4. Verifica se o bloco atual é o início de um novo JPEG
        // Assinatura: 0xff 0xd8 0xff e o quarto byte entre 0xe0 e 0xef
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            // Se já houver um JPEG aberto, fecha ele antes de começar o próximo
            if (img != NULL)
            {
                fclose(img);
            }

            // Gera o novo nome do arquivo (ex: 000.jpg, 001.jpg...)
            sprintf(filename, "%03i.jpg", count);
            img = fopen(filename, "w");
            count++;
        }

        // 5. Se houver um arquivo aberto, escreve o bloco de dados nele
        if (img != NULL)
        {
            fwrite(buffer, 1, 512, img);
        }
    }

    // 6. Limpeza final: fecha todos os arquivos abertos
    if (img != NULL)
    {
        fclose(img);
    }
    fclose(raw_file);

    return 0;
}
