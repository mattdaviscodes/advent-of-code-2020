#include <iostream>
#include <fstream>
#include <string>
#include <vector>

#include "../common/common.h"

void partOne(std::vector<int>& input) {
  std::cout << "Part One" << std::endl;
}

void partTwo(std::vector<int>& input) {
  std::cout << "Part Two" << std::endl;
}

int main()
{
  std::vector<std::string> input = Common::readFileLines("input.txt");

  partOne(input);
  partTwo(input);

  return 0;
}