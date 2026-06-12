#include "opencv2/opencv.hpp"
#include <iostream>

using namespace cv;
using namespace std;
const String folderPath = "/home/aa/kuBig2026/opencv_ex/data/";
void decode_qrcode();

int main(void)
{
    decode_qrcode();

    return 0;
}

void decode_qrcode()
{
    VideoCapture cap(0);

    cap.set(CAP_PROP_FOURCC, VideoWriter::fourcc('M', 'J', 'P', 'G'));
    cap.set(CAP_PROP_FRAME_WIDTH, 640);
    cap.set(CAP_PROP_FRAME_HEIGHT, 480);
    cap.set(CAP_PROP_FPS, 30);

    if (!cap.isOpened())
    {
        cerr << "Camera open failed!" << endl;
        return;
    }

    QRCodeDetector detector;

    Mat frame;
    while (true)
    {
        cap >> frame;

        if (frame.empty())
        {
            cerr << "Frame load failed!" << endl;
            break;
        }

        vector<Point> points;
        String info = detector.detectAndDecode(frame, points);

        if (!info.empty())
        {
            polylines(frame, points, true, Scalar(0, 0, 255), 2);
            putText(frame, info, Point(10, 30), FONT_HERSHEY_DUPLEX, 1, Scalar(0, 0, 255));
        }

        imshow("frame", frame);
        if (waitKey(1) == 27)
            break;
    }
}
