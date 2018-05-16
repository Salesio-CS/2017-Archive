//
//  time.cpp
//  wataneko
//
//  Created by wataneko on 2017/06/29.
//  Copyright © 2017年 wataneko. All rights reserved.
//

#include <iostream>
#include <string>
#include <vector>
#include <stdlib.h>
#include <time.h>

using namespace std;
int time(int argc, const char * argv[]) {
    vector<int> V(1);
    int i;
    int T;
    
    string fn = "test.txt";
    
    //file
    
    
    i=0;
    V[i]=0;
    
    while(i != -1){
        cout<<"消費時間は？"<<endl;
        cin >> T;
        if(T==-1){//終了
            V.push_back(-1);
            i=-1;
        }else{
            V.push_back(T);
            i++;        }
        
        
    }
    return 0;
}
