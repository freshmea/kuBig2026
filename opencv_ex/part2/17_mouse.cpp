#include "colors.hpp"
#include <iostream>
#include <opencv2/opencv.hpp>

using namespace std;
using namespace cv;

String folderPath = "/home/aa/kuBig2026/opencv_ex/data/";

void on_mouse(int event, int x, int y , int flags, void *data);

int main()
{
    Mat img = imread(folderPath + "lenna.bmp");

    namedWindow("img");
    setMouseCallback("img", on_mouse, (void *)&img);

    while (true)
    {
        imshow("img", img);
        if (waitKey(30) == 27)
            break;
    }
    destroyAllWindows();
    return 0;
}

void on_mouse(int event, int x, int y, int flags, void *data)
{
    cout << " mouse event 발생!! " << endl;
}