#include <iostream>
#include <fstream>
#include <filesystem>
#include <vector>
namespace fs = std::filesystem;

#define debug = true

// Has to have /home/dylan/
std::string books_path = "/home/dylan/Documents/Books";
const std::string path_save = "/home/dylan/Documents/_Code/C++/Book_Manager/path.txt";
std::string path;

// This updates the stored Books path
void update_books_path(std::string new_path = "/home/dylan/Documents/Books"){
  books_path = new_path;

  std::ofstream file;
  file.open(path_save);

  if(file.is_open()){
    file << new_path;
    file.close();
  }

  else{
    std::cout << "File failed to open!";
  }
}

void change_dir(std::string s){
  std::string new_path = path + "/" + s;
  
  #ifdef debug:
    std::cout << new_path;
  #endif

  if(fs::exists(new_path) && fs::is_directory(new_path)){
    path = new_path;
  }
  else{
    std::cout << "That is not a valid path";
  }  
}

void init(){
  update_books_path("/home/dylan/Documents/Books");
  path = books_path;
}

// This prints out all of the files in the books directory
void print_files(){
  #ifdef debug
    std::cout << path << "\n";
  #endif

  if(fs::exists(path)){
    if(fs::is_directory(path)){
      for(const auto& entry : fs::directory_iterator(path)){
        std::cout << entry.path().filename().string() << "\n";
      }
    }
    else{
      std::cout << "That is not a directory!";
    }
  }
  else{
    std::cout << "That path doesn't exist!";
  }
}

std::vector<std::string> new_cmd(std::string input){
  std::vector<std::string> temp;
  std::string word = "";

  for(int i = 0; i < input.length() - 1; i++){
    if(input[i] != ' '){
     word = word + input[i];
    }
    else{
      temp.push_back(word);
      word = "";
    }
  }

  int j = (int)temp.size() - 1;
  std::cout << j;
  for(int i = 0; i < j; i++){
    std::cout << temp[i] << "\n";
  }

  return temp;
}

void process_input(std::string input){
  
  std::vector<std::string> t = new_cmd(input); 
}

void input_loop(){
  while(true){
    std::string input = "";
    std::cout << ">> ";
    std::cin >> input;

    process_input(input);
  }
}

int main(){ 

  init();
  
  
  // print_files();
  // change_dir("Skibidi");

  input_loop();

  return 0;
} 