#include "Sonar.h"

Sonar::Sonar(std::vector<int> &depths) : depths(depths) {}

int Sonar::getDepthIncreases(unsigned int range)
{
    int increases = 0;

    for (int i = range; i < depths.size(); i++)
    {
        if (depths[i] > depths[i - range])
        {
            increases++;
        }
    }

    return increases;
}