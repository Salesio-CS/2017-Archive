//
//  main.cpp
//  noname
//
//  Created by wataneko on 2017/05/25.
//  Copyright © 2017年 wataneko. All rights reserved.
//
#include <iostream>
#include <string>
#include <stdlib.h>
#include <time.h>
#include <fstream>
#include <vector>

using namespace std;

//盤のサイズ
#define SIZE 9

//駒の列挙型-------------------------------------------------------------------------------------------
enum PIECE{
    FU=1,KY,KE,GI,KI,KA,HI,OU,TO,NY,NK,NG,UM,RY
};

//指し手のクラス-----------------------------------------------------------------------------------------
class Phase {
public:
    int before;
    int after;
    int time;
    PIECE piece;
};

//情報のタイプを示す列挙型--------------------------------------------------------------------------------
enum PROP{
    SITE,SENTE,GOTE,START,END
};


//数字を駒の文字列にする関数------------------------------------------------------------------------------
//n:駒名　手番込みでも可
//hasPhase:手番込みであるか　trueの場合＋ーが文字列の先頭につきます
string getPiece(int n,bool hasPhase=false){
    string Pieces[] = {"","FU","KY","KE","GI","KI","KA","HI","OU","TO","NY","NK","NG","UM","RY"};
    string s("");
    if(hasPhase)
        s += (n<0)?("-"):((n>0)?("+"):(" * ")) ;
    s += Pieces[abs(n)];
    return s;
}

//整数の２次元配列から盤面を表示する関数--------------------------------------------------------------------
void showBoard(int (*board)[SIZE]){
    for(int i=0;i<SIZE;i++){
        cout << "P" << i+1;
        for(int j=0;j<SIZE;j++){
            cout << getPiece(board[i][j],true);
        }
        cout << endl;
    }
}

//棋譜の情報などを入力する関数----------------------------------------------------------------------------
void printProp(PROP type,string s){
    switch(type){
        case SITE:
            s="$SITE:"+s;
            break;
        case SENTE:
            s="N+"+s;
            break;
        case GOTE:
            s="N-"+s;
            break;
        case START:
            s="$START_TIME:"+s;
            break;
        case END:
            s="$END_TIME:"+s;
            break;
    }
    cout << s << endl;
}

//指し手を計算する関数-----------------------------------------------------------------------------------
//b:移動前の駒の位置
//a:移動後の駒の位置
//p:移動した駒の種類
void printPhase(int b,int a,int p,int t=-1){
    static int tb,tn=(int)time(NULL);
    static bool turn=true;//先手か後手か、true=先手
    int td;
    string s=(turn)?("+"):("-");
    turn ^= true;//先手と後手の切り替え
    //前回関数を呼び出した時と今回呼び出した時の時刻の差を計算
    tb=tn;
    tn=(int)time(NULL);
    td=tn-tb;
    
    //書き込む
    //時間の書き込み
    cout << "T" ;
    if(t!=-1){
        cout << t << endl;
    }else{
        cout << td << endl;
    }
    //指し手の書き込み
    cout << s << b << a << getPiece(p) << endl;
    
}
//指し手を入力する関数-----------------------------------------------------------------------------------
void inputPhase(vector<Phase> &v){
    string s="";
    int i=1,t;
    while(1){
        Phase ph;
        cout << i << "手目" << endl;
        cout << "指した駒の位置を入力してください" << endl;
        cout << "移動前" << endl;
        cin >> ph.before;
        cout << "移動後" << endl;
        cin >> ph.after;
        cout << "指した駒の番号を入力してください" << endl;
        cout << "1:歩,2:香車,3:桂馬,4:銀将,5:金将,6:角行,7:飛車,8:王,9:と金,10:成香,11:成桂,12:成銀,13:竜馬,14:竜王" << endl;
        cin >> t;
        ph.piece = (PIECE)t;
        v.push_back(ph);
        cout << "この手で終了するなら１、終了しないなら０を入力してください" << endl;
        cin >> t;
        if(t){
            break;
        }
        
        i++;
    }
}

//指し手のvector受け取ったら全部表示する関数---------------------------------------------------------------
void printPhase(vector<Phase> &v){
    for( auto i : v )
    {
        printPhase(i.after, i.before, i.piece, i.time);
    }
}


