
#include <bits/stdc++.h>
using namespace std;

// number of total nodes
#define N 20
#define INF INT_MAX
#include <ctime>
class Node
{
public:
    vector<pair<int, int>> path;
    int matrix_reduced[N][N];
    int cost;
    int vertex;
    int level;
};

Node* newNode(int matrix_parent[N][N], vector<pair<int, int>> const &path,int level, int i, int j)
{
    Node* node = new Node;
    node->path = path;
    if (level != 0)
        node->path.push_back(make_pair(i, j));
    memcpy(node->matrix_reduced, matrix_parent,
        sizeof node->matrix_reduced);
    for (int k = 0; level != 0 && k < N; k++)
    {
        node->matrix_reduced[i][k] = INF;
        node->matrix_reduced[k][j] = INF;
    }

    node->matrix_reduced[j][0] = INF;
    node->level = level;
    node->vertex = j;
    return node;
}

void reduce_row(int matrix_reduced[N][N], int row[N])
{
    fill_n(row, N, INF);

    for (int i = 0; i < N; i++)
        for (int j = 0; j < N; j++)
            if (matrix_reduced[i][j] < row[i])
                row[i] = matrix_reduced[i][j];

    for (int i = 0; i < N; i++)
        for (int j = 0; j < N; j++)
            if (matrix_reduced[i][j] != INF && row[i] != INF)
                matrix_reduced[i][j] -= row[i];
}

void reduce_column(int matrix_reduced[N][N], int col[N])
{
    fill_n(col, N, INF);

    for (int i = 0; i < N; i++)
        for (int j = 0; j < N; j++)
            if (matrix_reduced[i][j] < col[j])
                col[j] = matrix_reduced[i][j];

    for (int i = 0; i < N; i++)
        for (int j = 0; j < N; j++)
            if (matrix_reduced[i][j] != INF && col[j] != INF)
                matrix_reduced[i][j] -= col[j];
}

int cost_calculation(int matrix_reduced[N][N])
{
    int cost = 0;

    int row[N];
    reduce_row(matrix_reduced, row);

    int col[N];
    reduce_column(matrix_reduced, col);

    for (int i = 0; i < N; i++)
        cost += (row[i] != INT_MAX) ? row[i] : 0,
            cost += (col[i] != INT_MAX) ? col[i] : 0;

    return cost;
}

void printPath(vector<pair<int, int>> const &list)
{
    for (int i = 0; i < list.size(); i++)
        cout << list[i].first + 1 << " -> "
             << list[i].second + 1 << endl;
}

class comp {
public:
    bool operator()(const Node* lhs, const Node* rhs) const
    {
        return lhs->cost > rhs->cost;
    }
};

int solve(float adjacensyMatrix[N][N])
{
    priority_queue<Node*, std::vector<Node*>, comp> pq;
    vector<pair<int, int>> v;
    Node* root = newNode(adjacensyMatrix, v, 0, -1, 0);
    root->cost = cost_calculation(root->matrix_reduced);
    pq.push(root);
    while (!pq.empty())
    {
        Node* min = pq.top();
        pq.pop();
        int i = min->vertex;
        if (min->level == N - 1)
        {
            min->path.push_back(make_pair(i, 0));
            printPath(min->path);
            return min->cost;
        }

        for (int j = 0; j < N; j++)
        {
            if (min->matrix_reduced[i][j] != INF)
            {
                Node* child = newNode(min->matrix_reduced, min->path,
                    min->level + 1, i, j);

                child->cost = min->cost + min->matrix_reduced[i][j]
                            + cost_calculation(child->matrix_reduced);

                pq.push(child);
            }
        }

        delete min;
    }
}

int main()
{
    
    
    float adjacensyMatrix[N][N] ={
        {INF,51664,28225,51644,59475,42589,60563,59690,43885,71165,45310,58806,53229,44440,48368,65707,46959,52892,53497,52297},
{51664,INF,41528,62480,35068,45597,52894,32558,66907,72558,42739,55050,49045,43127,70308,39443,33078,34069,55345,44712},
{28225,41528,INF,44589,60949,56050,47567,37122,40664,53108,56227,63480,52674,46219,51477,43069,40368,59410,38066,61281},
{51644,62480,44589,INF,50567,18717,67584,61561,56610,45388,55574,48280,60441,63321,59713,61844,59809,42371,66726,51282},
{59475,35068,60949,50567,INF,47556,53449,30655,63250,66400,37922,56592,46677,52249,33349,43813,46538,55143,46348,27059},
{42589,45597,56050,18717,47556,INF,50465,58529,65602,43718,54639,38491,50915,51679,53536,73623,52212,51032,65091,64307},
{60563,52894,47567,67584,53449,50465,INF,51844,35207,59772,47126,55171,54588,56765,76673,59655,41720,69333,65723,52091},
{59690,32558,37122,61561,30655,58529,51844,INF,49778,62367,43860,36136,32116,40083,62327,45672,56087,42259,57155,61991},
{43885,66907,40664,56610,63250,65602,35207,49778,INF,56528,53199,50855,29212,68142,43090,48695,58187,54966,48191,59694},
{71165,72558,53108,45388,66400,43718,59772,62367,56528,INF,40543,45068,50305,54725,59652,56875,53106,62078,65376,34588},
{45310,42739,56227,55574,37922,54639,47126,43860,53199,40543,INF,44433,50262,51642,48943,61610,54523,37419,65384,50689},
{58806,55050,63480,48280,56592,38491,55171,36136,50855,45068,44433,INF,51053,61654,52710,36211,50865,34018,44383,48850},
{53229,49045,52674,60441,46677,50915,54588,32116,29212,50305,50262,51053,INF,64386,42468,62264,62343,41737,49730,50999},
{44440,43127,46219,63321,52249,51679,56765,40083,68142,54725,51642,61654,64386,INF,51642,59356,57383,68662,40214,36268},
{48368,70308,51477,59713,33349,53536,76673,62327,43090,59652,48943,52710,42468,51642,INF,38906,55196,48223,52015,50881},
{65707,39443,43069,61844,43813,73623,59655,45672,48695,56875,61610,36211,62264,59356,38906,INF,53625,60372,42547,47228},
{46959,33078,40368,59809,46538,52212,41720,56087,58187,53106,54523,50865,62343,57383,55196,53625,INF,54841,62251,50797},
{52892,34069,59410,42371,55143,51032,69333,42259,54966,62078,37419,34018,41737,68662,48223,60372,54841,INF,54041,52413},
{53497,55345,38066,66726,46348,65091,65723,57155,48191,65376,65384,44383,49730,40214,52015,42547,62251,54041,INF,65319},
{52297,44712,61281,51282,27059,64307,52091,61991,59694,34588,50689,48850,50999,36268,50881,47228,50797,52413,65319,INF}
};
time_t start, end;
     double cpu_time_used;
     start = time(NULL);
     cout<<("Running...");
    cout << "\nCost is " << solve(adjacensyMatrix);
    cout<<("Finished");
    end = time(NULL);
     cpu_time_used = ((double) (end - start)) ;
     cout<<("fun() took %f seconds to execute \n", cpu_time_used);
    return 0;
}