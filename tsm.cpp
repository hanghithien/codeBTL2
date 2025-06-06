#include <fstream>
#include <iostream>
#include <map>
#include <sstream>
#include <stdexcept>
#include <string>
#include <vector>
#include<algorithm>
#include<cmath>
using namespace std;

// You can add your helper functions here
int get_mapped_index(char ch, char v[26], char v_cre[26], int num_vertices) {
    for (int i = 0; i < num_vertices; i++) {
        if (ch == v[i]) return i; 
    }
    return -1; // Không tìm thấy
}
int find_num_vertices(int edge[][3], int numberOfEdges, char v[26], char v_cre[26]) {
    int ascii[256];
    for(int i=0;i<256;i++) {
        ascii[i] = -1;
    }
    int num_vertices = 0;
    for (int i = 0; i < numberOfEdges; i++) {
        int x = edge[i][0];
        int y = edge[i][1];
        ascii[x] = x;
        ascii[y] = y;
    }
    for (int i = 0; i < 256; i++) {
        if (ascii[i] != -1) {
            v[num_vertices] = (char)i;
            num_vertices++;
        }
    }
    for (int i = 0; i < num_vertices; i++) {
        v_cre[i] = 'A'+i;
    }
    // Không thay đổi edge ở đây, để giữ nguyên danh sách cạnh gốc
    return num_vertices;
}
void Traveling(int edge[][3], int numberOfEdges, char startVertex){
    // Your code here
    char v[26];
    char v_cre[26];
    int num_vertices = find_num_vertices(edge, numberOfEdges, v, v_cre);

    int G[30][30];
    for (int i = 0; i < num_vertices; i++) {
        for (int j = 0; j < num_vertices; j++) {
            G[i][j] = 0;
        }
    }
    // Ánh xạ cạnh vào ma trận G
    for (int i = 0; i < numberOfEdges; i++) {
        int u = get_mapped_index(edge[i][0], v, v_cre, num_vertices);
        int v_idx = get_mapped_index(edge[i][1], v, v_cre, num_vertices);
        if (u >= 0 && u < num_vertices && v_idx >= 0 && v_idx < num_vertices) {
            G[u][v_idx] = edge[i][2];
        }
    }

    int start_in = get_mapped_index(startVertex, v, v_cre, num_vertices);
    if (start_in < 0 || start_in >= num_vertices) {
        return;
    }
    vector<vector<int>> X(1<<num_vertices, vector<int>(num_vertices, -1));
    vector<vector<int>> Y(1<<num_vertices, vector<int>(num_vertices, -1));
    Y[1<<start_in][start_in] = 0;
    for(int i=0;i<num_vertices;i++) {
        if(G[start_in][i] != 0 && i != start_in) {
            Y[1<<i][i] = G[start_in][i];
            X[1<<i][i] = i;
        }
    }
    for(int i=1;i<(1<<num_vertices);i++) {
        for(int j=0;j<num_vertices;j++) {
            if((i & (1<<j)) && !(i & (1<<start_in)) && j!=start_in)  {
                for(int k=0;k<num_vertices;k++) {
                    if(k != j && G[k][j] != 0 && (i & (1<<k)) && k != start_in) {
                        int pre_i = i^(1<<j);
                        if(Y[pre_i][j] !=-1) {
                            int new_distance = Y[pre_i][k] + G[k][j];
                            if((Y[pre_i][k] + G[k][j]) < Y[i][j] || Y[i][j] == -1) {
                                Y[i][j] = new_distance;
                                X[i][j] = k;
                            }
                        }
                    }
                }
            }

        }
    }
    int min_distance = INT_MAX;
    int final_i = ((1<<num_vertices)-1)^(1<<start_in);
    int pre_in = -1;
    for(int j=0;j<num_vertices;j++) {
        if(j!=start_in && Y[final_i][j] != -1 && G[j][start_in] != 0 ) {
            int new_dist = Y[final_i][j] + G[j][start_in];
            if(new_dist<min_distance) {
                min_distance = new_dist;
                pre_in = j;
            }
        }
    }
    if(min_distance == INT_MAX) return;
    vector<char> temp;
    temp.push_back(v[pre_in]);
    int current_i = final_i;
    int current_j = pre_in;
    while(current_i != 0) {
        int pre_j = X[current_i][current_j];
        temp.push_back(v[pre_j]);
        current_i = current_i^(1<<current_j);
        current_j = pre_j;
    }
    string str;
    for(int i=temp.size()-1;i>=0;i--) {
        str+=temp[i]+" ";
    }
    str+=v[start_in];
    cout << str;
}

int computePathCost(int** matrix, int numCities, const char* vertex, const std::string& path) {
        if (path.empty()) {
            return -1; // No path provided
        }
        std::map<char, int> vertexIndex;
        for (int i = 0; i < numCities; ++i) {
            vertexIndex[vertex[i]] = i;
        }

        std::vector<int> pathIndices;
        std::istringstream iss(path);
        std::string token;
        while (iss >> token) {
            char v = token[0];
            if (vertexIndex.find(v) == vertexIndex.end()) {
                return -2;
            }
            pathIndices.push_back(vertexIndex[v]);
        }

        int totalCost = 0;
        for (size_t i = 0; i + 1 < pathIndices.size(); ++i) {
            int from = pathIndices[i];
            int to = pathIndices[i + 1];
            totalCost += matrix[from][to];
        }

        return totalCost;
    }

int main(){
    string name = "tsm01";
    stringstream output;

    //! ---- DATA --------
    int numCities = 5;
    int matrix[5][5] = {
        {0, 9, 92, 61, 11},
        {41, 0, 99, 44, 78},
        {75, 42, 0, 79, 12},
        {86, 78, 24, 0, 15},
        {86, 62, 1, 9, 0}
    };
    char vertex[5] = {'A', 'C', 'F', 'I', 'H'};

    char startVertex = 'A';

    // Convert to edge list
    int edge[25][3];
    int numberOfEdges = 0;
    for (int i = 0; i < numCities; i++)
    {
        for (int j = 0; j < numCities; j++)
        {
            if (matrix[i][j] > 0)
            {
                edge[numberOfEdges][0] = vertex[i];
                edge[numberOfEdges][1] = vertex[j];
                edge[numberOfEdges][2] = matrix[i][j];
                numberOfEdges++;
            }
        }
    }

    //! ---- PROCESS --------

    Traveling(edge, numberOfEdges, startVertex);
    std::streambuf* oldCoutBuffer = std::cout.rdbuf();
    std::cout.rdbuf(output.rdbuf());
    Traveling(edge, numberOfEdges, startVertex);
    std::cout.rdbuf(oldCoutBuffer);

    int* matrixToCal[5];
    for (int i = 0; i < numCities; ++i) matrixToCal[i] = matrix[i];

    int path_len = computePathCost(matrixToCal, numCities, vertex, output.str());

    string output_len = "The best path length is: ";
        output_len += (127 * 0.95 < path_len && path_len < 127 * 1.05 ? "127" :to_string(path_len));

    //! ---- EXPECT --------
    string expect = "The best path length is: 127";
    cout << output.str();

}