#include "colors.hpp"
#include <iostream>
#include <opencv2/opencv.hpp>

using namespace std;
using namespace cv;

int main()
{
    const String folderPath = "/home/aa/kuBig2026/opencv_ex/data/";
    double min, max;

    cout << "hello, world" << endl;
    Mat img = imread(folderPath + "hawkes.bmp", IMREAD_GRAYSCALE);
    Mat img2 = 2.f * img;
    Mat img3 = img + (img -128) * 1.f;
    minMaxLoc(img, &min, &max);
    Mat img4 = (img - min) * 255 / (max - min);

    imshow("lenna", img);
    imshow("multiple", img2);
    imshow("center contrast", img3);
    imshow("stretching", img4);
    waitKey();

    return 0;
}