//メイン関数-------------------------------------------------------------------------------------------
int main(int argc, const char * argv[]) {
    //初期の盤面
    int board[SIZE][SIZE]={
        {-2,-3,-4,-5,-8,-5,-4,-3,-2},
        { 0,-7, 0, 0, 0, 0, 0,-6, 0},
        {-1,-1,-1,-1,-1,-1,-1,-1,-1},
        { 0, 0, 0, 0, 0, 0, 0, 0, 0},
        { 0, 0, 0, 0, 0, 0, 0, 0, 0},
        { 0, 0, 0, 0, 0, 0, 0, 0, 0},
        { 1, 1, 1, 1, 1, 1, 1, 1, 1},
        { 0, 6, 0, 0, 0, 0, 0, 7, 0},
        { 2, 3, 4, 5, 8, 5, 4, 3, 2},
    };
    string fn,sente,gote,site;
    vector<Phase> tern;
    
    //初期設定
    int n=2;
    time_t      timep;
    struct tm   *time_inf;
    int y,m,d,h,min,sec;
    
    // 紀元からの経過秒数を得る
    timep = time(NULL);
    
    // ローカル標準時へ変換
    time_inf = localtime(&timep);
    
    //現在の時間を定義
    y = time_inf->tm_year + 1900;   /* 年 */
    m = time_inf->tm_mon + 1;       /* 月 */
    d = time_inf->tm_mday;          /* 日 */
    h = time_inf->tm_hour;          /* 時 */
    min = time_inf->tm_min;         /* 分 */
    sec = time_inf->tm_sec;         /* 秒 */
    
    std::string start = std::to_string(y) + "/" + std::to_string(m) + "/" + std::to_string(d) + " " + std::to_string(h) + ":" + std::to_string(min) + ":" + std::to_string(sec); //開始時刻の定義
    
    cout << "先手の名前を入力してください" << endl;
    cin >> sente;
    cout << "後手の名前を入力してください" << endl;
    cin >> gote;
    cout << "試合を行っている場所を入力してください" << endl;
    cin >> site;
    
    while(n==2){
    cout << "ファイル名を指定しますか？(y=1/n=0)" << endl;
    cin >> n;
    if(n==0){
        fn = sente + " vs. " + gote + ".csa";
    }else if(n==1){
        cout << "ファイル名を指定してください" << endl;
        cin >> fn;
        fn = fn + ".csa";
    }else{
        cout << "入力が適正ではありません,入力し直してください" << endl;
        n=2;
    }
    }

    inputPhase(tern);
    
    //file
    ofstream wf;
    wf.open(fn, ios::out);
    
    cout << "writing " << fn << "..." << endl;
    streambuf* last = cout.rdbuf();
    
    //出力先を標準出力にするにはこの行をコメントアウトする
    cout.rdbuf(wf.rdbuf());
    
    // 紀元からの経過秒数を得る
    timep = time(NULL);
    
    // ローカル標準時へ変換
    time_inf = localtime(&timep);
    
    //現在の時間を定義
    y = time_inf->tm_year + 1900;   /* 年 */
    m = time_inf->tm_mon + 1;       /* 月 */
    d = time_inf->tm_mday;          /* 日 */
    h = time_inf->tm_hour;          /* 時 */
    min = time_inf->tm_min;         /* 分 */
    sec = time_inf->tm_sec;         /* 秒 */
    
    std::string end= std::to_string(y) + "/" + std::to_string(m) + "/" + std::to_string(d) + " " + std::to_string(h) + ":" + std::to_string(min) + ":" + std::to_string(sec); //終了時刻の定義
    
    cout<< "v2.2" << endl;
    printProp(SENTE, sente);
    printProp(GOTE, gote);
    printProp(SITE, site);
    printProp(START, start);
    printProp(END, end);
    
    showBoard(board);
    
    printPhase(tern);
    cout << "%%TORYO" << endl;
    
    //    //test
    //    printPhase(77, 76, FU);
    //    printPhase(33, 34, FU);
    //    printPhase(67, 66, FU);
    //    printPhase(83, 84, FU);
    
    wf.close();
    cout.rdbuf(last);
    cout << "wrote " << fn << "!" << endl;
    
    
    return 0;
}
