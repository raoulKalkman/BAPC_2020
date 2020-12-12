//
// Created by raoulkalkman on 12/12/2020.
//

#include <iostream>
#include <vector>

/*
 * find shortest distance in graph from starting to Delft (1)
 *
 * individual ticket:   shortest distance between 2 stations = price
 * group ticket:        2 stations + names of any number of people, g euro per person
 *      -> only allow 1 group ticket in total
 *
 *
 */

void addToList(size_t from, size_t to, const size_t &weight){



}


int main(){
    size_t stations, connections, members, cost;
    //gather information from first line
    std::cin >> stations >> connections >> members >> cost;

    std::cout << "stations: " << stations << "\nconnections: " << connections << "\nfamily members: " << members << "\ncost of group ticket: " << cost << "\n";

    std::vector<size_t> starting;
    starting.reserve(members);

    for(size_t i = 0; i < members; i++){
        std::cin >> starting[i];    //init all family member starting points
    }

    std::vector <std::vector <std::pair<size_t, size_t> > > adjacencyList;
    adjacencyList[0].reserve(stations);




    //get everything in an adjaceny list.
    for(size_t i = 0; i < stations; i++){
        bool unique = true;
        size_t from, to, weight;
        std::cin >> from >> to >> weight; //get input from line

        for (size_t i = 0; i < adjacencyList[from].size(); i++) {
            if (adjacencyList[from][i].first == to) {
                unique = false;
            }
        }

        if(unique){
            adjacencyList[from].push_back(std::pair<size_t, size_t>(to, weight));
        }

        unique = true;
        for(size_t i = 0; i < adjacencyList[to].size(); i++){
            if(adjacencyList[to][i].first == from){
                unique = false;
            }
        }

        if(unique){
            adjacencyList[to].push_back(std::pair<size_t, size_t>(from, weight)); // add to other list as well as weight should be symmetric
        }

    }

    {
        std::string ret = "Adjacency list:";

        for (size_t y = 0; y < adjacencyList.size(); y++) {
            ret += "\n\t[" + std::to_string(y + 1) + "]->";
            for (size_t x = 0; x < adjacencyList[y].size(); x++) {
                ret += "[" + std::to_string(adjacencyList[y][x].first + 1) + " | " +
                       std::to_string(adjacencyList[y][x].second) + "]->";
            }
//        ret += "\b\b";
        }
        ret += "\n";
        std::cout << ret;
    }

}

