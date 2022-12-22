#include <fstream>
#include <iostream>
#include <string>
#include <vector>

int main() {
    std::ifstream file("example.txt");
    std::string line;
    std::vector <std::string> lines;
    while (std::getline(file, line)) {
        lines.push_back(line);
    }

    // get all the valves
    std::vector <std::string> valves;
    for (int i = 0; i < lines.size(); i++) {
        valves.push_back(lines[i].substr(6, 2));
    }

    // get all the flow rates
    std::vector <std::string> flow_rates;
    for (int i = 0; i < lines.size(); i++) {
        flow_rates.push_back(lines[i].substr(lines[i].find('=') + 1, lines[i].find(';') - lines[i].find('=') - 1));
    }

    /*
     * Parse this
     *
     * Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
    Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II

        * into this
        * DD, II, BB
        * CC, AA
        * DD, BB
        * CC, AA, EE
        * etc..
     * */


    std::vector <std::vector<std::string>> values;
    for (int i = 0; i < lines.size(); i++) {
        std::vector <std::string> temp;
        std::string tunnels;
        if (lines[i].find("lead to values") != std::string::npos) {
            tunnels = lines[i].substr(lines[i].find("lead to valves") + (size_t) 2);
        } else {
            tunnels = lines[i].substr(lines[i].find("lead to valve") + 13,
                                                  lines[i].find(';') - lines[i].find("lead to valve") - 13);
        }
        std::cout << tunnels << std::endl;
    }

    // print values
    for (int i = 0; i < values.size(); i++) {
        for (int j = 0; j < values[i].size(); j++) {
            std::cout << values[i][j] << " ";
        }
        std::cout << std::endl;
    }

    return 0;
}