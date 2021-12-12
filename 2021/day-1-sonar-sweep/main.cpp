#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include "../common/readFile.h"

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
  std::vector<int> input = readFile("input.txt");

  partOne(input);
  partTwo(input);

  return 0;
}