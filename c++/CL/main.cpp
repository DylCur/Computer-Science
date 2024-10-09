#include <iostream>
#include <filesystem>
#include <sstream>
#include <vector>
#include <unistd.h> 


std::string path = "~/";


std::vector<std::string> splitString(const std::string& str) {
  std::vector<std::string> result;
  std::istringstream stream(str);
  std::string word;
  
  while (stream >> word) {
      result.push_back(word);
  }

  return result;
}

void invalid(){
  std::cout << "Invalid Parameters";
}

void cd(std::vector<std::string>& cmd){
  
  const char* path = cmd[1].c_str();
  
  if(cmd.size() != 2){
    invalid();
  }

  else{
    if(chdir(path) != 0){
      perror("chdir");
    }
  }

  

}

void translateCommand(std::vector<std::string>& cmd){
  // 0 will be the command and all the others will be parameters

  if(cmd[0] == "cd"){
    cd(cmd);
  }
}

void commands(){

}

int main(){
  
  return 0;
}