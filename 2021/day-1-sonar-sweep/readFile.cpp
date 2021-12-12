#include <vector>
#include <string>
#include <fstream>
#include "readFile.h"

std::vector<int> readFile(const std::string& filename) {
  std::fstream file;
  std::vector<int> v;

  file.open(filename, std::ios::in);

  if (file.is_open()) {

    int a;

    while (file >> a) {
      v.push_back(a);
    }

    file.close();
  };

  return v;
}