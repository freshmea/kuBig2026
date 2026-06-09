#include "colors.hpp"
#include <iostream>
#include <opencv2/opencv.hpp>

using namespace std;
using namespace cv;

int main()
{
    const String folderPath = "/home/aa/kuBig2026/opencv_ex/data/";
    String name;
    int age;
    Point pt1;
    vector<float> scores;
    Mat mat1;

    FileStorage fs;
    fs.open(folderPath + "mydata.xml", FileStorage::READ);
    fs["name"] >> name;
    fs["age"] >> age;
    fs["point"] >> pt1;
    fs["scores"] >> scores;
    fs["data"] >> mat1;

    cout << name << age << pt1 << Mat(scores).t() << mat1 << endl;

    fs.release();

    return 0;
}