#include <iostream>
#include <opencv2/opencv.hpp>
#include "colors.hpp"

using namespace std;
using namespace cv;


int main()
{
    const String folderPath = "/home/aa/kuBig2026/opencv_ex/data/";
    cout << "hello, world" << endl;
    // Mat img = imread(folderPath + "20260604_113829.jpg");
    // Mat img = Mat::zeros(480, 640, CV_8UC3);
    Mat img = Mat(480, 640, CV_8UC3, Color::Red);
    Size size(640, 480);
    resize(img, img, size);
    imshow("lenna", img);
    waitKey();

    return 0;
}