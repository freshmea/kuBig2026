#include <iostream>
#include <opencv2/opencv.hpp>

using namespace std;
using namespace cv;

String folderPath = "/home/aa/kuBig2026/opencv_ex/data/";

int main()
{
    cout << "hello, world" << endl;
    Mat img = imread(folderPath + "20260604_113829.jpg");
    // Mat img = Mat::zeros(480, 640, CV_8UC3);
    Size size(640, 480);
    resize(img, img, size);
    imshow("lenna", img);
    waitKey();

    return 0;
}