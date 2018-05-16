//実行するプログラム関数群(Run.hからインクルード)
#include"Run.h"


void Run()//実行関数
{

	ChangeWindowMode(TRUE);
	SetGraphMode(960, 540, 16);//画面サイズ
	SetWindowText("Local Weather Viewer Systems");//ウィンドウテキスト

	DxLib_Init();

	while (ProcessMessage() == 0)
	{



	}

	DxLib_End();


}