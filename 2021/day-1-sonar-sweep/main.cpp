#include <iostream>
#include <fstream>
#include <string>
#include <vector>

#include "../common/common.h"

std::vector<int> vecStringsToInts(std::vector<std::string> &input)
{
  std::vector<int> ints;
  std::transform(input.begin(), input.end(), std::back_inserter(ints), [](const std::string &str)
                 { return std::stoi(str); });
  return ints;
}

void partOne(std::vector<int>& input) {
  int increases = 0;
  int last;
  bool firstPass = true;

  for (int num : input) {

    if (firstPass) {
      last = num;
      firstPass = false;
      continue;
    }

    if (num > last) {
      increases++;
    }

    last = num;
  }

  std::cout << "Part One" << std::endl;
  std::cout << "Depth increases: " << increases << std::endl;
}

void partTwo(std::vector<int>& input) {
  const int offset = 3;
  int increases = 0;

  for (int i = offset; i < input.size(); i++) {
    if (input[i] > input[i - offset]) {
      increases++;
    }
  }

  std::cout << "Part Two" << std::endl;
  std::cout << "Depth increases: " << increases << std::endl;
}

int main()
{
  std::vector<std::string> input = Common::readFileLines("input.txt");
  std::vector<int> ints = vecStringsToInts(input);

  partOne(ints);
  partTwo(ints);

  return 0;
}