#ifndef SONAR_ADVENT_2021_
#define SONAR_ADVENT_2021_

#include <vector>

class Sonar
{
private:
    std::vector<int> depths;

public:
    Sonar();
    Sonar(std::vector<int> &depths);

    int getDepthIncreases(unsigned int range = 1);
};

#endif