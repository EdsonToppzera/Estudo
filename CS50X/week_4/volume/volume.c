// Modifies the volume of an audio file

#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

// Number of bytes in .wav header
const int HEADER_SIZE = 44;

int main(int argc, char *argv[])
{
    // Check command-line arguments
    if (argc != 4)
    {
        printf("Usage: ./volume input.wav output.wav factor\n");
        return 1;
    }

    // Open files and determine scaling factor
    FILE *input = fopen(argv[1], "r");
    if (input == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }

    FILE *output = fopen(argv[2], "w");
    if (output == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }

    float factor = atof(argv[3]);

    // Cria um array para armazenar os 44 bytes do cabeçalho
    uint8_t header[HEADER_SIZE];

    // Lê o cabeçalho do arquivo de entrada
    fread(header, HEADER_SIZE, 1, input);

    // Escreve o cabeçalho exatamente igual no arquivo de saída
    fwrite(header, HEADER_SIZE, 1, output);

    // Variável para armazenar uma única amostra de 2 bytes (16 bits)
    int16_t sample;

    // O loop continua enquanto houver amostras para ler (fread retorna 1)
    while (fread(&sample, sizeof(int16_t), 1, input))
    {
        // Modifica o volume multiplicando pelo fator
        sample = sample * factor;

        // Escreve a amostra modificada no arquivo de saída
        fwrite(&sample, sizeof(int16_t), 1, output);
    }

    // Close files
    fclose(input);
    fclose(output);
}
