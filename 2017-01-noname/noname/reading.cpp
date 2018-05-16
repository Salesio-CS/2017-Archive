	int capture(int argc, char* argv[])
	{
		Mat mat;
		VideoCapture vcap(0);

		if (!vcap.isOpened())
			return -1;

		while (1) {
			vcap >> mat;
			Sleep(3000);
			imshow("camera", mat);
			imwrite("grid.jpg", mat);

		}
		return 0;
	}
