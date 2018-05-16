#include <cstdio>
#include <winsock2.h>
#include <iostream>
#include <string>

#include "aite.hpp"

// g++ -o c.exe -l ws2_32 client.cpp

using namespace std;

int main(int argc, char *argv[])
{
	Setonix_brachyurus::aite yatu;

	if(argc != 2)																			// コマンドライン引数にIPがなかったらダメ
		return 0;

	// つながっちゃうゾ
	yatu.connect(argv[1]);

	std::string data, buf;
	do
	{
		std::cin >> data;																	// データ入力
		int n = data.size();

		std::cout << "send : \"" << data << "\"[" << n << "]" << std::endl;					// 送るデータと長さ表示

		yatu.send(data);													// 届け アイドル

		// サーバからデータを受信
		n = yatu.resv(buf);												// 受け取るんば

		std::cout << "resv : \"" << buf << "\"[" << n << "]" << std::endl;		// 受け取ったデータと長さ表示

	}while(data != "exit");

	return 0;
}
