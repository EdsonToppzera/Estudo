#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Max number of candidates
#define MAX 9

// Candidates have name and vote count
typedef struct
{
    string name;
    int votes;
} candidate;

// Array of candidates
candidate candidates[MAX];

// Number of candidates
int candidate_count;

// Function prototypes
bool vote(string name);
void print_winner(void);

int main(int argc, string argv[])
{
    // Check for invalid usage
    if (argc < 2)
    {
        printf("Usage: plurality [candidate ...]\n");
        return 1;
    }

    // Populate array of candidates
    candidate_count = argc - 1;
    if (candidate_count > MAX)
    {
        printf("Maximum number of candidates is %i\n", MAX);
        return 2;
    }
    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i].name = argv[i + 1];
        candidates[i].votes = 0;
    }

    int voter_count = get_int("Number of voters: ");

    // Loop over all voters
    for (int i = 0; i < voter_count; i++)
    {
        string name = get_string("Vote: ");

        // Check for invalid vote
        if (!vote(name))
        {
            printf("Invalid vote.\n");
        }
    }

    // Display winner of election
    print_winner();
}

// Update vote totals given a new vote
bool vote(string name)
{
    // TODO
    int td_certo = 1;
    for (int y=0;y<candidate_count;y++)
    {
        if (strcmp(name, candidates[y].name)==0)
        {
            candidates[y].votes++;
            td_certo = 0;
        }
    }

    if (td_certo == 1)
    {
        return false;
    }
    else
    {
        return true;
    }
}

// Print the winner (or winners) of the election
void print_winner(void)
{
    // TODO
    string winner = candidates[0].name;
    int winnerv = candidates[0].votes;

    for (int j=0;j<candidate_count-1;j++)
    {
        if (winnerv<candidates[j+1].votes)
        {
            winner = candidates[j+1].name;
            winnerv = candidates[j+1].votes;
        }
    }
    printf("%s\n",winner);
    for (int k=0;k<candidate_count;k++)
    {
        if (winnerv==candidates[k].votes)
        {
            if (strcmp(winner, candidates[k].name) != 0)
            {
                printf("%s\n",candidates[k].name);
            }
        }
    }
    return;
}
