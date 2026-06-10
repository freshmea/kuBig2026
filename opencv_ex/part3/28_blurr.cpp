#include "colors.hpp"
#include <iostream>
#include <opencv2/opencv.hpp>

using namespace std;
using namespace cv;

void blur_ex(Mat &img);

int main()
{
    const String folderPath = "/home/aa/kuBig2026/opencv_ex/data/";
    VideoCapture cap(0, CAP_V4L2);

    if (!cap.isOpened())
    {
        cerr << "카메라를 열수 없습니다." << endl;
    }

    // MJPG
    cap.set(CAP_PROP_FOURCC, VideoWriter::fourcc('M', 'J', 'P', 'G'));
    cap.set(CAP_PROP_FRAME_WIDTH, 640);
    cap.set(CAP_PROP_FRAME_HEIGHT, 480);
    cap.set(CAP_PROP_FPS, 30);

    Mat frame;
    for (int i = 0; i < 1000; ++i)
    {
        cap >> frame;
        if (waitKey(30) == 27)
            break;
        blur_ex(frame);
        blur(frame, frame, Size(21,21));
        imshow("frame", frame);
    }
    cap.release();
    destroyAllWindows();
    return 0;
}

void blur_ex(Mat &img)
{
    float data[] = {1, 1, 1, 1, 1, 1, 1, 1, 1}; // 커널의 데이터 중요!
    Mat blur(3, 3, CV_32FC1, data);
    blur = blur / 9.0;

    // Mat dst = Mat::zeros(img.size(), img.type());
    filter2D(img, img, -1, blur, Point(-1, -1), 0, BORDER_REPLICATE);
}