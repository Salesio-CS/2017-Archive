#include <stdio.h>
#include <stdlib.h>
#include <math.h>

typedef unsigned short WORD;
typedef unsigned long DWORD;
typedef long LONG;
typedef unsigned char BYTE;

struct BITMAPINFOHEADER{
	DWORD      biSize;
	LONG       biWidth;
	LONG       biHeight;
	WORD       biPlanes;
	WORD       biBitCount;
	DWORD      biCompression;
	DWORD      biSizeImage;
	LONG       biXPelsPerMeter;
	LONG       biYPelsPerMeter;
	DWORD      biClrUsed;
	DWORD      biClrImportant;
};

struct BITMAPFILEHEADER {
        WORD    bfType;
        DWORD   bfSize;
        WORD    bfReserved1;
        WORD    bfReserved2;
        DWORD   bfOffBits;
};

typedef struct{
	BITMAPFILEHEADER fileheader;
	BITMAPINFOHEADER infoheader;
}BmpHeader;

typedef struct{
	unsigned char b;
	unsigned char g;
	unsigned char r;
}Rgb;


int main(int argc, char *argv[])
{

	if(argc != 4){
		perror("argv error");
		exit(EXIT_FAILURE);
	}

	FILE *fp_i, *fp_o ,*fp_b;
	BmpHeader header = { 0 };
	
	if ((fp_i = fopen(argv[1], "rb")) == NULL){
		exit(EXIT_FAILURE);
	}
	if ((fp_b = fopen(argv[2], "rb")) == NULL){
		exit(EXIT_FAILURE);
	}

	//ファイルヘッダ読み込み
	fread(&header.fileheader.bfType, sizeof(WORD), 1, fp_i);
	fread(&header.fileheader.bfSize, sizeof(DWORD), 1, fp_i);
	fread(&header.fileheader.bfReserved1, sizeof(WORD), 1, fp_i);
	fread(&header.fileheader.bfReserved2, sizeof(WORD), 1, fp_i);
	fread(&header.fileheader.bfOffBits, sizeof(DWORD), 1, fp_i);

	//情報ヘッダ読み込み
	fread(&header.infoheader.biSize, sizeof(DWORD), 1, fp_i);
	fread(&header.infoheader.biWidth, sizeof(LONG), 1, fp_i);
	fread(&header.infoheader.biHeight, sizeof(LONG), 1, fp_i);
	fread(&header.infoheader.biPlanes, sizeof(WORD), 1, fp_i);
	fread(&header.infoheader.biBitCount, sizeof(WORD), 1, fp_i);
	fread(&header.infoheader.biCompression, sizeof(DWORD), 1, fp_i);
	fread(&header.infoheader.biSizeImage, sizeof(DWORD), 1, fp_i);
	fread(&header.infoheader.biXPelsPerMeter, sizeof(LONG), 1, fp_i);
	fread(&header.infoheader.biYPelsPerMeter, sizeof(LONG), 1, fp_i);
	fread(&header.infoheader.biClrUsed, sizeof(DWORD), 1, fp_i);
	fread(&header.infoheader.biClrImportant, sizeof(DWORD), 1, fp_i);

	fseek(fp_i, 54, SEEK_SET);
	fseek(fp_b, 54, SEEK_SET);

	int count_all = 0;
	int count_dif = 0;

	unsigned char light = 10;

	for (int i = 0; i < header.infoheader.biWidth; i++){
		for (int j = 0; j < header.infoheader.biHeight; j++){
			count_all++;
			Rgb color_i = { 0, 0, 0 };
			Rgb color_b = { 0, 0, 0 };
			Rgb color_plus10 = { 0, 0, 0 };
			Rgb color_minus10 = { 0, 0, 0 };
			fread(&color_i.b, sizeof(BYTE), 1, fp_i);
			fread(&color_i.g, sizeof(BYTE), 1, fp_i);
			fread(&color_i.r, sizeof(BYTE), 1, fp_i);
			fread(&color_b.b, sizeof(BYTE), 1, fp_b);
			fread(&color_b.g, sizeof(BYTE), 1, fp_b);
			fread(&color_b.r, sizeof(BYTE), 1, fp_b);
			if(color_b.b < light){
				color_plus10.b = color_b.b + light;
				color_minus10.b = 0;
			}else if(color_b.b > 255 - light){
				color_plus10.b = 255;
				color_minus10.b = color_b.b - light;
			}else{
				color_plus10.b = color_b.b + light;
				color_minus10.b = color_b.b - light;
			}
			if(color_b.g < light){
				color_plus10.g = color_b.g + light;
				color_minus10.g = 0;
			}else if(color_b.g > 255 - light){
				color_plus10.g = 255;
				color_minus10.g = color_b.g - light;
			}else{
				color_plus10.g = color_b.g + light;
				color_minus10.g = color_b.g - light;
			}
			if(color_b.r < light){
				color_plus10.r = color_b.r + light;
				color_minus10.r = 0;
			}else if(color_b.r > 255 - light){
				color_plus10.r = 255;
				color_minus10.r = color_b.r - light;
			}else{
				color_plus10.r = color_b.r + light;
				color_minus10.r = color_b.r - light;
			}
			if (color_i.b > color_minus10.b && color_i.b < color_plus10.b || color_i.g > color_minus10.g && color_i.g < color_plus10.g || color_i.r > color_minus10.r && color_i.r < color_plus10.r){
				/*fprintf(stderr, "[%d] color_i.b = %d\n", count_all, color_i.b);
				fprintf(stderr, "[%d] color_i.g = %d\n", count_all, color_i.g);
				fprintf(stderr, "[%d] color_i.r = %d\n", count_all, color_i.r);
				fprintf(stderr, "[%d] color_b.b = %d\n", count_all, color_b.b);
				fprintf(stderr, "[%d] color_b.g = %d\n", count_all, color_b.g);
				fprintf(stderr, "[%d] color_b.r = %d\n", count_all, color_b.r);
				fprintf(stderr, "[%d] color_minus.b = %d\n", count_all, color_minus10.b);
				fprintf(stderr, "[%d] color_minus.g = %d\n", count_all, color_minus10.g);
				fprintf(stderr, "[%d] color_minus.r = %d\n", count_all, color_minus10.r);
				fprintf(stderr, "[%d] color_plus.b = %d\n", count_all, color_plus10.b);
				fprintf(stderr, "[%d] color_plus.g = %d\n", count_all, color_plus10.g);
				fprintf(stderr, "[%d] color_plus.r = %d\n", count_all, color_plus10.r);*/
			}else{
				count_dif++;
				//fprintf(stderr, "count_dif++ [%d]\n", count_dif);
			}
		}
	}

	int dif_per = count_dif * 100 / count_all;

	fprintf(stderr, "%d/%d %d%%\n", count_dif, count_all, dif_per);

	if (dif_per > 80){
		if ((fp_o = fopen(argv[3], "wb")) == NULL){
			exit(EXIT_FAILURE);
		}
		//ファイルヘッダ書き込み
		fwrite(&header.fileheader.bfType, sizeof(WORD), 1, fp_o);
		fwrite(&header.fileheader.bfSize, sizeof(DWORD), 1, fp_o);
		fwrite(&header.fileheader.bfReserved1, sizeof(WORD), 1, fp_o);
		fwrite(&header.fileheader.bfReserved2, sizeof(WORD), 1, fp_o);
		fwrite(&header.fileheader.bfOffBits, sizeof(DWORD), 1, fp_o);
	
		//情報ヘッダ書き込み
		fwrite(&header.infoheader.biSize, sizeof(DWORD), 1, fp_o);
		fwrite(&header.infoheader.biWidth, sizeof(LONG), 1, fp_o);
		fwrite(&header.infoheader.biHeight, sizeof(LONG), 1, fp_o);
		fwrite(&header.infoheader.biPlanes, sizeof(WORD), 1, fp_o);
		fwrite(&header.infoheader.biBitCount, sizeof(WORD), 1, fp_o);
		fwrite(&header.infoheader.biCompression, sizeof(DWORD), 1, fp_o);
		fwrite(&header.infoheader.biSizeImage, sizeof(DWORD), 1, fp_o);
		fwrite(&header.infoheader.biXPelsPerMeter, sizeof(LONG), 1, fp_o);
		fwrite(&header.infoheader.biYPelsPerMeter, sizeof(LONG), 1, fp_o);
		fwrite(&header.infoheader.biClrUsed, sizeof(DWORD), 1, fp_o);
		fwrite(&header.infoheader.biClrImportant, sizeof(DWORD), 1, fp_o);
		
		fseek(fp_i, 54, SEEK_SET);
		fseek(fp_b, 54, SEEK_SET);
		fseek(fp_o, 54, SEEK_SET);

		double max = 255.0;
		double gamma = 2.5;

		for (int i = 0; i < header.infoheader.biWidth; i++){
			for (int j = 0; j < header.infoheader.biHeight; j++){
				Rgb color_i = { 0, 0, 0 };
				Rgb color_o = { 0, 0, 0 };
				fread(&color_i.b, sizeof(BYTE), 1, fp_i);
				fread(&color_i.g, sizeof(BYTE), 1, fp_i);
				fread(&color_i.r, sizeof(BYTE), 1, fp_i);
				color_o.b = max * pow(color_i.b / max, 1 / gamma);
				color_o.g = max * pow(color_i.g / max, 1 / gamma);
				color_o.r = max * pow(color_i.r / max, 1 / gamma);
				fwrite(&color_o.b, sizeof(BYTE), 1, fp_o);
				fwrite(&color_o.g, sizeof(BYTE), 1, fp_o);
				fwrite(&color_o.r, sizeof(BYTE), 1, fp_o);
			}
			if (header.infoheader.biHeight * 3 % 4 != 0){
				int padding = header.infoheader.biHeight * 3 % 4;
				int padding_f;
				fread(&padding_f, sizeof(BYTE), padding, fp_i);
				fwrite(&padding_f, sizeof(BYTE), padding, fp_o);
			}
		}
		fclose(fp_o);
	}

	fclose(fp_i);
	fclose(fp_b);

	return 0;

}