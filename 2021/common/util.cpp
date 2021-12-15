#include <iostream>
#include <vector>
#include <fstream>

#include "util.h"

std::vector<std::string> Util::readFileLines(const std::string &filename)
{
    std::vector<std::string> v;
    std::string line;
    std::ifstream in(filename);

    if (!in)
    {
        std::cerr << "Cannot open the File : " << filename << std::endl;
        return v;
    }

    while (std::getline(in, line)) {
        if (line.size() > 0) {
            v.push_back(line);
        }
    }

    in.close();
    return v;
}