#include "colors.hpp"
#include <iostream>
#include <opencv2/opencv.hpp>
#include <vector>

using namespace std;
using namespace cv;

int main()
{
    const String folderPath = "/home/aa/kuBig2026/opencv_ex/data/";
    Mat img = imread(folderPath + "lenna256.bmp", IMREAD_GRAYSCALE);
    Mat img2 = imread(folderPath + "square.bmp", IMREAD_GRAYSCALE);
    Mat dst1, dst2, dst3, dst4;

    bitwise_and(img, img2, dst1);
    bitwise_or(img, img2, dst2);
    bitwise_xor(img, img2, dst3);
    bitwise_not(img, dst4);

    vector<pair<string, Mat>> images = {
        {"lenna", img},
        {"square", img2},
        {"and", dst1},
        {"or", dst2},
        {"xor", dst3},
        {"not", dst4},
    };

    for (auto [name, image] : images){
        imshow(name, image);
    }

    waitKey();

    return 0;
}