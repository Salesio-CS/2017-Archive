#include <winsock2.h>
#include <cstdio>

// g++ -o s.exe -l ws2_32 server.cpp

int main()
{
	WSADATA wsaData;
	SOCKET sock0;
	struct sockaddr_in addr;
	struct sockaddr_in client;
	int len;
	SOCKET sock;
	char buf[32];

	// winsock2の初期化
	WSAStartup(MAKEWORD(2,0), &wsaData);

	// ソケットの作成
	sock0 = socket(AF_INET, SOCK_STREAM, 0);

	// ソケットの設定
	addr.sin_family = AF_INET;							// 通信の種類(?)
	addr.sin_port = htons(4096);						// ポート
	addr.sin_addr.S_un.S_addr = INADDR_ANY;				// どのIPアドレスでも受け取ってやるよ
	bind(sock0, (struct sockaddr *)&addr, sizeof(addr));	// アドレスとソケットを紐付け

	printf("準備完了\n");

	// TCPクライアントからの接続要求を待てる状態にする
	listen(sock0, 5);												// 待機！

	// TCPクライアントからの接続要求を受け付ける
	len = sizeof(client);											// サイズ取得
	sock = accept(sock0, (struct sockaddr *)&client, &len);

	printf("繋がったゾ\n");

	// サーバからデータを受信
	memset(buf, 0, sizeof(buf));									// 零梅
	do
	{
		int n = recv(sock, buf, sizeof(buf), 0);						// 受け取るんば

		printf("%d, %s\n", n, buf);										// 表示

		// 届いた分まるまる送り返す
		send(sock, buf, n, 0);										// 届け アイドル

	}while(buf[0] != 'q');

	shutdown(sock0, SD_BOTH);					// sock0 の時送受信機能を殺す
	shutdown(sock, SD_BOTH);					// sock の送受信機能を殺す

	// TCPセッションの終了
	closesocket(sock);												// ばいばい
	closesocket(sock0);

	// winsock2の終了処理
	WSACleanup();													// (○・▽・○)おわりだよ～

	return 0;
}
