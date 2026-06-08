#include <iostream>
#include <opencv2/opencv.hpp>

using namespace std;
using namespace cv;

String folderPath = "/home/aa/kuBig2026/opencv_ex/data/";

int main()
{
    Point_<int> p1(1, 3);
    Point_<float> p2(3.14, 4.31);
    Point_<int> p3(5, 8);

    cout << p1 << p2 << endl;
    cout << p1 + p3 << endl;

    return 0;
}
