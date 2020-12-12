//
// Created by raoulkalkman on 12/12/2020.
//

#include <iostream>
#include <cstddef>
#include <cmath>

int main(){
    //calculate dimensions of surface area

    size_t corner, edge, center;

    std::cin >> corner >> edge >> center;

    if(corner == 0 && edge == 0 && center == 0){
        std::cout << "0 0";
    }

    if(corner != 4){
        std::cout << "impossible";
    }

    if(edge % 2 != 0){
        std::cout << "impossible";
    }

    //we have 4 corners and an even amount of edges
    size_t sumSideLength = edge / static_cast<int>(2);

    for(size_t i = 0; i <= sumSideLength - i; i++){
        size_t x = i;
        size_t y = sumSideLength - i;
//        std::cout << "trying index " << i << " where x axis is " << x << " and y is " << y << "\n";
//        std::cout << "This should thus have " << x * y << " center pieces!\n";

        if(x * y == center){
            std::cout << x*2 << " " << y*2;
            exit(0);
        }
    }

    std::cout << "impossible";
    exit(0);
}