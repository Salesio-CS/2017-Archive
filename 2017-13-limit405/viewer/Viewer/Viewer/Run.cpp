//���s����v���O�����֐��Q(Run.h����C���N���[�h)
#include"Run.h"


void Run()//���s�֐�
{

	ChangeWindowMode(TRUE);
	SetGraphMode(960, 540, 16);//��ʃT�C�Y
	SetWindowText("Local Weather Viewer Systems");//�E�B���h�E�e�L�X�g

	DxLib_Init();

	while (ProcessMessage() == 0)
	{



	}

	DxLib_End();


}