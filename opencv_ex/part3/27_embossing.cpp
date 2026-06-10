#include "colors.hpp"
#include <iostream>
#include <opencv2/opencv.hpp>

using namespace std;
using namespace cv;

void filter_embossing(Mat &img);
void filter_median();

int main()
{
    // const String folderPath = "/home/aa/kuBig2026/opencv_ex/data/";
    // VideoCapture cap(0, CAP_V4L2);

    // if (!cap.isOpened())
    // {
    //     cerr << "카메라를 열수 없습니다." << endl;
    // }

    // // MJPG
    // cap.set(CAP_PROP_FOURCC, VideoWriter::fourcc('M', 'J', 'P', 'G'));
    // cap.set(CAP_PROP_FRAME_WIDTH, 640);
    // cap.set(CAP_PROP_FRAME_HEIGHT, 480);
    // cap.set(CAP_PROP_FPS, 30);

    // Mat frame;
    // for (int i = 0; i < 1000; ++i)
    // {
    //     cap >> frame;
    //     if (waitKey(30) == 27)
    //         break;
    //     filter_embossing(frame);
    //     imshow("frame", frame);
    // }
    // cap.release();
    // destroyAllWindows();
    filter_median();
    return 0;
}

void filter_embossing(Mat &img)
{
    float data[] = {-1, -1, 0, -1, 0, 1, 0, 1, 1}; // 커널의 데이터 중요!
    Mat emboss(3, 3, CV_32FC1, data);

    // Mat dst = Mat::zeros(img.size(), img.type());
    filter2D(img, img, -1, emboss, Point(-1, -1), 0, BORDER_REPLICATE);
}

void filter_median()
{
    const String folderPath = "/home/aa/kuBig2026/opencv_ex/data/";
    Mat src = imread(folderPath + "lenna.bmp", IMREAD_GRAYSCALE);

    if (src.empty())
    {
        cerr << "Image load failed!" << endl;
        return;
    }

    int num = (int)(src.total() * 0.1);
    for (int i = 0; i < num; i++)
    {
        int x = rand() % src.cols;
        int y = rand() % src.rows;
        src.at<uchar>(y, x) = (i % 2) * 255;
    }

    Mat dst1;
    GaussianBlur(src, dst1, Size(), 1);

    Mat dst2;
    medianBlur(src, dst2, 3);

    imshow("src", src);
    imshow("dst1", dst1);
    imshow("dst2", dst2);

    waitKey();
    destroyAllWindows();
}