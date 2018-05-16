#ifndef IG_AITE_HPP
#define IG_AITE_HPP

#include <winsock2.h>
#include <string>

namespace Setonix_brachyurus
{
	class aite
	{
	private:
		WSADATA wsaData;
		struct sockaddr_in server;
		SOCKET sock;

	public:
		// コンストラクタ
		aite();

		// デストラクタ
		~aite();

		// 絆
		void connect(std::string ip_address);

		// 送るゾ
		void send(std::string &data);

		// 受け取る
		int resv(std::string &buf);

		// ばいばい(*^^*)
		void close();
	};
}

#endif
