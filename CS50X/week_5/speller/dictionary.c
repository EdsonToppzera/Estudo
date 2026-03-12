// Implements a dictionary's functionality
#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h> // Necessário para strcasecmp

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// Escolhendo um N grande o suficiente para espalhar bem as palavras e evitar listas longas
// 100000 é um número arbitrário, mas grande o suficiente para o dicionário do CS50
const unsigned int N = 100000;

// Hash table
node *table[N];

// Variável global para rastrear o tamanho do dicionário rapidamente
unsigned int word_count = 0;

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // 1. Descobre em qual "gaveta" (índice) a palavra deve estar
    unsigned int index = hash(word);

    // 2. Cria um ponteiro cursor para percorrer a lista encadeada daquela gaveta
    node *cursor = table[index];

    // 3. Percorre a lista até o fim (NULL)
    while (cursor != NULL)
    {
        // strcasecmp compara ignorando maiúsculas/minúsculas, como exigido
        if (strcasecmp(cursor->word, word) == 0)
        {
            return true; // Palavra encontrada!
        }
        cursor = cursor->next; // Move para o próximo nó
    }

    return false; // Chegou ao fim da lista e não encontrou
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // Uma função hash customizada simples, mas eficiente.
    // Ela soma os valores das letras com um deslocamento de bits para misturar os resultados.
    unsigned int hash_value = 0;

    for (int i = 0; word[i] != '\0'; i++)
    {
        // Converte para maiúscula para garantir que 'apple' e 'Apple' tenham o mesmo hash
        hash_value = (hash_value << 2) ^ toupper(word[i]);
    }

    // Retorna o valor garantindo que ele caiba dentro do tamanho do array N
    return hash_value % N;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // 1. Abre o arquivo do dicionário
    FILE *file = fopen(dictionary, "r");
    if (file == NULL)
    {
        return false;
    }

    char current_word[LENGTH + 1];

    // 2. Lê cada palavra do arquivo até chegar ao fim (EOF)
    while (fscanf(file, "%s", current_word) != EOF)
    {
        // 3. Aloca memória para um novo nó
        node *new_node = malloc(sizeof(node));
        if (new_node == NULL)
        {
            fclose(file);
            return false;
        }

        // 4. Copia a palavra lida para o novo nó
        strcpy(new_node->word, current_word);

        // 5. Descobre o índice usando a função hash
        unsigned int index = hash(current_word);

        // 6. Insere o nó no início da lista encadeada (Linked List)
        new_node->next = table[index];
        table[index] = new_node;

        // 7. Aumenta o contador de palavras
        word_count++;
    }

    // Fecha o arquivo após terminar
    fclose(file);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // Retorna a variável global que foi alimentada durante o load
    return word_count;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // Percorre todos os 'N' índices da tabela hash
    for (int i = 0; i < N; i++)
    {
        // Cursor aponta para o início da lista na gaveta atual
        node *cursor = table[i];

        // Libera cada nó da lista encadeada
        while (cursor != NULL)
        {
            node *tmp = cursor;       // Salva o nó atual
            cursor = cursor->next;    // Move o cursor para o próximo
            free(tmp);                // Libera a memória do nó salvo
        }
    }

    return true;
}
