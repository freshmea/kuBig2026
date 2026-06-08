#include "colors.hpp"
#include <iostream>
#include <opencv2/opencv.hpp>
#include <vector>
#include <array>

using namespace std;
using namespace cv;

String folderPath = "/home/aa/kuBig2026/opencv_ex/data/";

int main()
{
    Mat img;
    Mat img2(100, 200, CV_8UC1);
    Mat img3(100, 200, CV_8UC3, Scalar(0, 0, 255));
    Mat img4(Size(600, 800), CV_8UC3);

    // 외부 메모리 사용
    float data[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    Mat mat5(2, 5, CV_32FC1, data);

    // 동적 할당
    // vector<float> *data2 = new vector<float>(10);
    auto data2 = make_unique<vector<float>>(10);
    // array<float, 10> *data2 = new array<float, 10>;
    // for (int i = 0; i < 10;i++){
    //     data[i] = static_cast<float>(i + 1);
    // }
    for (auto& x : *data2)
    {
        x = 100.0;
    }
    Mat mat6(2, 5, CV_32FC1, data2->data());

    cout << "mat5 : " << mat5 << endl;
    cout << "mat6 : " << mat6 << endl;
    // delete data2; // 반드시 직접 해제 해야 함

    return 0;
}