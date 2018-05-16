#include "aite.hpp"

#include <cstdio>
#include <winsock2.h>
#include <string>

using namespace Setonix_brachyurus;

// コンストラクタ
aite::aite()
{
	// winsock2の初期化
	::WSAStartup(MAKEWORD(2,0), &wsaData);
}

// デストラクタ
aite::~aite()
{
	aite::close();
	::WSACleanup();																	// (○・▽・○)おわりだよ～
}

// 絆
void aite::connect(std::string ip_address)
{
	// ソケットの作成
	sock = ::socket(AF_INET, SOCK_STREAM, 0);

	// 接続先指定用構造体の準備
	server.sin_family = AF_INET;
	server.sin_port = htons(4096);
	server.sin_addr.S_un.S_addr = inet_addr(ip_address.data());

	// つながれ！
	::connect(sock, (struct sockaddr *)&server, sizeof(server));
}

// 送るゾ
void aite::send(std::string &data)
{
	::send(sock, data.data(), data.size(), 0);												// 届け アイドル
}

// 受け取る
int aite::resv(std::string &buf)
{
	char b[810];
	int n = ::recv(sock, b, sizeof(b), 0);													// 受け取るんば
	b[n] = 0;
	buf = std::string(b);
	return n;
}

// ばいばい(*^^*)
void aite::close()
{
	::shutdown(sock, SD_BOTH);																// バイバイソケット
	::closesocket(sock);
}
