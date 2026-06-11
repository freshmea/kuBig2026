// 카메라 영상을 사용
// trackbar 를 붙여서 내가 원하는 색상 물체에 범위를 얻어냄
// 그 물체 를 사각형 박스를 그려서 따라 다니게 만듬
// mask 영상의 크기를 판단
// ai 활용하기.

#include "colors.hpp"
#include <iostream>
#include <opencv2/opencv.hpp>
#include <vector>

using namespace std;
using namespace cv;

int h_min = 0;
int h_max = 179;
int s_min = 0;
int s_max = 255;
int v_min = 0;
int v_max = 255;

int min_area = 500;

int main()
{
    VideoCapture cap(0, CAP_V4L2);

    if (!cap.isOpened())
    {
        cerr << "카메라를 열 수 없습니다." << endl;
        return -1;
    }

    cap.set(CAP_PROP_FOURCC, VideoWriter::fourcc('M', 'J', 'P', 'G'));
    cap.set(CAP_PROP_FRAME_WIDTH, 640);
    cap.set(CAP_PROP_FRAME_HEIGHT, 480);
    cap.set(CAP_PROP_FPS, 30);

    Mat frame, hsv, mask;
    vector<vector<Point>> contours;

    namedWindow("frame");
    namedWindow("mask");
    namedWindow("trackbar");

    createTrackbar("h_min", "trackbar", &h_min, 179);
    createTrackbar("h_max", "trackbar", &h_max, 179);
    createTrackbar("s_min", "trackbar", &s_min, 255);
    createTrackbar("s_max", "trackbar", &s_max, 255);
    createTrackbar("v_min", "trackbar", &v_min, 255);
    createTrackbar("v_max", "trackbar", &v_max, 255);
    createTrackbar("min_area", "trackbar", &min_area, 10000);

    while (true)
    {
        cap >> frame;

        if (frame.empty())
        {
            cerr << "프레임을 읽을 수 없습니다." << endl;
            break;
        }

        cvtColor(frame, hsv, COLOR_BGR2HSV);

        Scalar lower(h_min, s_min, v_min);
        Scalar upper(h_max, s_max, v_max);

        inRange(hsv, lower, upper, mask);

        contours.clear();

        findContours(mask, contours, RETR_EXTERNAL, CHAIN_APPROX_SIMPLE);

        for (size_t i = 0; i < contours.size(); ++i)
        {
            double area = contourArea(contours[i]);

            if (area < min_area)
                continue;

            Rect box = boundingRect(contours[i]);

            rectangle(frame, box, Color::Red, 2);

            Point center(
                box.x + box.width / 2,
                box.y + box.height / 2);

            circle(frame, center, 4, Color::Blue, -1);

            string text = "area: " + to_string(static_cast<int>(area));

            putText(
                frame,
                text,
                Point(box.x, box.y - 10),
                FONT_HERSHEY_SIMPLEX,
                0.6,
                Color::Red,
                2);
        }

        imshow("frame", frame);
        imshow("mask", mask);

        if (waitKey(30) == 27)
            break;
    }

    cap.release();
    destroyAllWindows();

    return 0;
}