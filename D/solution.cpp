//
// Created by raoulkalkman on 12/12/2020.
//

#include <iostream>
#include <stdexcept>
#include <vector>
#include <string>

enum answer = {SKY, SEA, HORIZON};

int main(){
    answer answer; //init enum
    size_t width, height;

    std::cin >> width >> height;

    std::vector<std::vector<size_t> > image;

    image.reserve(width);

    for(size_t i = 0; i < width; i++){
        image[i].reserve(height);
    }

    // do a binary search in column 1 to find where approximately horizon is
    // from this point look at y, y -1, y+1, y-2, y+2,... until next horizon approximation is found
    // do this until we find a horizon pixel
    // save horizon pixel, go on

    std::string answer;
    size_t req = height/2;
    std::cout << "? " << 0 << " " << req;
    std::cout.flush();
    std::cin >> answer;

    switch (answer) {
        case SKY:

            break;
        case SEA:

            break;
        case HORIZON:

            break;
    }



    std::cout << "? x y"; //where x is column of pixel, y is row returns "sky", "sea", "horizon" (return in std::cin)
    std::cout.flush();

    std::cout << "! x1 y1 x2 y2"; //solution with our coordinates
    std::cout.flush();

}