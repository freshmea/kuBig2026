#include "colors.hpp"
#include <iostream>
#include <opencv2/opencv.hpp>

using namespace std;
using namespace cv;

String folderPath = "/home/aa/kuBig2026/opencv_ex/data/";

int main()
{
    Mat img(400, 600, CV_8UC3, Color::White);
    // 400 높이, 600 넓이 배열의 논리 [y][x] {{x1...} {x2...}}

    int a = 0, b = 0, c = 0;
    while (true)
    {
        Mat img2 = img.clone();
        line(img2, Point(50, 50), Point(200 + a, 100 + b), Color::Blue, 3);
        arrowedLine(img2, Point(50 + a, 100), Point(200, 50), Color::Orange, 3, LINE_8);
        drawMarker(img2, Point(600 - a, 400 - b), Color::Red, MARKER_STAR);
        // Point (x(넓이), y(높이))
        rectangle(img2, Rect(300, 50, 50 + c, 50 + c), Color::Red, 2, LINE_AA);
        circle(img2, Point(350, 150), 20, Color::Yellow, 2, LINE_AA);
        ellipse(img2, Point(500, 50), Size(60, 30), 20, 0, 0 + c, Color::Cyan, FILLED, LINE_AA);
        imshow("img", img2);
        if(waitKey(1000/30) == 27)
            break;
        a += 1;
        b += 2;
        c += 3;
    }
    destroyAllWindows();
    return 0;
}